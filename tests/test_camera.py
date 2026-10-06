"""camera-protocol camera-messages/1: camera.harpia and its rules."""

import pytest
from samples import camera_stats, control_reply, control_request, device_info, stream_settings

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json


def _rejects(msg, match):
    with pytest.raises(ContractError, match=match):
        to_json(msg)


def test_device_info_lists_every_control_with_its_options():
    back = from_json(mc.DeviceInfo, to_json(device_info()))
    keys = [c.key for c in back.cameras[0].controls]
    assert keys == ["android.sensor.exposureTime", "android.control.aeMode"]
    assert [o.name for o in back.cameras[0].controls[1].options] == ["OFF", "ON"]


def test_reply_reports_unsupported_and_applied_side_by_side():
    back = from_json(mc.ControlReply, to_json(control_reply()))
    statuses = [mc.ControlStatus.Name(r.status) for r in back.results]
    assert statuses == ["CONTROL_STATUS_APPLIED", "CONTROL_STATUS_UNSUPPORTED"]
    assert not back.results[1].HasField("applied")


def test_reply_with_a_clamped_setting():
    r = control_reply()
    r.results[1].status = mc.ControlStatus.Value("CONTROL_STATUS_CLAMPED")
    r.results[1].applied.int_value = 683_709_000
    back = from_json(mc.ControlReply, to_json(r))
    assert back.results[1].requested.int_value != back.results[1].applied.int_value


def test_request_without_stream_leaves_the_stream_alone():
    req = control_request()
    req.ClearField("stream")
    assert not from_json(mc.ControlRequest, to_json(req)).HasField("stream")


@pytest.mark.parametrize("msg, match", [
    (control_request(request_id=""), "request_id and serial can't be empty"),
    (control_request(reply_endpoint="192.168.7.10:5700"), "reply_endpoint .* must be tcp://<host>:<port>"),
    (control_request(reply_endpoint="tcp://*:5700"), "must be tcp://<host>:<port>"),
    (control_request(reply_endpoint="tcp://recorder:70000"), "must be tcp://<host>:<port>"),
    (control_request(want_device_info=0), r"\['want_device_info'\] hold their UNSET value"),
    (control_request(settings=[mc.ControlSetting(key="k", value=mc.ControlValue(int_value=1))] * 2), r"requested twice \['k'\]"),
    (control_reply(serial=""), "request_id and serial can't be empty"),
    (control_reply(device_info=device_info(serial="999")), "isn't the reply's serial"),
    (stream_settings(bitrate_kbps=0), "must be positive"),
    (camera_stats(thermal_status=7), "thermal_status is Android's 0..6"),
    (camera_stats(dropped_frames=-1), "can't be negative"),
    (mc.FpsRange(min_fps=30, max_fps=15), "0 < min <= max"),
    (mc.FrameSize(width=0, height=10), "size must be positive"),
])
def test_camera_rules(msg, match):
    _rejects(msg, match)


def test_camera_info_orientation_and_duplicates():
    info = device_info()
    info.cameras[0].sensor_orientation_deg = 45
    _rejects(info, r"DeviceInfo\.cameras\[0\]: sensor_orientation_deg must be")
    info = device_info()
    info.cameras.append(info.cameras[0])
    _rejects(info, r"duplicate camera ids \['0'\]")
    info = device_info()
    info.cameras[0].controls.append(info.cameras[0].controls[0])
    _rejects(info, "duplicate control keys")
