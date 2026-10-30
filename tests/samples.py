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


def extract_index(**kw):
    body = ["nose", "left_shoulder", "right_shoulder", "left_hip", "right_hip"]
    fields = dict(
        take_id="t003", calibration_take_id="t001",
        calibration_path="calibration/calibration.toml",
        fps=30.0, frames=1260, t0_ns=T0,
        length_unit=_enum("LengthUnit", "LENGTH_UNIT_M"), up_axis=_enum("UpAxis", "UP_AXIS_Z"),
        synced_videos=[mc.SyncedVideo(role="body_2", path="takes/t003/extract/synced/body_2.mp4")],
        alignment=[mc.CameraAlignment(role="body_2", offset_ns=1_000_000, drift_ppm=-19.5,
                                      frames_in=1258, frames_out=1260)],
        points_3d=[mc.PointSet(name="body", role="", path="takes/t003/extract/body_3d.npy",
                               frames=1260, point_names=body)],
        points_2d=[mc.PointSet(name="body", role="body_2", path="takes/t003/extract/2d/body_2_body.npy",
                               frames=1260, point_names=body)],
    )
    fields.update(kw)
    return mc.ExtractIndex(**fields)


def quality_report(**kw):
    fields = dict(
        take_id="t003", calibration_reproj_err_px=0.42,
        cameras=[mc.CameraQuality(role="body_2", detection_rate_body=0.98, detection_rate_left_hand=0.71,
                                  detection_rate_right_hand=0.69, jitter_px=1.8, reproj_err_px=2.3)],
        bones=[mc.BoneStability(bone="upper_arm_left", mean_length_m=0.29, rsd=0.034)],
        ablation=[mc.CameraAblation(removed_role="body_2", mean_shift_m=0.012, mean_rsd_change=0.006)],
    )
    fields.update(kw)
    return mc.QualityReport(**fields)


def mocap_take(frames=3, **kw):
    header = mc.MocapTakeHeader(
        take_id="t003", session_id="s2026-10-05", actor_id="a2", character_id="c1",
        fps=30.0, frame_count=frames, t0_ns=T0,
        length_unit=_enum("LengthUnit", "LENGTH_UNIT_M"), up_axis=_enum("UpAxis", "UP_AXIS_Z"),
        body_joints=["nose", "left_ankle", "right_ankle"],
        left_hand_joints=["left_wrist", "left_index_tip"],
        right_hand_joints=["right_wrist", "right_index_tip"],
    )
    off, on = _enum("Flag", "FLAG_OFF"), _enum("Flag", "FLAG_ON")
    return mc.MocapTake(header=header, frames=[
        mc.MocapFrame(
            frame_id=i, timestamp_ns=T0 + i * 33_333_333,
            body_xyz=[0.0, 0.0, 1.62, 0.1, 0.0, 0.08, -0.1, 0.0, 0.08],
            left_hand_xyz=[0.3, 0.1, 1.0, 0.35, 0.12, 0.98],
            right_hand_xyz=[0.0] * 6, right_hand_missing=[0, 1],  # right hand not seen
            left_foot_contact=on, right_foot_contact=off if i else on,
        )
        for i in range(frames)
    ], **kw)


def device_info(**kw):
    exposure = SAMPLES["ControlCapability"]()
    ae_mode = mc.ControlCapability(
        backend=_enum("ControlBackend", "CONTROL_BACKEND_CAMERA2"), key="android.control.aeMode",
        value_type=_enum("ControlValueType", "CONTROL_VALUE_TYPE_MENU"),
        options=[mc.ControlMenuOption(value=0, name="OFF"), mc.ControlMenuOption(value=1, name="ON")],
        current_value=_int(1), read_only=_enum("Flag", "FLAG_OFF"), unit="",
    )
    fields = dict(
        model="Multilaser M7", serial="200138", android_version="11", app_version="0.1.0",
        h264_encoders=["c2.android.avc.encoder", "OMX.MTK.VIDEO.ENCODER.AVC"],
        cameras=[mc.CameraInfo(
            camera_id="0", facing=_enum("CameraFacing", "CAMERA_FACING_BACK"), hardware_level="LIMITED",
            sensor_orientation_deg=90, focal_lengths_mm=[3.3],
            sizes=[mc.FrameSize(width=1600, height=1200), mc.FrameSize(width=1280, height=720)],
            fps_ranges=[mc.FpsRange(min_fps=15, max_fps=30), mc.FpsRange(min_fps=30, max_fps=30)],
            controls=[exposure, ae_mode],
        )],
    )
    fields.update(kw)
    return mc.DeviceInfo(**fields)


