## 1. session.harpia (owner: mocap-capture/P1)

- **Depends on:** bootstrap
- **Contract:**
  - In: —
  - Requires: enum `CameraSource {UVC, FILE_IMPORT}`; enum `TakeType {CALIBRATION, PERFORMANCE}`
  - Delivers: `Session` (id, date, actor), `Actor` (height, optional lengths), `CameraConfig` (role, source, device_hint, width, height, fps, notes), `CalibrationBoard` (squares_x, squares_y, square_length_mm, marker_length_mm, aruco_dictionary, measured_square_length_mm — all required, no defaults)
- **Pre-work:** Read the comment restrictions of the `.harpia` lexer (Harpia's initiatives/README).
- **Out of scope:** —
- **Tests:** JSON round-trip; required fields (a board with any field missing is rejected)
