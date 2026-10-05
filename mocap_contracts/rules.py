"""Contract rules that `required` can't express, per message type.

`to_json` and `from_json` run `check(msg)`, which applies the rules of every
message in the tree (nested ones included) and raises ContractError with the
path of the first violation. Rules check what a message means, never fill
anything in.
"""

from __future__ import annotations

import datetime
import re
from collections.abc import Callable, Iterator

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.message import Message

from mocap_contracts.errors import ContractError
from mocap_contracts.layout import ID_PATTERN

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


def _sync_pair(start: Message, end: Message | None) -> Iterator[str]:
    if _enum_name(start, "kind") != "SYNC_KIND_START":
        yield f"start must be a START event, got {_enum_name(start, 'kind')}"
    if end is not None:
        if _enum_name(end, "kind") != "SYNC_KIND_END":
            yield f"end must be an END event, got {_enum_name(end, 'kind')}"
        if end.host_ts_ns < start.host_ts_ns:
            yield f"end ({end.host_ts_ns}) is before start ({start.host_ts_ns})"


def _take(msg: Message) -> Iterator[str]:
    yield from _sync_pair(msg.start, msg.end if msg.HasField("end") else None)
    if _enum_name(msg, "type") == "TAKE_TYPE_CALIBRATION" and not msg.HasField("board"):
        yield "a CALIBRATION take needs its board"
    if dup := _duplicates([c.config.role for c in msg.cameras]):
        yield f"duplicate camera roles {dup}"


def _take_closed(msg: Message) -> Iterator[str]:
    yield from _sync_pair(msg.start, msg.end)
    if not msg.roles:
        yield "roles is empty"
    if dup := _duplicates(list(msg.roles)):
        yield f"duplicate roles {dup}"


def _span(msg: Message, what: str) -> Iterator[str]:
    negative = [f for f in what.split() if getattr(msg, f) < 0]
    if negative:
        yield f"negative {negative}"
    if msg.last_ts_ns < msg.first_ts_ns:
        yield f"last_ts_ns ({msg.last_ts_ns}) is before first_ts_ns ({msg.first_ts_ns})"


def _camera_file_ready(msg: Message) -> Iterator[str]:
    if not re.fullmatch(r"[0-9a-f]{64}", msg.sha256):
        yield f"sha256 must be 64 lowercase hex characters, got {msg.sha256!r}"
    if not _relative(msg.path):
        yield f"path must be relative to the take folder, got {msg.path!r}"
    yield from _span(msg, "size_bytes frames")


def _camera_take_report(msg: Message) -> Iterator[str]:
    yield from _span(msg, "frames")
    if msg.fps_measured < 0 or msg.fps_cv < 0:
        yield "fps_measured and fps_cv can't be negative"


def _frame_gap(msg: Message) -> Iterator[str]:
    if msg.after_frame < 0 or msg.duration_ns <= 0:
        yield f"a gap needs after_frame >= 0 and a positive duration, got {msg.after_frame}, {msg.duration_ns}"


def _take_report(msg: Message) -> Iterator[str]:
    if _enum_name(msg, "ok") == "FLAG_ON" and msg.problems:
        yield f"a report with problems can't be ok: {list(msg.problems)}"
    if dup := _duplicates([r.role for r in msg.reports]):
        yield f"duplicate report roles {dup}"


def _relative(path: str) -> bool:
    return bool(path) and not path.startswith("/") and ".." not in path.split("/")


def _extract_index(msg: Message) -> Iterator[str]:
    if msg.fps <= 0:
        yield f"fps must be positive, got {msg.fps}"
    if msg.frames < 0:
        yield f"frames can't be negative, got {msg.frames}"
    paths = [msg.calibration_path] + [v.path for v in msg.synced_videos] + [
        p.path for p in list(msg.points_3d) + list(msg.points_2d)
    ]
    if bad := [p for p in paths if not _relative(p)]:
        yield f"paths must be relative to the session folder: {bad}"
    for what, roles in (
        ("synced video", [v.role for v in msg.synced_videos]),
        ("alignment", [a.role for a in msg.alignment]),
    ):
        if dup := _duplicates(roles):
            yield f"duplicate {what} roles {dup}"
    if bad := [p.name for p in msg.points_3d if p.role]:
        yield f"3D point sets can't name a role: {bad}"
    if bad := [p.name for p in msg.points_2d if not p.role]:
        yield f"2D point sets need a role: {bad}"


def _point_set(msg: Message) -> Iterator[str]:
    if msg.frames < 0:
        yield f"frames can't be negative, got {msg.frames}"
    if dup := _duplicates(list(msg.point_names)):
        yield f"duplicate point names {dup}"


