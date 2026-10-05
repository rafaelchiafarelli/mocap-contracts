## 1. camera.harpia (owner: mocap-camera-app)

- **Depends on:** baseline messages-v0/1, /2, /3 (imports `camera_control.harpia`, `session.harpia`, `capture.harpia`)
- **Contract:**
  - In: —
  - Requires:
    - **Every** Camera2 control the device offers is exposed: the app lists them and the recorder can set any of them (Rafael, 2026-10-05), using the shared vocabulary (`ControlCapability`, `ControlSetting`, `ControlResult`) rather than a fixed list
    - stream settings (camera id, width, height, fps, bitrate, H.264 profile/I-frame interval) kept separate from camera controls
    - every unit declared
  - Delivers:
    - `DeviceInfo`: model, serial, Android version, and per camera its id, facing, Camera2 hardware level, sensor orientation, sizes, fps ranges, H.264 encoders and **every `ControlCapability`**
    - `CameraStats`, per second: camera and encoder fps, dropped frames, CPU, battery temperature, thermal status
    - `ControlRequest`: request_id, device serial, optional stream settings, `ControlSetting`s, and a flag that asks for `DeviceInfo` in the reply
    - `ControlReply`: the same request_id and device serial, a `ControlResult` per setting (unsupported or clamped ones say so, never silently), and `DeviceInfo` when asked

    The id and serial are needed because every app's reply arrives on the recorder's one shared receiver (task 3).
- **Pre-work:** none
- **Out of scope:** the transport (task 3)
- **Tests:** JSON round-trip; a reply with an unsupported and a clamped setting reports both