def stream_settings(**kw):
    fields = dict(camera_id="0", width=1600, height=1200, fps=30.0, bitrate_kbps=20000, i_frame_interval_s=1.0)
    fields.update(kw)
    return mc.StreamSettings(**fields)


def control_request(**kw):
    fields = dict(
        request_id="r-17", serial="200138", reply_endpoint="tcp://192.168.7.10:5700", stream=stream_settings(),
        settings=[mc.ControlSetting(key="android.control.aeMode", value=_int(0)),
                  mc.ControlSetting(key="android.sensor.exposureTime", value=_int(8_000_000))],
        want_device_info=_enum("Flag", "FLAG_ON"),
    )
    fields.update(kw)
    return mc.ControlRequest(**fields)


def control_reply(**kw):
    fields = dict(
        request_id="r-17", serial="200138", stream_applied=stream_settings(),
        results=[
            mc.ControlResult(key="android.control.aeMode", requested=_int(0), applied=_int(0),
                             status=_enum("ControlStatus", "CONTROL_STATUS_APPLIED"), note=""),
            mc.ControlResult(key="android.sensor.exposureTime", requested=_int(8_000_000),
                             status=_enum("ControlStatus", "CONTROL_STATUS_UNSUPPORTED"),
                             note="LIMITED device without MANUAL_SENSOR"),
        ],
        device_info=device_info(),
    )
    fields.update(kw)
    return mc.ControlReply(**fields)


def camera_stats(**kw):
    fields = dict(serial="200138", sensor_ns=35_123_093_746_000, camera_fps=29.98, encoder_fps=29.97,
                  dropped_frames=3, cpu_percent=41.5, battery_temp_c=36.2, thermal_status=0)
    fields.update(kw)
    return mc.CameraStats(**fields)


# The default parts of a new film (mocap-writer file-format/layout/1) and one agent space.
FILM_PARTS = (
    ("script", "script.fountain", "writer"),
    ("settings", "settings/script-settings.json", "writer"),
    ("bible", "bible/", "writer"),
    ("annotations", "annotations/", "writer"),
    ("proposals-pcp", "proposals/props-continuity-planner/", "props-continuity-planner"),
    ("history", "history/", "writer"),
)


def film(**kw):
    fields = dict(
        format_version=1,
        origin=mc.FilmOrigin(program="mocap-writer", version="1.0.0"),
        parts=[mc.FilmPart(name=n, path=p, owner=o) for n, p, o in FILM_PARTS],
        spaces=[
            mc.IdSpace(code="w", owner="writer"),
            mc.IdSpace(code="pcp", owner="props-continuity-planner"),
        ],
    )
    fields.update(kw)
    return mc.Film(**fields)


def id_counters(**next_):
    return mc.IdCounters(next=next_ or {"character": 13, "prop": 4})


def _state(name):
    return mc.ValueState.Value(f"VALUE_STATE_{name}")


def bible_value(**kw):
    fields = dict(field="look.color", text="blue", state=_state("SCRIPT_STATED"),
                  source="12", department="props", by="writer")
    fields.update(kw)
    return mc.BibleValue(**fields)


def bible_item(**kw):
    fields = dict(
        id="prop-w-3", name="Xícara Azul", aliases=["xícara"],
        values=[
            bible_value(),
            bible_value(field="look.width", text=None, number="0.08", unit="m",
                        state=_state("CREATOR_APPROVED"), source="decision 2026-10-28", by="creator"),
            bible_value(field="state.state", scene="12.A", text="full"),
            bible_value(field="ownership.owner", text="character-w-1", state=_state("PROPOSAL"),
                        source="12", by="props-continuity-planner"),
            bible_value(field="touch.weight", text=None, number="0.3", unit="kg", state=_state("TBD"),
                        source="12", by="writer", revisit="when the prop is bought"),
        ],
        links=[mc.BibleLink(scene="12"), mc.BibleLink(scene="12.A")],
    )
    fields.update(kw)
    return mc.BibleItem(**fields)


