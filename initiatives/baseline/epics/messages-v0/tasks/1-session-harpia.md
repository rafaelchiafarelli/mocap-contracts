## 1. session.harpia (owner: mocap-capture/P1)

- **Depends on:** bootstrap
- **Contract:**
  - In: —
  - Requires: enum `CameraSource {UVC, FILE_IMPORT}`; enum `TakeType {CALIBRATION, PERFORMANCE}`
  - Delivers: `Session` (id, date, actor), `Actor` (height, optional lengths), `CameraConfig` (role, source, device_hint, width, height, fps, notes)
- **Pre-work:** Read the comment restrictions of the `.harpia` lexer (Harpia's initiatives/README).
- **Out of scope:** —
- **Tests:** JSON round-trip; required fields
