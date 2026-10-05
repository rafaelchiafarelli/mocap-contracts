## 2. Stream protocol v1 — fixtures and reference reader

- **Depends on:** 1
- **Contract:**
  - In: the spec
  - Requires: fixtures kept small (a few frames), committed under `fixtures/stream-v1/`
  - Delivers:
    - a short H.264 capture with SEI, plus its expected per-frame `(seq, sensor_ns, device_unix_ns)` CSV
    - sample clock-sync request/reply packets with their expected decoded values
    - `mocap_contracts.stream_v1`, a stdlib-only reference reader for both, which every receiver tests against
- **Pre-work:** record the fixture from a tablet running the eval app. It's a few seconds and needs no actor, but it does need a device. If that can't happen in the same session, it becomes a separate task.
- **Decisions (Claude, for Rafael's review, 2026-10-05):**
  - The real fixture is cut from the eval's existing recording (`camera-stream-eval/results/M7_WIFI-…/samples/sample.h264`), so no new device session was needed. Its slices are cut to 32 bytes: 549 bytes total, with real SPS/PPS/SEI, but not decodable.
  - Its expected timestamps come from the eval's own `sei.py` (an independent reader) and are committed.
  - A second, decodable fixture (ffmpeg, 64×64, 6 frames) carries v1 SEIs written by the reference writer, a sequence skip, and x264's own SEI to be ignored.
  - The sync packets are built per the spec with values from the M7 run, not captured off the wire.
  - Everything is reproducible with `tools/make_stream_fixtures.py`.
- **Out of scope:** decoding the video itself
- **Tests:** the reader reproduces the expected CSV and packet values; a truncated or garbled SEI is reported, never misread
