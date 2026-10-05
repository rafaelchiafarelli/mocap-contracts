"""messages-v0/6: the session folder layout."""

from pathlib import Path

import pytest
from samples import session, take, uvc_camera

from mocap_contracts import ContractError, layout, to_json

ROOT = Path("/data/mocap")


def test_session_paths():
    assert layout.session_json(ROOT, "s1") == ROOT / "s1/session.json"
    assert layout.calibration_toml(ROOT, "s1") == ROOT / "s1/calibration/calibration.toml"


def test_take_paths_are_deterministic():
    t = layout.take_dir(ROOT, "s1", "t003")
    assert t == ROOT / "s1/takes/t003"
    assert layout.take_json(t) == t / "take.json"
    assert layout.report_json(t) == t / "report.json"
    assert layout.closed_json(t) == t / "closed.json"
    assert layout.raw_video(t, "body_1") == t / "raw/body_1.mkv"
    assert layout.raw_timestamps(t, "body_1") == t / "raw/body_1.timestamps.csv"
    assert layout.prep_video(t, "body_1") == t / "prep/body_1.mkv"
    assert layout.synced_video(t, "body_1") == t / "extract/synced/body_1.mp4"
    assert layout.index_json(t) == t / "extract/index.json"
    assert layout.quality_json(t) == t / "extract/quality.json"
    assert layout.quality_md(t) == t / "extract/quality.md"
    assert layout.mocap_take_json(t) == t / "adapt/mocap_take.json"
    assert layout.blender_dir(t) == t / "blender"


def test_ready_sidecar_sits_next_to_its_file():
    video = Path("prep/body_1.mkv")
    assert layout.ready_sidecar(video) == Path("prep/body_1.mkv.ready.json")
    assert layout.ready_sidecar(layout.ready_sidecar(video)).name == "body_1.mkv.ready.json.ready.json"


def test_same_relative_paths_on_both_pcs():
    rec = layout.prep_video(layout.take_dir("/rec/data", "s1", "t3"), "face")
    proc = layout.prep_video(layout.take_dir("D:/mocap", "s1", "t3"), "face")
    assert rec.relative_to("/rec/data") == proc.relative_to("D:/mocap")


def test_timestamps_columns():
    assert layout.TIMESTAMPS_COLUMNS == ("frame", "host_ts_ns")


@pytest.mark.parametrize("bad", ["", "../etc", "a/b", "a b", "-lead", "x" * 65, "café", "t.003", None])
def test_invalid_ids_rejected(bad):
    with pytest.raises(ContractError, match="invalid take id"):
        layout.take_dir(ROOT, "s1", bad)


@pytest.mark.parametrize("good", ["t003", "T-3_b", "0", "x" * 64])
def test_valid_ids_accepted(good):
    assert layout.check_id("take", good) == good


def test_message_ids_follow_the_same_pattern():
    with pytest.raises(ContractError, match="ids must be letters"):
        to_json(session(id="s 1"))
    with pytest.raises(ContractError, match=r"session_id='\.\./x'"):
        to_json(take(session_id="../x"))
    with pytest.raises(ContractError, match=r"CameraConfig: ids must be"):
        to_json(uvc_camera(role="body/1"))
