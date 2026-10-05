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
- **Out of scope:** decoding the video itself
- **Tests:** the reader reproduces the expected CSV and packet values; a truncated or garbled SEI is reported, never misread
