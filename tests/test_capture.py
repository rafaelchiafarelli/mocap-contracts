"""messages-v0/3: capture.harpia and its rules."""

import json

import pytest
from samples import T0, board, camera_report, file_ready, sync, take, take_camera, take_closed, take_report, uvc_camera

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json


def _rejects(msg, match):
    with pytest.raises(ContractError, match=match):
        to_json(msg)


def _enum(cls, name):
    return getattr(mc, cls).Value(name)


# ---------------------------------------------------------------- take

def test_take_describes_its_cameras_in_full():
    back = from_json(mc.Take, to_json(take()))
    stream, uvc = back.cameras
    assert stream.config.stream_host == "192.168.50.21" and stream.config.video_port == 8080
    assert uvc.config.device_hint.startswith("/dev/v4l/by-id/")
    assert stream.control_results[0].applied.int_value == 8_000_000


def test_take_while_recording_has_no_end():
    t = take()
    t.ClearField("end")
    assert not from_json(mc.Take, to_json(t)).HasField("end")


def test_calibration_take_needs_its_board():
    calib = take(type=_enum("TakeType", "TAKE_TYPE_CALIBRATION"), casting=[])
    _rejects(calib, "CALIBRATION take needs its board")
    calib.board.CopyFrom(board())
    assert from_json(mc.Take, to_json(calib)).board.squares_x == 5


def test_take_board_is_checked_with_its_path():
    calib = take(type=_enum("TakeType", "TAKE_TYPE_CALIBRATION"), board=board(squares_x=1))
    _rejects(calib, r"Take\.board: a ChArUco board needs")


@pytest.mark.parametrize("start, end, match", [
    (sync("SYNC_KIND_END", T0), sync("SYNC_KIND_END", T0 + 1), "start must be a START event"),
    (sync("SYNC_KIND_START", T0), sync("SYNC_KIND_START", T0 + 1), "end must be an END event"),
    (sync("SYNC_KIND_START", T0), sync("SYNC_KIND_END", T0 - 1), "is before start"),
])
def test_take_sync_events_are_checked(start, end, match):
    _rejects(take(start=start, end=end), match)


def test_sync_source_unset_is_rejected():
    _rejects(take(start=sync("SYNC_KIND_START", T0, "SYNC_SOURCE_UNSET")), r"Take\.start: required field\(s\) \['source'\]")


def test_duplicate_camera_roles_in_a_take_are_rejected():
    _rejects(take(cameras=[take_camera(), take_camera()]), r"duplicate camera roles \['body_2'\]")


def test_camera_config_inside_a_take_is_still_checked():
    bad = uvc_camera()
    bad.ClearField("device_hint")
    _rejects(take(cameras=[take_camera(bad)]), r"Take\.cameras\[0\]\.config: a UVC camera needs device_hint")


def test_camera_controls_are_all_optional():
    empty = mc.CameraControls()
    assert json.loads(to_json(empty)) == {}
    assert not from_json(mc.CameraControls, "{}").HasField("exposure_ns")


# ---------------------------------------------------------------- report

def test_gaps_are_listed():
    back = from_json(mc.CameraTakeReport, to_json(camera_report()))
    assert [(g.after_frame, g.duration_ns) for g in back.gaps] == [(611, 100_000_000)]


def test_report_with_problems_cannot_be_ok():
    _rejects(take_report(ok=_enum("Flag", "FLAG_ON")), "a report with problems can't be ok")


def test_report_ok_unset_is_rejected():
    _rejects(take_report(ok=0), r"\['ok'\] hold their UNSET value")


@pytest.mark.parametrize("kw, match", [
    (dict(frames=-1), "negative"),
    (dict(last_ts_ns=T0), "is before first_ts_ns"),
    (dict(fps_cv=-0.1), "can't be negative"),
])
def test_camera_report_values_checked(kw, match):
    _rejects(camera_report(**kw), match)


def test_bad_gap_rejected_with_its_path():
    _rejects(camera_report(gaps=[mc.FrameGap(after_frame=3, duration_ns=0)]), r"CameraTakeReport\.gaps\[0\]")


def test_duplicate_report_roles_rejected():
    _rejects(take_report(reports=[camera_report(), camera_report()]), r"duplicate report roles \['body_2'\]")


# ---------------------------------------------------------------- hand-off events

@pytest.mark.parametrize("field", list(mc.messages.REQUIRED_FIELDS["CameraFileReady"]))
def test_camera_file_ready_missing_any_field_is_rejected(field):
    data = json.loads(to_json(file_ready()))
    del data[field]
    with pytest.raises(ContractError, match=rf"missing required field\(s\) \['{field}'\]"):
        from_json(mc.CameraFileReady, json.dumps(data))


@pytest.mark.parametrize("kw, match", [
    (dict(sha256="AB" * 32), "64 lowercase hex"),
    (dict(sha256="ab" * 31), "64 lowercase hex"),
    (dict(path="/data/s/t003/prep/body_2.mkv"), "relative to the take folder"),
    (dict(path="../t002/prep/body_2.mkv"), "relative to the take folder"),
    (dict(size_bytes=-5), "negative"),
    (dict(kind=0), r"\['kind'\] hold their UNSET value"),
])
def test_camera_file_ready_values_checked(kw, match):
    _rejects(file_ready(**kw), match)


def test_timestamps_file_ready_round_trips():
    ev = file_ready(kind=_enum("FileKind", "FILE_KIND_TIMESTAMPS"), path="raw/body_2.timestamps.csv", size_bytes=40_312)
    assert from_json(mc.CameraFileReady, to_json(ev)) == ev


def test_take_closed_needs_both_events_and_unique_roles():
    tc = take_closed()
    tc.ClearField("end")
    with pytest.raises(ContractError, match=r"missing required field\(s\) \['end'\]"):
        to_json(tc)
    _rejects(take_closed(roles=["body_1", "body_1"]), r"duplicate roles \['body_1'\]")
    _rejects(take_closed(roles=[]), "roles is empty")


def test_camera_without_preprocessing_has_no_applied_preprocess():
    uvc = from_json(mc.Take, to_json(take())).cameras[1]
    assert not uvc.HasField("applied_preprocess")
