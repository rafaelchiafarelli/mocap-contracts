import json

import pytest
from google.protobuf import descriptor_pb2, descriptor_pool, message_factory

import mocap_contracts
from mocap_contracts import ContractError, from_json, messages, to_json
from samples import SAMPLES

CONTRACT_MESSAGES = sorted(messages.DECLARED_FIELDS)


# ---------------------------------------------------------------- the real contracts

def test_every_contract_message_has_a_sample():
    assert sorted(SAMPLES) == CONTRACT_MESSAGES


@pytest.mark.parametrize("name", CONTRACT_MESSAGES)
def test_every_declared_field_exists_in_the_generated_message(name):
    generated = set(getattr(mocap_contracts, name).DESCRIPTOR.fields_by_name)
    assert set(messages.DECLARED_FIELDS[name]) <= generated


@pytest.mark.parametrize("name", CONTRACT_MESSAGES)
def test_sample_round_trips(name):
    cls = getattr(mocap_contracts, name)
    msg = SAMPLES[name]()
    text = to_json(msg)
    assert set(json.loads(text)) <= set(messages.DECLARED_FIELDS[name])
    assert from_json(cls, text) == msg


def test_bookkeeping_fields_are_never_written():
    cls = mocap_contracts.ControlMenuOption
    msg = SAMPLES["ControlMenuOption"]()
    for field in cls.DESCRIPTOR.fields:  # Harpia's own fields, set on purpose
        if field.name not in messages.DECLARED_FIELDS["ControlMenuOption"]:
            setattr(msg, field.name, 7 if field.cpp_type == field.CPPTYPE_INT32 else "x")
    assert json.loads(to_json(msg)) == {"value": "1", "name": "Manual Mode"}  # int64 is a JSON string


def test_missing_required_rejected():
    with pytest.raises(ContractError, match=r"missing required field\(s\) \['name'\]"):
        from_json(mocap_contracts.ControlMenuOption, '{"value": "1"}')


def test_bookkeeping_key_rejected_on_read():
    with pytest.raises(ContractError, match="unknown field"):
        from_json(mocap_contracts.ControlMenuOption, '{"value": "1", "name": "a", "ORIGINATOR": "x"}')


@pytest.mark.parametrize("text", ["{not json", "[1, 2]", '"name"'])
def test_invalid_json_rejected(text):
    with pytest.raises(ContractError):
        from_json(mocap_contracts.ControlMenuOption, text)


def test_wrong_value_type_rejected():
    with pytest.raises(ContractError):
        from_json(mocap_contracts.ControlMenuOption, '{"value": "1", "name": {"a": 1}}')


def test_harpia_service_message_is_not_a_contract():
    from harpia_generated.protofiles import heartBeat_pb2

    with pytest.raises(ContractError, match="not a contract message"):
        to_json(heartBeat_pb2.heartBeat())


# ---------------------------------------------------------------- UNSET enums

def test_required_enum_left_unset_is_refused_on_write():
    msg = SAMPLES["ControlCapability"]()
    msg.read_only = mocap_contracts.Flag.Value("FLAG_UNSET")
    with pytest.raises(ContractError, match=r"\['read_only'\] hold their UNSET value"):
        to_json(msg)


def test_required_enum_unset_is_refused_on_read():
    data = json.loads(to_json(SAMPLES["ControlResult"]()))
    data["status"] = "CONTROL_STATUS_UNSET"
    with pytest.raises(ContractError, match=r"\['status'\] hold their UNSET value"):
        from_json(mocap_contracts.ControlResult, json.dumps(data))


def test_optional_enum_may_stay_unset():
    msg = mocap_contracts.ControlValue(flag_value=mocap_contracts.Flag.Value("FLAG_UNSET"))
    assert from_json(mocap_contracts.ControlValue, to_json(msg)).HasField("flag_value")


# ---------------------------------------------------------------- nesting (test-only schema)

def _nested_classes():
    f = descriptor_pb2.FileDescriptorProto(name="nested_test.proto", package="t", syntax="proto3")
    inner = f.message_type.add(name="inner")
    inner.field.add(name="label", number=1, type=9, label=1)          # string
    inner.field.add(name="n", number=2, type=5, label=1)              # int32
    inner.field.add(name="ID_" + "a" * 32, number=3, type=5, label=1)  # Harpia-style
    outer = f.message_type.add(name="outer")
    outer.field.add(name="count", number=1, type=5, label=1)
    outer.field.add(name="one", number=2, type=11, label=1, type_name=".t.inner")
    outer.field.add(name="many", number=3, type=11, label=3, type_name=".t.inner")
    outer.field.add(name="ORIGINATOR", number=4, type=9, label=1)
    pool = descriptor_pool.DescriptorPool()
    pool.Add(f)
    get = lambda n: message_factory.GetMessageClass(pool.FindMessageTypeByName(n))  # noqa: E731
    return get("t.outer"), get("t.inner")


OUTER, INNER = _nested_classes()
DECLARED = {"outer": ("count", "one", "many"), "inner": ("label", "n")}
REQUIRED = {"outer": ("count", "one"), "inner": ("n",)}


def _read(obj):
    return from_json(OUTER, json.dumps(obj), declared=DECLARED, required=REQUIRED)


def test_nested_round_trip_drops_bookkeeping_and_keeps_defaults():
    msg = OUTER(count=0, ORIGINATOR="x", one=INNER(label="a", n=0), many=[INNER(n=2)])
    setattr(msg.one, "ID_" + "a" * 32, 8)
    setattr(msg.many[0], "ID_" + "a" * 32, 9)
    text = to_json(msg, declared=DECLARED)
    data = json.loads(text)
    assert data == {
        "count": 0,
        "one": {"label": "a", "n": 0},
        "many": [{"label": "", "n": 2}],
    }
    back = from_json(OUTER, text, declared=DECLARED, required=REQUIRED)
    assert back.count == 0 and back.one.n == 0 and back.many[0].n == 2


@pytest.mark.parametrize(
    "obj, where",
    [
        ({"one": {"n": 1}}, r"outer: missing required field\(s\) \['count'\]"),
        ({"count": 1, "one": {"label": "a"}}, r"outer\.one: missing required"),
        ({"count": 1, "one": {"n": 1}, "many": [{"n": 1}, {}]}, r"outer\.many\[1\]: missing required"),
        ({"count": 1, "one": {"n": 1, "ID_" + "a" * 32: 3}}, r"outer\.one: unknown field"),
        ({"count": 1, "one": "nope"}, r"outer\.one: expected a JSON object"),
    ],
)
def test_nested_violations_rejected_with_their_path(obj, where):
    with pytest.raises(ContractError, match=where):
        _read(obj)
