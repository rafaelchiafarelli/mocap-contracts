## 2. capture.harpia (owner: mocap-capture/P2)

- **Depends on:** 1
- **Contract:**
  - In: —
  - Requires: imports `session.harpia`
  - Delivers: `Take` (id, type, session_id, roles, host_start/end), `SyncEvent` (kind START/END, host_ts_ns, source FIRMWARE/MANUAL), `CameraTakeReport` (role, frames, fps_measured, fps_cv, gaps, flash_frames), `TakeReport` (ok, reports[])
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** JSON round-trip
