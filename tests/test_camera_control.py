"""messages-v0/1: the camera control vocabulary."""

import json

import mocap_contracts as mc
from mocap_contracts import from_json, to_json


def test_menu_options_keep_their_order():
    cap = mc.ControlCapability(
        backend=mc.ControlBackend.Value("CONTROL_BACKEND_V4L2"),
        key="exposure_auto",
        value_type=mc.ControlValueType.Value("CONTROL_VALUE_TYPE_MENU"),
        options=[
            mc.ControlMenuOption(value=3, name="Aperture Priority Mode"),
            mc.ControlMenuOption(value=1, name="Manual Mode"),
        ],
        current_value=mc.ControlValue(int_value=3),
        read_only=mc.Flag.Value("FLAG_OFF"),
        unit="",
    )
    back = from_json(mc.ControlCapability, to_json(cap))
    assert [o.name for o in back.options] == ["Aperture Priority Mode", "Manual Mode"]


def test_capability_without_reported_limits_has_none():
    cap = mc.ControlCapability(
        backend=mc.ControlBackend.Value("CONTROL_BACKEND_CAMERA2"),
        key="android.colorCorrection.gains",
        value_type=mc.ControlValueType.Value("CONTROL_VALUE_TYPE_FLOAT_LIST"),
        read_only=mc.Flag.Value("FLAG_OFF"),
        unit="",
    )
    data = json.loads(to_json(cap))
    assert "min_value" not in data and "max_value" not in data
    assert not from_json(mc.ControlCapability, to_json(cap)).HasField("min_value")


def test_clamped_result_keeps_requested_and_read_back_apart():
    res = mc.ControlResult(
        key="brightness",
        requested=mc.ControlValue(int_value=300),
        applied=mc.ControlValue(int_value=255),
        status=mc.ControlStatus.Value("CONTROL_STATUS_CLAMPED"),
        note="",
    )
    back = from_json(mc.ControlResult, to_json(res))
    assert (back.requested.int_value, back.applied.int_value) == (300, 255)


def test_unsupported_result_has_no_applied_value():
    res = mc.ControlResult(
        key="android.sensor.exposureTime",
        requested=mc.ControlValue(int_value=8_000_000),
        status=mc.ControlStatus.Value("CONTROL_STATUS_UNSUPPORTED"),
        note="LIMITED device without MANUAL_SENSOR",
    )
    back = from_json(mc.ControlResult, to_json(res))
    assert not back.HasField("applied")


def test_float_list_value_round_trips():
    gains = mc.ControlValue(float_values=[1.5, 1.0, 1.0, 2.25])  # RGGB white balance gains
    assert list(from_json(mc.ControlValue, to_json(gains)).float_values) == [1.5, 1.0, 1.0, 2.25]
