## 2. capture.harpia (owner: mocap-capture/P2)

- **Depends on:** 1
- **Contract:**
  - In: —
  - Requires: imports `session.harpia`
  - Delivers:
    - `Take` (id, type, session_id, roles, host_start/end, board: `CalibrationBoard` — required on CALIBRATION takes, applied_controls per role, applied_preprocess per role)
    - `CameraControls` (exposure, gain, focus, white_balance, power_line_hz, auto_* flags — the values the camera reported back, not the requested ones)
    - `SyncEvent` (kind START/END, host_ts_ns, source MANUAL — the enum leaves room for a future hardware source)
    - `CameraTakeReport` (role, frames, fps_measured, fps_cv, gaps, first_ts_ns, last_ts_ns), `TakeReport` (ok, reports[])
    - **Hand-off events** (recorder → processing PC): `TakeClosed` (take_id, roles expected, START/END `SyncEvent`s), sent at END; `CameraFileReady` (take_id, role, kind VIDEO|TIMESTAMPS, relative path, size_bytes, sha256, frames, first/last host_ts_ns), sent once per file **after** that file has been copied to the processing PC. So the event means "arrived", not "exists on the recorder".
- **Pre-work:** none
- **Out of scope:** the transport that carries the hand-off events (task 6)
- **Tests:** JSON round-trip; a `CameraFileReady` with any field missing is rejected
