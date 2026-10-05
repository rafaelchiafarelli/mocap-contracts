"""messages-v0/2: session.harpia and its rules."""

import json

import pytest
from samples import board, session, stream_camera, uvc_camera

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json


def _rejects(msg, match):
    with pytest.raises(ContractError, match=match):
        to_json(msg)


# ---------------------------------------------------------------- board

@pytest.mark.parametrize("field", list(mc.messages.REQUIRED_FIELDS["CalibrationBoard"]))
def test_board_missing_any_field_is_rejected(field):
    data = json.loads(to_json(board()))
    del data[field]
    with pytest.raises(ContractError, match=rf"missing required field\(s\) \['{field}'\]"):
        from_json(mc.CalibrationBoard, json.dumps(data))


@pytest.mark.parametrize("kw, match", [
    (dict(squares_x=1), "at least 2x2"),
    (dict(marker_length_mm=0.0), "lengths must be positive"),
    (dict(marker_length_mm=80.0), "marker_length_mm must be smaller"),
    (dict(aruco_dictionary=""), "aruco_dictionary is empty"),
])
def test_board_values_are_checked(kw, match):
    _rejects(board(**kw), match)


# ---------------------------------------------------------------- cameras

def test_uvc_camera_round_trip_has_no_stream_fields():
    data = json.loads(to_json(uvc_camera()))
    assert "stream_host" not in data and "video_port" not in data
    assert from_json(mc.CameraConfig, json.dumps(data)) == uvc_camera()


def test_stream_camera_without_preprocess_means_none():
    cam = stream_camera()
    cam.ClearField("preprocess")
    assert not from_json(mc.CameraConfig, to_json(cam)).HasField("preprocess")


@pytest.mark.parametrize("field", ["stream_host", "video_port", "sync_port", "control_port", "stats_port"])
def test_stream_camera_missing_host_or_any_port_is_rejected(field):
    cam = stream_camera()
    cam.ClearField(field)
    _rejects(cam, rf"STREAM camera needs \['{field}'\]")


@pytest.mark.parametrize("kw, match", [
    (dict(video_port=0), r"ports must be 1\.\.65535"),
    (dict(stats_port=70000), r"ports must be 1\.\.65535"),
    (dict(stream_host=""), "non-empty stream_host"),
    (dict(device_hint="/dev/video0"), "can't have device_hint"),
])
def test_stream_camera_bad_values_rejected(kw, match):
    _rejects(stream_camera(**kw), match)


def test_uvc_camera_without_device_hint_is_rejected():
    cam = uvc_camera()
    cam.ClearField("device_hint")
    _rejects(cam, "UVC camera needs device_hint")


def test_uvc_camera_with_stream_fields_is_rejected():
    _rejects(uvc_camera(stream_host="10.0.0.2"), r"can't have STREAM fields \['stream_host'\]")


def test_camera_source_unset_is_rejected():
    _rejects(uvc_camera(source=0), r"\['source'\] hold their UNSET value")


@pytest.mark.parametrize("kw, match", [(dict(width=0), "width and height"), (dict(fps=0.0), "fps must be positive")])
def test_camera_sizes_checked(kw, match):
    _rejects(uvc_camera(**kw), match)


def test_bad_crop_is_rejected_with_its_path():
    cam = stream_camera()
    cam.preprocess.crop.width = 0
    _rejects(cam, r"CameraConfig\.preprocess\.crop: crop needs")


def test_rules_also_run_on_read():
    data = json.loads(to_json(stream_camera()))
    del data["video_port"]
    with pytest.raises(ContractError, match="STREAM camera needs"):
        from_json(mc.CameraConfig, json.dumps(data))


# ---------------------------------------------------------------- session

def test_casting_is_many_to_many():
    back = from_json(mc.Session, to_json(session()))
    pairs = {(c.actor_id, c.character_id) for c in back.casting}
    assert {("a1", "c1"), ("a2", "c1"), ("a1", "c2")} == pairs


@pytest.mark.parametrize("casting, match", [
    (mc.Casting(actor_id="zz", character_id="c1"), "unknown actor 'zz'"),
    (mc.Casting(actor_id="a1", character_id="zz"), "unknown character 'zz'"),
])
def test_casting_with_unknown_ids_is_rejected(casting, match):
    s = session()
    s.casting.append(casting)
    _rejects(s, match)


def test_duplicate_actor_ids_rejected():
    s = session()
    s.actors.append(mc.Actor(id="a1", name="Other", height_m=1.7))
    _rejects(s, r"duplicate actor ids \['a1'\]")


def test_duplicate_character_ids_rejected():
    s = session()
    s.characters.append(mc.Character(id="c2", name="Other"))
    _rejects(s, r"duplicate character ids \['c2'\]")


@pytest.mark.parametrize("date", ["2026-13-01", "05/10/2026", "2026-10-5", ""])
def test_session_date_must_be_iso(date):
    _rejects(session(date=date), "date must be YYYY-MM-DD")


def test_actor_height_checked_in_a_session_path():
    s = session()
    s.actors[1].height_m = 0.0
    _rejects(s, r"Session\.actors\[1\]: height_m must be positive")
