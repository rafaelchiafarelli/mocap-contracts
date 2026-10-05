# Changelog

## v0.1.0 — 2026-10-05

First release of the Mocap Studio contracts (`baseline` initiative).

- **Generation:** `.harpia` → Python with Harpia `V5` (`make gen`, `make check-gen`). The generated code is committed, so consumers need neither Harpia nor Docker. Compliance profile: class_a, networked, no PHI.
- **Messages** (`schema/Include/`, one module per owner):
  - `common`: `Flag`
  - `camera_control`: every V4L2 / Camera2 control, as capability, setting and read-back result
  - `session`: session, actors, characters, many-to-many casting, camera config (UVC or STREAM with four ports), preprocessing, ChArUco board
  - `capture`: self-describing `Take`, `CameraControls` summary, sync events, take report with every frame gap, hand-off events `TakeClosed` / `CameraFileReady`
  - `extract`: `ExtractIndex`, alignment, point sets, `QualityReport`
  - `adapt`: `MocapTake` (header + compact frames, metres, Z up)
- **JSON:** `to_json` / `from_json`. They write declared fields only and enforce `required` (a required enum can't be `*_UNSET`) and the per-message rules in `mocap_contracts.rules`, on write and on read, with the path of any problem.
- **Layout:** `mocap_contracts.layout`, the session folder tree shared by both PCs, filename-safe ids, the timestamps CSV header.
- **Transport:** the hand-off events over Harpia ZeroMQ push/pull (`mocap_contracts.transport`, `[zmq]` extra).
