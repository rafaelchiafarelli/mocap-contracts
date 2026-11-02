"""Build fixtures/stream-v1/ (stream protocol v1 test fixtures).

Run once; the outputs are committed. Needs ffmpeg and a recording from the
evaluation app (mocap-studio/camera-stream-eval/results/*/samples/sample.h264).

    python3 tools/make_stream_fixtures.py <sample.h264>

Writes:
- tablet-excerpt.h264: a real recording from a tablet (Multilaser M7, eval
  app). SPS, PPS and the first frames with their real timestamp SEIs, but each
  slice is cut to its first 32 bytes, which keeps the file tiny. Not decodable.
  Its expected timestamps (tablet-excerpt.timestamps.csv) are not written
  here: they were produced once by the eval's own scripts/sei.py, an
  independent reader, and committed:
      python3 camera-stream-eval/scripts/sei.py tablet-excerpt.h264 out.csv
  (column tablet_unix_ns renamed device_unix_ns).
- decodable.h264 + decodable.timestamps.csv: a small stream ffmpeg can decode
  (64x64, 6 frames), with a v1 SEI added before every frame by the reference
  writer, known values, and a skip (seq 4 -> 6). x264's own SEI (another UUID)
  stays in, so readers must ignore it.
- garbled.h264: v1 SEIs that must be reported, never read (wrong payload
  size, truncated payload) around one good one.
- sync.json: clock-sync request/reply bytes with decoded values, and a set of
  probes with the offset the timing model gives.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from mocap_contracts import stream_v1 as v1  # noqa: E402

OUT = ROOT / "fixtures" / "stream-v1"
SC = b"\x00\x00\x00\x01"


def tablet_excerpt(sample: Path, frames: int = 6) -> bytes:
    out, seen = bytearray(), 0
    for nal_type, nal in v1.nal_units(sample.read_bytes()):
        if nal_type in (v1.NAL_SPS, v1.NAL_PPS, v1.NAL_SEI):
            if nal_type == v1.NAL_SEI:
                seen += 1
                if seen > frames:
                    break
            out += SC + nal
        elif nal_type in (v1.NAL_IDR, v1.NAL_SLICE):
            out += SC + nal[:32]
    return bytes(out)


def decodable() -> tuple[bytes, list[tuple[int, int, int, int]]]:
    with tempfile.TemporaryDirectory() as d:
        raw = Path(d) / "x.h264"
        subprocess.run(
            ["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc=size=64x64:rate=30",
             "-frames:v", "6", "-c:v", "libx264", "-g", "6", "-bf", "0", "-pix_fmt", "yuv420p",
             "-f", "h264", str(raw)],
            check=True,
        )
        data = raw.read_bytes()
    t0, period = 1_759_700_000_000_000_000 - 1_791_093_621_077_859_584 % 10**9, 33_333_333
    seqs = [1, 2, 3, 4, 6, 7]  # a skip after 4: the camera dropped frame 5
    out, rows, i = bytearray(), [], 0
    for nal_type, nal in v1.nal_units(data):
        if nal_type in (v1.NAL_IDR, v1.NAL_SLICE):
            seq = seqs[i]
            sensor = 3_512_345_678_901 + (seq - 1) * period
            unix = t0 + (seq - 1) * period
            out += v1.build_timestamp_sei(seq, sensor, unix)
            rows.append((i, seq, sensor, unix))
            i += 1
        out += SC + nal
    assert i == len(seqs), f"expected {len(seqs)} slices, got {i}"
    return bytes(out), rows


def garbled() -> bytes:
    good = v1.build_timestamp_sei(10, 5_000_000_000, 1_700_000_000_000_000_000)
    rbsp = bytes([5, 39]) + v1.UUID + b"\x01" * 23 + b"\x80"  # payloadSize 39
    wrong_size = SC + bytes([6]) + v1.escape(rbsp)
    rbsp = bytes([5, 40]) + v1.UUID + b"\x02" * 10  # cut short
    truncated = SC + bytes([6]) + v1.escape(rbsp)
    slice_ = SC + bytes([0x41]) + b"\x9a" * 8
    return wrong_size + slice_ + good + slice_ + truncated + slice_


def sync() -> dict:
    token, sensor, unix = 7, 35_084_754_348_416, 1_791_128_653_834_000_000
    reply = v1.sync_reply(token, sensor, unix)
    t, offset = 1_791_128_705_832_208_000, 1_791_093_621_077_859_584
    probes = []
    for i, rtt_us in enumerate([6570, 2351, 2400, 9100, 2390, 7000, 6600, 2500, 12000, 3000,
                                6500, 6700, 2600, 6800, 8000, 6900, 2700, 7100, 6650, 2800,
                                6550, 2450, 7300, 6450, 2550, 6750, 6850, 2650, 6950, 7050]):
        t_send = t + i * 10_000_000
        rtt = rtt_us * 1000
        # the reply is stamped at an asymmetric point for slow probes, as on real Wi-Fi
        skew = 0 if rtt_us < 3000 else rtt // 5
        sensor_i = t_send + rtt // 2 + skew - offset
        probes.append({"t_send_ns": t_send, "t_recv_ns": t_send + rtt, "sensor_ns": sensor_i})
    expected = v1.sync_offset([v1.Probe(**p) for p in probes])
    return {
        "request": {"hex": v1.sync_request(token).hex(), "token": token},
        "reply": {"hex": reply.hex(), "token": token, "sensor_ns": sensor, "device_unix_ns": unix},
        "probes": probes,
        "expected_offset_ns": expected,
        "note": "slow probes carry an asymmetric delay; the fastest 10% (3 of 30) recover the true offset "
                f"{offset} exactly",
    }


def main() -> None:
    sample = Path(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "tablet-excerpt.h264").write_bytes(tablet_excerpt(sample))
    data, rows = decodable()
    (OUT / "decodable.h264").write_bytes(data)
    with open(OUT / "decodable.timestamps.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["frame", "seq", "sensor_ns", "device_unix_ns"])
        w.writerows(rows)
    (OUT / "garbled.h264").write_bytes(garbled())
    (OUT / "sync.json").write_text(json.dumps(sync(), indent=2) + "\n")
    for p in sorted(OUT.iterdir()):
        print(f"{p.name}: {p.stat().st_size} bytes")


if __name__ == "__main__":
    main()
