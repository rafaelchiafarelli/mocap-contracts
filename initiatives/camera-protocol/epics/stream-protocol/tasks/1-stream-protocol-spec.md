## 1. Stream protocol v1 — spec

- **Depends on:** —
- **Contract:**
  - In: what the eval app does today (`mocap-studio/camera-stream-eval`, README "How it works"): `TimestampSei` (UUID `MOCAPSTUDIO-TS01`, frame seq, sensor ns, device Unix ns), `TimeSyncServer` (UDP NTP-style on the sensor clock), `/h264.raw`, the multipart `/stream`
  - Requires: every byte layout explicit (field order, sizes, endianness, units, clock each timestamp is on); ports declared; a version field or rule, so a v2 can coexist
  - Delivers: `docs/stream-protocol-v1.md`: video transport, SEI payload, clock sync request and reply, the timing model (`capture time on recorder clock = sensor_ns + offset`, offset and drift from syncs before and after a take), and what a receiver must do on a lost or garbled frame
- **Pre-work:** none. Video transport decided (Rafael, 2026-10-05): raw Annex-B H.264 over HTTP (`/h264.raw`), with the timestamps only in the SEI, and the multipart `/stream` dropped. One format means one parser on the recorder.
- **Out of scope:** control/info/status, including every camera control (camera-messages, over ZeroMQ); HEVC
- **Decisions (Claude, for Rafael's review, 2026-10-05):**
  - v1 is exactly what the eval app does today (byte layouts read from its source), so every device measured with `camera-stream-eval` was measured on the real protocol
  - the recorder's host clock is Unix ns (`CLOCK_REALTIME`), the clock UVC cameras get from FFmpeg's wall-clock timestamps, so both camera types share one clock
  - `device_unix_ns` is informational only and never used for alignment (the device's wall clock is synced to nothing)
  - the version lives in the SEI UUID (`…-TS01`); receivers ignore other UUIDs
- **Tests:** none of its own (a document); task 2's fixtures check it