def change(**kw):
    fields = dict(time="2026-10-28T14:03:12.5Z", by="writer", path="bible/props/blue-cup/item.json",
                  record="prop-w-3", op=mc.ChangeOp.Value("CHANGE_OP_UPDATE"),
                  before='{"id": "prop-w-3"}\n', after='{"id": "prop-w-3", "name": "x"}\n')
    fields.update(kw)
    return mc.Change(**fields)


def _script_settings():
    from pathlib import Path
    text = (Path(__file__).resolve().parents[1] / "fixtures" / "script-v1" / "settings"
            / "script-settings.json").read_text()
    s = mc.from_json(mc.ScriptSettings, text)
    s.locations.add(headings=["INT. ROOM - DAY", "INT. ROOM - NIGHT"])
    s.spelling_words.append("açúcar")
    page = s.title_page.pages.add()
    page.strings.add(items=["A FILM"], x_mm=105.0, y_mm=70.5, size_pt=24,
                     align=mc.TextAlign.Value("TEXT_ALIGN_CENTER"), bold=2, italic=1, underlined=1,
                     font=mc.TitleFont.Value("TITLE_FONT_COURIER"))
    return s


def _script_part(name):
    s = _script_settings()
    return {
        "ScriptSettings": s, "PageSettings": s.page, "TextStyle": s.elements[0].screen,
        "ElementStyle": s.elements[0], "PdfFont": s.pdf.bold, "PdfSettings": s.pdf,
        "ScriptStrings": s.strings, "HeaderLine": s.headers.lines[0], "HeaderSettings": s.headers,
        "AutoCompletionList": s.auto_completion[2], "LocationGroup": s.locations[0],
        "TitleString": s.title_page.pages[0].strings[0], "TitlePageLayout": s.title_page.pages[0],
        "TitlePages": s.title_page,
    }[name]


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
    "CameraAlignment": lambda: extract_index().alignment[0],
    "SyncedVideo": lambda: extract_index().synced_videos[0],
    "PointSet": lambda: extract_index().points_3d[0],
    "ExtractIndex": extract_index,
    "CameraQuality": lambda: quality_report().cameras[0],
    "BoneStability": lambda: quality_report().bones[0],
    "CameraAblation": lambda: quality_report().ablation[0],
    "QualityReport": quality_report,
    "MocapTakeHeader": lambda: mocap_take().header,
    "MocapFrame": lambda: mocap_take().frames[0],
    "MocapTake": mocap_take,
    "FrameSize": lambda: mc.FrameSize(width=1600, height=1200),
    "FpsRange": lambda: mc.FpsRange(min_fps=30, max_fps=30),
    "CameraInfo": lambda: device_info().cameras[0],
    "DeviceInfo": device_info,
    "StreamSettings": stream_settings,
    "CameraStats": camera_stats,
    "ControlRequest": control_request,
    "ControlReply": control_reply,
    "FilmOrigin": lambda: film().origin,
    "FilmPart": lambda: film().parts[0],
    "IdSpace": lambda: film().spaces[0],
    "Film": film,
    "IdCounters": id_counters,
    "BibleCatalog": lambda: mc.bible.catalog(),
    "CatalogMap": lambda: mc.bible.catalog().maps[0],
    "CatalogGroup": lambda: mc.bible.catalog().maps[0].groups[1],
    "CatalogField": lambda: mc.bible.catalog().maps[0].groups[1].fields[0],
    "BibleValue": bible_value,
    "BibleLink": lambda: mc.BibleLink(scene="12.A", item="character-w-1"),
    "BibleItem": bible_item,
    "NotProps": lambda: mc.NotProps(words=["OK", "TV"]),
    "Change": lambda: change(),
    **{n: (lambda n=n: _script_part(n)) for n in (
        "ScriptSettings", "PageSettings", "TextStyle", "ElementStyle", "PdfFont", "PdfSettings",
        "ScriptStrings", "HeaderLine", "HeaderSettings", "AutoCompletionList", "LocationGroup",
        "TitleString", "TitlePageLayout", "TitlePages")},
}
