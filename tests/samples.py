"""One realistic, fully populated sample per contract message.

tests/test_jsonio.py round-trips every one and fails when a contract message
has no sample here, so each new message brings its own.
"""

import mocap_contracts as mc


def _int(v):
    return mc.ControlValue(int_value=v)


def _enum(cls, name):
    return getattr(mc, cls).Value(name)


def uvc_camera(**kw):
    fields = dict(
        role="body_1",
        source=_enum("CameraSource", "CAMERA_SOURCE_UVC"),
        width=1920, height=1080, fps=30.0, notes="webcam on the left tripod",
        device_hint="/dev/v4l/by-id/usb-046d_HD_Pro_Webcam_C920-video-index0",
        controls=[mc.ControlSetting(key="exposure_auto", value=_int(1))],
    )
    fields.update(kw)
    return mc.CameraConfig(**fields)


def stream_camera(**kw):
    fields = dict(
        role="body_2",
        source=_enum("CameraSource", "CAMERA_SOURCE_STREAM"),
        width=1600, height=1200, fps=30.0, notes="",
        stream_host="192.168.50.21", video_port=8080, sync_port=8081,
        control_port=8090, stats_port=8091,
        preprocess=mc.PreprocessSpec(
            crop=mc.Crop(x=200, y=0, width=1200, height=1200),
            output_width=960, output_height=960,
        ),
        controls=[mc.ControlSetting(key="android.control.aeMode", value=_int(0))],
    )
    fields.update(kw)
    return mc.CameraConfig(**fields)


def board(**kw):
    fields = dict(
        squares_x=5, squares_y=7, square_length_mm=80.0, marker_length_mm=60.0,
        aruco_dictionary="DICT_4X4_250", measured_square_length_mm=79.6,
    )
    fields.update(kw)
    return mc.CalibrationBoard(**fields)


def session(**kw):
    fields = dict(
        id="s2026-10-05",
        date="2026-10-05",
        actors=[
            mc.Actor(id="a1", name="Ana Souza", height_m=1.68,
                     lengths=[mc.BodyLength(segment="upper_arm_left", length_m=0.31)]),
            mc.Actor(id="a2", name="Bruno Lima", height_m=1.82),
        ],
        characters=[mc.Character(id="c1", name="The Knight"), mc.Character(id="c2", name="The Squire")],
        # many-to-many: a1 plays both, c1 is played by both
        casting=[
            mc.Casting(actor_id="a1", character_id="c1"),
            mc.Casting(actor_id="a2", character_id="c1"),
            mc.Casting(actor_id="a1", character_id="c2"),
        ],
    )
    fields.update(kw)
    return mc.Session(**fields)


T0 = 1_759_700_000_000_000_000  # host clock, ns


def sync(kind, ts, source="SYNC_SOURCE_MANUAL"):
    return mc.SyncEvent(kind=_enum("SyncKind", kind), host_ts_ns=ts, source=_enum("SyncSource", source))


def take_camera(cam=None):
    cam = cam or stream_camera()
    tc = mc.TakeCamera(
        config=cam,
        control_results=[mc.ControlResult(
            key="android.sensor.exposureTime", requested=_int(8_000_000), applied=_int(8_000_000),
            status=_enum("ControlStatus", "CONTROL_STATUS_APPLIED"), note="",
        )],
        applied_controls=mc.CameraControls(
            exposure_ns=8_000_000, iso=400, auto_exposure=_enum("Flag", "FLAG_OFF"),
        ),
    )
    if cam.HasField("preprocess"):  # absent means no preprocessing
        tc.applied_preprocess.CopyFrom(cam.preprocess)
    return tc


def take(**kw):
    fields = dict(
        id="t003", session_id="s2026-10-05", type=_enum("TakeType", "TAKE_TYPE_PERFORMANCE"),
        start=sync("SYNC_KIND_START", T0), end=sync("SYNC_KIND_END", T0 + 42_000_000_000),
        casting=[mc.Casting(actor_id="a2", character_id="c1")],
        cameras=[take_camera(), take_camera(uvc_camera())],
    )
    fields.update(kw)
    return mc.Take(**fields)


def file_ready(**kw):
    fields = dict(
        take_id="t003", role="body_2", kind=_enum("FileKind", "FILE_KIND_VIDEO"),
        path="prep/body_2.mkv", size_bytes=412_345_678, sha256="ab" * 32,
        frames=1260, first_ts_ns=T0 + 1_000_000, last_ts_ns=T0 + 41_966_000_000,
    )
    fields.update(kw)
    return mc.CameraFileReady(**fields)


def camera_report(**kw):
    fields = dict(
        role="body_2", frames=1258, fps_measured=29.96, fps_cv=0.012,
        gaps=[mc.FrameGap(after_frame=611, duration_ns=100_000_000)],
        first_ts_ns=T0 + 1_000_000, last_ts_ns=T0 + 41_966_000_000,
    )
    fields.update(kw)
    return mc.CameraTakeReport(**fields)


def take_report(**kw):
    fields = dict(
        take_id="t003", ok=_enum("Flag", "FLAG_OFF"),
        problems=["body_2: 1 gap longer than 1.5 frame periods"],
        reports=[camera_report(), camera_report(role="body_1", gaps=[])],
    )
    fields.update(kw)
    return mc.TakeReport(**fields)


def take_closed(**kw):
    fields = dict(
        take_id="t003", roles=["body_1", "body_2"],
        start=sync("SYNC_KIND_START", T0), end=sync("SYNC_KIND_END", T0 + 42_000_000_000),
    )
    fields.update(kw)
    return mc.TakeClosed(**fields)


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
    "BodyLength": lambda: mc.BodyLength(segment="thigh_right", length_m=0.45),
    "Actor": lambda: session().actors[0],
    "Character": lambda: mc.Character(id="c1", name="The Knight"),
    "Casting": lambda: mc.Casting(actor_id="a1", character_id="c1"),
    "Session": session,
    "Crop": lambda: mc.Crop(x=0, y=60, width=1920, height=960),
    "PreprocessSpec": lambda: stream_camera().preprocess,
    "CameraConfig": stream_camera,
    "CalibrationBoard": board,
    "SyncEvent": lambda: sync("SYNC_KIND_START", T0),
    "CameraControls": lambda: take_camera().applied_controls,
    "TakeCamera": take_camera,
    "Take": take,
    "FrameGap": lambda: mc.FrameGap(after_frame=611, duration_ns=100_000_000),
    "CameraTakeReport": camera_report,
    "TakeReport": take_report,
    "TakeClosed": take_closed,
    "CameraFileReady": file_ready,
}
