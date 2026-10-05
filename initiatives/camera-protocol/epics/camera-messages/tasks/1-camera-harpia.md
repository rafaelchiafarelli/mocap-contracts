## 1. camera.harpia (owner: mocap-camera-app)

- **Depends on:** baseline messages-v0/1, /2 (imports `session.harpia`, `capture.harpia` for `CameraControls`)
- **Contract:**
  - In: —
  - Requires: the app's control surface as it exists in the eval app (`/control` keys: width, height, fps, mode, bitrate, quality, facing) plus manual controls (exposure time, ISO, focus distance, white balance, AE/AF lock); every unit declared (ns, mm, K)
  - Delivers: `DeviceInfo` (model, serial, Android version, Camera2 hardware level, cameras with sizes, fps ranges, sensor orientation, H.264 encoders), `CameraStats` (per-second: camera and encoder fps, dropped frames, CPU, battery temperature, thermal status), `ControlRequest` (requested stream settings + requested `CameraControls`), `ControlReply` (`CameraControls` actually applied, unsupported controls listed by name — never silently ignored)
- **Pre-work:** none
- **Out of scope:** the transport (task 3)
- **Tests:** JSON round-trip; a reply with an unsupported control lists it
