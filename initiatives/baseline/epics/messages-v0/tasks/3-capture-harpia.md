## 3. capture.harpia (owner: mocap-capture/P2)

- **Depends on:** 2
- **Contract:**
  - In: —
  - Requires: imports `session.harpia` and `camera_control.harpia`
  - Delivers:
    - `Take` (id, type, session_id, roles, host_start/end, board: `CalibrationBoard` — required on CALIBRATION takes, per role: `control_results` (every `ControlResult` from applying the role's controls, i.e. the full native record) and `applied_controls` (the normalized `CameraControls` summary), applied_preprocess per role)
    - `CameraControls`: a normalized summary for comparing cameras in the study (exposure in ns, gain/ISO, focus, white balance in K, power_line_hz, auto_* flags), filled from the read-back `ControlResult`s where a native control maps onto it, empty where none does. Never the requested values.
    - `SyncEvent` (kind START/END, host_ts_ns, source MANUAL — the enum leaves room for a future hardware source)
    - `CameraTakeReport` (role, frames, fps_measured, fps_cv, gaps, first_ts_ns, last_ts_ns), `TakeReport` (ok, reports[])
    - **Hand-off events** (recorder → processing PC): `TakeClosed` (take_id, roles expected, START/END `SyncEvent`s), sent at END; `CameraFileReady` (take_id, role, kind VIDEO|TIMESTAMPS, relative path, size_bytes, sha256, frames, first/last host_ts_ns), sent once per file **after** that file has been copied to the processing PC. So the event means "arrived", not "exists on the recorder".
- **Pre-work:** none
- **Out of scope:** the transport that carries the hand-off events (task 6)
- **Tests:** JSON round-trip; a `CameraFileReady` with any field missing is rejected
