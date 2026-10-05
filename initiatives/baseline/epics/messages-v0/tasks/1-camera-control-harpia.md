## 1. camera_control.harpia (owner: mocap-capture/P1; the camera app produces the same messages)

- **Depends on:** bootstrap
- **Contract:**
  - In: —
  - Requires:
    - **Every control a camera offers can be listed and set from the recorder** (Rafael, 2026-10-05): exposure, luminance/brightness, auto focus, white balance, anything the device exposes. No fixed list.
    - One vocabulary for both camera types:
      - **V4L2** (UVC webcams): every control `v4l2-ctl -l` lists
      - **Camera2** (STREAM tablets): every key in `getAvailableCaptureRequestKeys()`
    - Keys keep their native names (`exposure_time_absolute`, `android.control.aeMode`), never translated.
    - Values typed per control; a string encoding only if Harpia lacks the type (checked in pre-work).
  - Delivers:
    - enums `ControlBackend {V4L2, CAMERA2}`, `ControlValueType` (int, int64, float, bool, menu/enum, …, as the backends need), `ControlStatus {APPLIED, CLAMPED, UNSUPPORTED, READ_ONLY, FAILED}`
    - `ControlCapability`: backend, key, value type, min/max/step where the device reports them, menu options by name, default, current value, read_only, unit when the backend declares one (left empty, never guessed)
    - `ControlSetting`: key + typed value, as requested
    - `ControlResult`: key, requested value, value **read back** from the device after applying, status, and a note on failure
- **Pre-work:** the field types Harpia's documented language offers (USAGE §3 shows `int`, `string`, maps, enums, composed). Float, 64-bit int and bool are needed here and in every later message. If they aren't documented, stop and flag it.
- **Out of scope:** talking to a camera (`mocap-capture` studio-setup cameras, `mocap-camera-app` control); the normalized `CameraControls` summary (task 3)
- **Tests:** JSON round-trip of each message; a capability with a menu keeps its options in order; a result's requested and read-back values can differ (`CLAMPED`)
