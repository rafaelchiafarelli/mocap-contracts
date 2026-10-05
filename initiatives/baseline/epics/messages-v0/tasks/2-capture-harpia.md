## 2. capture.harpia (owner: mocap-capture/P2)

- **Depends on:** 1
- **Contract:**
  - In: —
  - Requires: imports `session.harpia`
  - Delivers: `Take` (id, type, session_id, roles, host_start/end, board: `CalibrationBoard` — required on CALIBRATION takes, applied_controls per role, applied_preprocess per role), `CameraControls` (exposure, gain, focus, white_balance, power_line_hz, auto_* flags — the values the camera reported back, not the requested ones), `SyncEvent` (kind START/END, host_ts_ns, source MANUAL — the enum leaves room for a future hardware source), `CameraTakeReport` (role, frames, fps_measured, fps_cv, gaps, first_ts_ns, last_ts_ns), `TakeReport` (ok, reports[]), `TakeManifest` (take_id, files[]: relative path, size_bytes, sha256 — written by the recorder last, after preprocessing; its presence means the take is complete and ready to hand off)
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** JSON round-trip
