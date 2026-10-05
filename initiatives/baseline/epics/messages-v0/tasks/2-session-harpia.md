## 2. session.harpia (owner: mocap-capture/P1)

- **Depends on:** 1; bootstrap
- **Contract:**
  - In: —
  - Requires: enum `CameraSource {UVC, STREAM}` (STREAM = a device that streams frames live to the recorder with each frame's capture time embedded, like the `camera-stream-eval` app; there is no internal-recording / `adb` import source); enum `TakeType {CALIBRATION, PERFORMANCE}`
  - Delivers: `Session` (id, date, actor), `Actor` (height, optional lengths), `CameraConfig` (role, source, device_hint — UVC only, stream_host + stream_port — STREAM only, width, height, fps, notes, preprocess, controls: the `ControlSetting`s declared for the role in `config.yaml`, any control the device offers), `PreprocessSpec` (optional crop x/y/w/h in source pixels, output width/height; declared per role, never inferred), `CalibrationBoard` (squares_x, squares_y, square_length_mm, marker_length_mm, aruco_dictionary, measured_square_length_mm — all required, no defaults)
- **Pre-work:** Read the comment restrictions of the `.harpia` lexer in Harpia's documented interface (`USAGE.md` §3).
- **Out of scope:** —
- **Tests:** JSON round-trip; required fields (a board with any field missing is rejected); a STREAM camera without host/port is rejected
