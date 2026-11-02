"""camera-protocol stream-protocol/2: the v1 reference reader against its fixtures."""

import csv
import json
from pathlib import Path

import pytest

from mocap_contracts import stream_v1 as v1

FIX = Path(__file__).resolve().parents[1] / "fixtures" / "stream-v1"


def _expected(name):
    with open(FIX / name) as f:
        return [v1.Timestamp(int(r["seq"]), int(r["sensor_ns"]), int(r["device_unix_ns"])) for r in csv.DictReader(f)]


# ---------------------------------------------------------------- real tablet excerpt

def test_tablet_excerpt_matches_the_independent_reader():
    frames = v1.frames((FIX / "tablet-excerpt.h264").read_bytes())
    assert [f.timestamp for f in frames] == _expected("tablet-excerpt.timestamps.csv")
    assert all(not f.problems for f in frames)


def test_tablet_excerpt_starts_with_config_then_a_key_frame():
    nals = [t for t, _ in v1.nal_units((FIX / "tablet-excerpt.h264").read_bytes())]
    assert nals[:4] == [v1.NAL_SPS, v1.NAL_PPS, v1.NAL_SEI, v1.NAL_IDR]
    assert all(f.nal_types == [v1.NAL_SEI, v1.NAL_SLICE] for f in v1.frames((FIX / "tablet-excerpt.h264").read_bytes())[1:])


def test_writer_matches_the_tablet_byte_for_byte():
    data = (FIX / "tablet-excerpt.h264").read_bytes()
    seis = [nal for t, nal in v1.nal_units(data) if t == v1.NAL_SEI]
    for nal, ts in zip(seis, _expected("tablet-excerpt.timestamps.csv")):
        assert v1.build_timestamp_sei(ts.seq, ts.sensor_ns, ts.device_unix_ns) == b"\x00\x00\x00\x01" + nal


# ---------------------------------------------------------------- decodable stream

def test_decodable_timestamps_and_the_skip():
    frames = v1.frames((FIX / "decodable.h264").read_bytes())
    stamps = [f.timestamp for f in frames]
    assert stamps == _expected("decodable.timestamps.csv")
    assert v1.seq_gaps(stamps) == [(4, 6)]


def test_other_uuids_are_ignored():
    data = (FIX / "decodable.h264").read_bytes()
    seis = [nal for t, nal in v1.nal_units(data) if t == v1.NAL_SEI]
    others = [nal for nal in seis if v1.parse_timestamp_sei(nal) is None]
    assert others, "the fixture keeps x264's own SEI"
    assert all(f.timestamp is not None and not f.problems for f in v1.frames(data))


# ---------------------------------------------------------------- garbled

def test_garbled_v1_seis_are_reported_never_read():
    frames = v1.frames((FIX / "garbled.h264").read_bytes())
    assert [f.timestamp.seq if f.timestamp else None for f in frames] == [None, 10, None]
    assert "payloadSize 39" in frames[0].problems[0]
    assert "truncated v1 SEI" in frames[2].problems[0]


def test_slice_without_sei_is_an_untimed_frame():
    good = v1.build_timestamp_sei(1, 10, 20)
    sl = b"\x00\x00\x00\x01\x41\x9a\x9a"
    frames = v1.frames(good + sl + sl)
    assert frames[0].timestamp.seq == 1
    assert frames[1].timestamp is None and frames[1].problems == ["slice without a v1 timestamp SEI"]


# ---------------------------------------------------------------- SEI encoding

@pytest.mark.parametrize("seq, sensor, unix", [
    (1, 0, 0),                                    # all zeros: emulation prevention everywhere
    (0x0000000100000003, 0x0300000000000000, 1),
    (2**63 - 1, 2**63 - 1, 2**63 - 1),
])
def test_sei_round_trips_through_emulation_prevention(seq, sensor, unix):
    nal = v1.build_timestamp_sei(seq, sensor, unix)[4:]
    assert b"\x00\x00\x00" not in nal and b"\x00\x00\x01" not in nal and b"\x00\x00\x02" not in nal
    assert v1.parse_timestamp_sei(nal) == v1.Timestamp(seq, sensor, unix)


def test_non_sei_nal_is_not_a_timestamp():
    assert v1.parse_timestamp_sei(b"\x65\x88") is None


# ---------------------------------------------------------------- clock sync

def test_sync_packets():
    s = json.loads((FIX / "sync.json").read_text())
    assert v1.sync_request(s["request"]["token"]).hex() == s["request"]["hex"]
    r = s["reply"]
    assert v1.parse_sync_reply(bytes.fromhex(r["hex"])) == (r["token"], r["sensor_ns"], r["device_unix_ns"])


def test_short_sync_reply_is_an_error():
    with pytest.raises(v1.StreamError, match="sync reply of 16 bytes"):
        v1.parse_sync_reply(b"\x00" * 16)


def test_sync_offset_uses_the_fastest_probes():
    s = json.loads((FIX / "sync.json").read_text())
    probes = [v1.Probe(**p) for p in s["probes"]]
    assert v1.sync_offset(probes) == s["expected_offset_ns"] == 1_791_093_621_077_859_584
    mean_all = sum(p.offset_ns for p in probes) // len(probes)
    assert mean_all != s["expected_offset_ns"]  # using every probe would be wrong


def test_sync_needs_three_probes():
    with pytest.raises(v1.StreamError, match="at least 3"):
        v1.sync_offset([v1.Probe(0, 10, 5)] * 2)


def test_host_time_interpolates_the_drift():
    # -20 ppm: over 60 s of sensor time the offset moves by -1.2 ms
    before, after = (1_000_000_000_000, 5_000_000), (1_060_000_000_000, 5_000_000 - 1_200_000)
    assert v1.host_ts_ns(1_000_000_000_000, before, after) == 1_000_005_000_000
    assert v1.host_ts_ns(1_030_000_000_000, before, after) == 1_030_000_000_000 + 4_400_000
    assert v1.host_ts_ns(1_060_000_000_000, before, after) == 1_060_003_800_000
    assert v1.host_ts_ns(7, (5, 100), (5, 900)) == 107
