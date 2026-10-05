"""messages-v0/5: adapt.harpia (MocapTake) and its rules."""

import pytest
from samples import mocap_take

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json


def _rejects(msg, match):
    with pytest.raises(ContractError, match=match):
        to_json(msg)


def test_frame_without_face_gaze_or_emotion_is_valid():
    back = from_json(mc.MocapTake, to_json(mocap_take()))
    f = back.frames[0]
    assert list(f.face_blendshapes) == [] and list(f.gaze) == [] and not f.HasField("emotion")


def test_missing_joints_are_explicit():
    back = from_json(mc.MocapTake, to_json(mocap_take()))
    assert list(back.frames[1].right_hand_missing) == [0, 1]


def test_face_gaze_and_emotion_round_trip_when_present():
    t = mocap_take()
    t.header.face_blendshape_names.extend(["jawOpen", "eyeBlinkLeft"])
    t.frames[0].face_blendshapes.extend([0.4, 0.0])
    t.frames[0].gaze.extend([0.0, 1.0, 0.0])
    t.frames[0].emotion = "calm"
    back = from_json(mc.MocapTake, to_json(t))
    assert back.frames[0].emotion == "calm" and len(back.frames[0].gaze) == 3


@pytest.mark.parametrize("mutate, match", [
    (lambda t: t.frames[1].body_xyz.append(0.0), r"frames\[1\]: body_xyz has 10 values, expected 3 x 3"),
    (lambda t: t.frames[0].left_hand_missing.append(5), r"left_hand_missing has out-of-range joints \[5\]"),
    (lambda t: t.frames[0].left_hand_missing.extend([1, 1]), "lists joints twice"),
    (lambda t: t.frames[0].gaze.extend([1.0, 2.0]), "gaze has 2 values"),
    (lambda t: t.frames[0].face_blendshapes.append(0.5), "face_blendshapes has 1 values, expected 0 or 0"),
    (lambda t: setattr(t.frames[2], "frame_id", 1), r"frames\[2\]: frame_id and timestamp_ns must strictly increase"),
    (lambda t: setattr(t.frames[1], "timestamp_ns", t.frames[0].timestamp_ns), "must strictly increase"),
    (lambda t: setattr(t.header, "frame_count", 7), "frame_count is 7 but there are 3 frames"),
    (lambda t: setattr(t.header, "fps", 0.0), r"MocapTake\.header: fps must be positive"),
    (lambda t: setattr(t.frames[0], "left_foot_contact", 0), r"\['left_foot_contact'\] hold their UNSET value"),
    (lambda t: setattr(t.header, "up_axis", 0), r"\['up_axis'\] hold their UNSET value"),
])
def test_take_rules(mutate, match):
    t = mocap_take()
    mutate(t)
    _rejects(t, match)


def test_duplicate_joint_names_rejected_in_the_header():
    header = mocap_take().header
    header.body_joints.append("nose")
    _rejects(header, r"duplicate body joints \['nose'\]")


def test_long_take_stays_fast_and_small():
    import time
    t = mocap_take(frames=3600)  # 2 minutes at 30 fps
    start = time.perf_counter()
    text = to_json(t)
    from_json(mc.MocapTake, text)
    assert time.perf_counter() - start < 10
    assert len(text) < 3_600 * 1_000  # well under 1 kB per frame for this joint set
