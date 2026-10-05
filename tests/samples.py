"""One realistic, fully populated sample per contract message.

tests/test_jsonio.py round-trips every one and fails when a contract message
has no sample here, so each new message brings its own.
"""

import mocap_contracts as mc


def _int(v):
    return mc.ControlValue(int_value=v)


SAMPLES = {
    "ControlValue": lambda: mc.ControlValue(int_values=[15, 30]),  # an fps range
    "ControlMenuOption": lambda: mc.ControlMenuOption(value=1, name="Manual Mode"),
    "ControlCapability": lambda: mc.ControlCapability(
        backend=mc.ControlBackend.Value("CONTROL_BACKEND_CAMERA2"),
        key="android.sensor.exposureTime",
        value_type=mc.ControlValueType.Value("CONTROL_VALUE_TYPE_INT"),
        min_value=_int(13_231),
        max_value=_int(683_709_000),
        default_value=_int(33_333_333),
        current_value=_int(16_666_666),
        read_only=mc.Flag.Value("FLAG_OFF"),
        unit="ns",
    ),
    "ControlSetting": lambda: mc.ControlSetting(
        key="exposure_auto", value=mc.ControlValue(int_value=1)
    ),
    "ControlResult": lambda: mc.ControlResult(
        key="android.control.aeExposureCompensation",
        requested=_int(40),
        applied=_int(12),
        status=mc.ControlStatus.Value("CONTROL_STATUS_CLAMPED"),
        note="clamped to the device maximum",
    ),
}
