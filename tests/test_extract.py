"""messages-v0/4: extract.harpia and its rules."""

import pytest
from samples import extract_index, quality_report

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json


def _rejects(msg, match):
    with pytest.raises(ContractError, match=match):
        to_json(msg)


def test_index_keeps_point_names_in_array_order():
    back = from_json(mc.ExtractIndex, to_json(extract_index()))
    assert list(back.points_3d[0].point_names)[:2] == ["nose", "left_shoulder"]


@pytest.mark.parametrize("field", ["length_unit", "up_axis"])
def test_index_frame_of_reference_must_be_declared(field):
    _rejects(extract_index(**{field: 0}), rf"\['{field}'\] hold their UNSET value")


@pytest.mark.parametrize("kw, match", [
    (dict(fps=0.0), "fps must be positive"),
    (dict(frames=-1), "frames can't be negative"),
    (dict(calibration_path="/data/calibration.toml"), "relative to the session folder"),
    (dict(calibration_path="../other/calibration.toml"), "relative to the session folder"),
])
def test_index_values_checked(kw, match):
    _rejects(extract_index(**kw), match)


def test_point_set_roles_match_their_dimension():
    idx = extract_index()
    idx.points_3d[0].role = "body_2"
    _rejects(idx, "3D point sets can't name a role")
    idx = extract_index()
    idx.points_2d[0].role = ""
    _rejects(idx, "2D point sets need a role")


def test_duplicate_point_names_rejected_with_path():
    idx = extract_index()
    idx.points_3d[0].point_names.append("nose")
    _rejects(idx, r"ExtractIndex\.points_3d\[0\]: duplicate point names \['nose'\]")


def test_duplicate_alignment_roles_rejected():
    idx = extract_index()
    idx.alignment.append(idx.alignment[0])
    _rejects(idx, r"duplicate alignment roles \['body_2'\]")


def test_quality_optional_fields_may_be_absent():
    q = quality_report()
    q.cameras[0].ClearField("jitter_px")
    q.ClearField("calibration_reproj_err_px")
    back = from_json(mc.QualityReport, to_json(q))
    assert not back.cameras[0].HasField("jitter_px")
    assert not back.HasField("calibration_reproj_err_px")


@pytest.mark.parametrize("field, value", [("detection_rate_body", 1.2), ("detection_rate_left_hand", -0.1)])
def test_detection_rates_within_0_1(field, value):
    q = quality_report()
    setattr(q.cameras[0], field, value)
    _rejects(q, r"QualityReport\.cameras\[0\]: rates must be within 0\.\.1")


def test_negative_reprojection_error_rejected():
    q = quality_report()
    q.cameras[0].reproj_err_px = -1.0
    _rejects(q, "can't be negative")


def test_duplicate_bones_rejected():
    q = quality_report()
    q.bones.append(q.bones[0])
    _rejects(q, r"duplicate bone entries \['upper_arm_left'\]")
