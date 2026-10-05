"""JSON for contract messages: declared fields only, `required` enforced.

Files written here contain exactly the fields declared in schema/, under
their declared names, with every non-`optional` field present even when it
holds its default value. Harpia's bookkeeping fields (ID_/STATUS_/ERROR_
<hash>, ORIGINATOR) are never written, and reading rejects any key that
isn't declared or any missing `required` key, at every nesting level.

Every contract enum has `*_UNSET` as its zero value, so a `required` enum
field holding it counts as missing. Writing applies the same checks as
reading, so an invalid file is never produced.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any, TypeVar

from google.protobuf import json_format
from google.protobuf.descriptor import Descriptor, FieldDescriptor
from google.protobuf.message import Message

from mocap_contracts.messages import DECLARED_FIELDS, REQUIRED_FIELDS

M = TypeVar("M", bound=Message)


class ContractError(ValueError):
    """JSON that doesn't match a contract message."""


def to_json(
    msg: Message,
    *,
    declared: Mapping[str, tuple[str, ...]] = DECLARED_FIELDS,
    required: Mapping[str, tuple[str, ...]] = REQUIRED_FIELDS,
) -> str:
    data = json_format.MessageToDict(
        msg, preserving_proto_field_name=True, including_default_value_fields=True
    )
    data = _prune(data, msg.DESCRIPTOR, declared)
    _check(data, msg.DESCRIPTOR, declared, required, msg.DESCRIPTOR.name)
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def from_json(
    cls: type[M],
    text: str,
    *,
    declared: Mapping[str, tuple[str, ...]] = DECLARED_FIELDS,
    required: Mapping[str, tuple[str, ...]] = REQUIRED_FIELDS,
) -> M:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise ContractError(f"invalid JSON for {cls.DESCRIPTOR.name}: {e}") from None
    _check(data, cls.DESCRIPTOR, declared, required, cls.DESCRIPTOR.name)
    try:
        return json_format.ParseDict(data, cls())
    except json_format.ParseError as e:
        raise ContractError(f"{cls.DESCRIPTOR.name}: {e}") from None


def _fields(desc: Descriptor, declared: Mapping[str, tuple[str, ...]]) -> tuple[str, ...]:
    try:
        return declared[desc.name]
    except KeyError:
        raise ContractError(f"{desc.name} is not a contract message") from None


def _is_message(field: FieldDescriptor) -> bool:
    return (
        field.type == FieldDescriptor.TYPE_MESSAGE
        and not field.message_type.GetOptions().map_entry
    )


def _is_unset_enum(field: FieldDescriptor, value: Any) -> bool:
    if field.type != FieldDescriptor.TYPE_ENUM or field.label == FieldDescriptor.LABEL_REPEATED:
        return False
    zero = field.enum_type.values_by_number[0].name
    return value in (0, zero)


def _children(value: Any, field: FieldDescriptor) -> list[Any]:
    if field.label == FieldDescriptor.LABEL_REPEATED:
        return value if isinstance(value, list) else []
    return [value]


def _prune(data: dict[str, Any], desc: Descriptor, declared) -> dict[str, Any]:
    keep = _fields(desc, declared)
    out = {}
    for name, value in data.items():
        if name not in keep:
            continue
        field = desc.fields_by_name[name]
        if _is_message(field):
            if field.label == FieldDescriptor.LABEL_REPEATED:
                value = [_prune(v, field.message_type, declared) for v in value]
            else:
                value = _prune(value, field.message_type, declared)
        out[name] = value
    return out


def _check(data: Any, desc: Descriptor, declared, required, path: str) -> None:
    if not isinstance(data, dict):
        raise ContractError(f"{path}: expected a JSON object for {desc.name}")
    known = _fields(desc, declared)
    unknown = sorted(set(data) - set(known))
    if unknown:
        raise ContractError(f"{path}: unknown field(s) {unknown}")
    missing = [f for f in required.get(desc.name, ()) if f not in data]
    if missing:
        raise ContractError(f"{path}: missing required field(s) {missing}")
    unset = [f for f in required.get(desc.name, ()) if _is_unset_enum(desc.fields_by_name[f], data[f])]
    if unset:
        raise ContractError(f"{path}: required field(s) {unset} hold their UNSET value")
    for name, value in data.items():
        field = desc.fields_by_name[name]
        if _is_message(field) and value is not None:
            for i, child in enumerate(_children(value, field)):
                sub = f"{path}.{name}" + (
                    f"[{i}]" if field.label == FieldDescriptor.LABEL_REPEATED else ""
                )
                _check(child, field.message_type, declared, required, sub)