def _camera_quality(msg: Message) -> Iterator[str]:
    rates = ("detection_rate_body", "detection_rate_left_hand", "detection_rate_right_hand")
    if bad := [f for f in rates if not 0 <= getattr(msg, f) <= 1]:
        yield f"rates must be within 0..1: {bad}"
    if bad := [f for f in ("jitter_px", "reproj_err_px") if msg.HasField(f) and getattr(msg, f) < 0]:
        yield f"can't be negative: {bad}"


def _bone_stability(msg: Message) -> Iterator[str]:
    if msg.mean_length_m < 0 or msg.rsd < 0:
        yield "mean_length_m and rsd can't be negative"


def _camera_ablation(msg: Message) -> Iterator[str]:
    if msg.mean_shift_m < 0:
        yield f"mean_shift_m can't be negative, got {msg.mean_shift_m}"


def _quality_report(msg: Message) -> Iterator[str]:
    if msg.HasField("calibration_reproj_err_px") and msg.calibration_reproj_err_px < 0:
        yield "calibration_reproj_err_px can't be negative"
    for what, keys in (
        ("camera", [c.role for c in msg.cameras]),
        ("bone", [b.bone for b in msg.bones]),
        ("ablation", [a.removed_role for a in msg.ablation]),
    ):
        if dup := _duplicates(keys):
            yield f"duplicate {what} entries {dup}"


GROUPS = ("body", "left_hand", "right_hand")


def _mocap_take_header(msg: Message) -> Iterator[str]:
    if msg.fps <= 0:
        yield f"fps must be positive, got {msg.fps}"
    for group in GROUPS:
        if dup := _duplicates(list(getattr(msg, f"{group}_joints"))):
            yield f"duplicate {group} joints {dup}"


def _mocap_frame(frame: Message, header: Message) -> Iterator[str]:
    for group in GROUPS:
        joints = len(getattr(header, f"{group}_joints"))
        xyz = len(getattr(frame, f"{group}_xyz"))
        if xyz != 3 * joints:
            yield f"{group}_xyz has {xyz} values, expected 3 x {joints} joints"
        missing = list(getattr(frame, f"{group}_missing"))
        if bad := [i for i in missing if not 0 <= i < joints]:
            yield f"{group}_missing has out-of-range joints {bad}"
        if dup := _duplicates(missing):
            yield f"{group}_missing lists joints twice {dup}"
    names = len(header.face_blendshape_names)
    if len(frame.face_blendshapes) not in (0, names):
        yield f"face_blendshapes has {len(frame.face_blendshapes)} values, expected 0 or {names}"
    if len(frame.gaze) not in (0, 3):
        yield f"gaze has {len(frame.gaze)} values, expected 0 or 3"


def _mocap_take(msg: Message) -> Iterator[str]:
    if msg.header.frame_count != len(msg.frames):
        yield f"header.frame_count is {msg.header.frame_count} but there are {len(msg.frames)} frames"
    prev = None
    for i, frame in enumerate(msg.frames):
        for problem in _mocap_frame(frame, msg.header):
            yield f"frames[{i}]: {problem}"
        if prev is not None and (frame.frame_id <= prev.frame_id or frame.timestamp_ns <= prev.timestamp_ns):
            yield f"frames[{i}]: frame_id and timestamp_ns must strictly increase"
        prev = frame


def _ids(msg: Message, fields: str) -> Iterator[str]:
    bad = [f"{f}={getattr(msg, f)!r}" for f in fields.split() if not ID_PATTERN.fullmatch(getattr(msg, f))]
    if bad:
        yield f"ids must be letters, digits, '-' or '_' (max 64), got {bad}"


def _chain(*rules: Rule) -> Rule:
    def run(msg: Message) -> Iterator[str]:
        for rule in rules:
            yield from rule(msg)
    return run


RULES: dict[str, Rule] = {
    "CameraConfig": _chain(lambda m: _ids(m, "role"), _camera_config),
    "PreprocessSpec": _preprocess_spec,
    "Crop": _crop,
    "CalibrationBoard": _calibration_board,
    "Actor": _actor,
    "BodyLength": _body_length,
    "Session": _chain(lambda m: _ids(m, "id"), _session),
    "Take": _chain(lambda m: _ids(m, "id session_id"), _take),
    "TakeClosed": _take_closed,
    "CameraFileReady": _camera_file_ready,
    "CameraTakeReport": _camera_take_report,
    "FrameGap": _frame_gap,
    "TakeReport": _take_report,
    "ExtractIndex": _extract_index,
    "PointSet": _point_set,
    "CameraQuality": _camera_quality,
    "BoneStability": _bone_stability,
    "CameraAblation": _camera_ablation,
    "QualityReport": _quality_report,
    "MocapTakeHeader": _mocap_take_header,
    "MocapTake": _mocap_take,
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
