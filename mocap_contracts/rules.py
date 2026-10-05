"""Contract rules that `required` can't express, per message type.

`to_json` and `from_json` run `check(msg)`, which applies the rules of every
message in the tree (nested ones included) and raises ContractError with the
path of the first violation. Rules check what a message means, never fill
anything in.
"""

from __future__ import annotations

import datetime
from collections.abc import Callable, Iterator

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.message import Message

from mocap_contracts.errors import ContractError

Rule = Callable[[Message], Iterator[str]]

STREAM_FIELDS = ("stream_host", "video_port", "sync_port", "control_port", "stats_port")
PORTS = ("video_port", "sync_port", "control_port", "stats_port")


def _enum_name(msg: Message, field: str) -> str:
    return msg.DESCRIPTOR.fields_by_name[field].enum_type.values_by_number[getattr(msg, field)].name


def _camera_config(msg: Message) -> Iterator[str]:
    if msg.width <= 0 or msg.height <= 0:
        yield f"width and height must be positive, got {msg.width}x{msg.height}"
    if msg.fps <= 0:
        yield f"fps must be positive, got {msg.fps}"
    source = _enum_name(msg, "source")
    if source == "CAMERA_SOURCE_UVC":
        if not msg.HasField("device_hint") or not msg.device_hint:
            yield "a UVC camera needs device_hint"
        extra = [f for f in STREAM_FIELDS if msg.HasField(f)]
        if extra:
            yield f"a UVC camera can't have STREAM fields {extra}"
    elif source == "CAMERA_SOURCE_STREAM":
        missing = [f for f in STREAM_FIELDS if not msg.HasField(f)]
        if missing:
            yield f"a STREAM camera needs {missing}"
        elif not msg.stream_host:
            yield "a STREAM camera needs a non-empty stream_host"
        bad = [f"{f}={getattr(msg, f)}" for f in PORTS
               if msg.HasField(f) and not 1 <= getattr(msg, f) <= 65535]
        if bad:
            yield f"ports must be 1..65535, got {bad}"
        if msg.HasField("device_hint"):
            yield "a STREAM camera can't have device_hint"


def _preprocess_spec(msg: Message) -> Iterator[str]:
    if msg.output_width <= 0 or msg.output_height <= 0:
        yield f"output size must be positive, got {msg.output_width}x{msg.output_height}"


def _crop(msg: Message) -> Iterator[str]:
    if msg.x < 0 or msg.y < 0 or msg.width <= 0 or msg.height <= 0:
        yield f"crop needs x, y >= 0 and a positive size, got {msg.x},{msg.y} {msg.width}x{msg.height}"


def _calibration_board(msg: Message) -> Iterator[str]:
    if msg.squares_x < 2 or msg.squares_y < 2:
        yield f"a ChArUco board needs at least 2x2 squares, got {msg.squares_x}x{msg.squares_y}"
    lengths = ("square_length_mm", "marker_length_mm", "measured_square_length_mm")
    bad = [f for f in lengths if getattr(msg, f) <= 0]
    if bad:
        yield f"lengths must be positive: {bad}"
    elif msg.marker_length_mm >= msg.square_length_mm:
        yield "marker_length_mm must be smaller than square_length_mm"
    if not msg.aruco_dictionary:
        yield "aruco_dictionary is empty"


def _actor(msg: Message) -> Iterator[str]:
    if msg.height_m <= 0:
        yield f"height_m must be positive, got {msg.height_m}"


def _body_length(msg: Message) -> Iterator[str]:
    if msg.length_m <= 0:
        yield f"length_m must be positive, got {msg.length_m}"


def _duplicates(ids: list[str]) -> list[str]:
    return sorted({i for i in ids if ids.count(i) > 1})


def _session(msg: Message) -> Iterator[str]:
    try:
        if datetime.date.fromisoformat(msg.date).isoformat() != msg.date:
            raise ValueError
    except ValueError:
        yield f"date must be YYYY-MM-DD, got {msg.date!r}"
    actors = [a.id for a in msg.actors]
    characters = [c.id for c in msg.characters]
    for what, ids in (("actor", actors), ("character", characters)):
        if dup := _duplicates(ids):
            yield f"duplicate {what} ids {dup}"
    for i, c in enumerate(msg.casting):
        if c.actor_id not in actors:
            yield f"casting[{i}] names unknown actor {c.actor_id!r}"
        if c.character_id not in characters:
            yield f"casting[{i}] names unknown character {c.character_id!r}"


RULES: dict[str, Rule] = {
    "CameraConfig": _camera_config,
    "PreprocessSpec": _preprocess_spec,
    "Crop": _crop,
    "CalibrationBoard": _calibration_board,
    "Actor": _actor,
    "BodyLength": _body_length,
    "Session": _session,
}


def check(msg: Message, path: str | None = None) -> None:
    path = path or msg.DESCRIPTOR.name
    rule = RULES.get(msg.DESCRIPTOR.name)
    if rule:
        for problem in rule(msg):
            raise ContractError(f"{path}: {problem}")
    for field, value in msg.ListFields():
        if field.type != FieldDescriptor.TYPE_MESSAGE or field.message_type.GetOptions().map_entry:
            continue
        if field.label == FieldDescriptor.LABEL_REPEATED:
            for i, child in enumerate(value):
                check(child, f"{path}.{field.name}[{i}]")
        else:
            check(value, f"{path}.{field.name}")
