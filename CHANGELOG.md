# Changelog

## v0.3.0 — 2026-10-06

- **`ControlRequest.reply_endpoint`** (required, `tcp://<host>:<port>`): where the recorder's `ControlReply` receiver listens. The camera app sends each reply there, so a tablet needs no recorder address of its own and moving the recorder PC changes nothing on the tablets. Nothing declared where the reply went before (`CameraConfig` has the app's `control_port` and `stats_port` only). New wire number 10; existing numbers unchanged. **Breaking:** a request without it is rejected by the rules, so recorder and app both move to `v0.3.0`.

## v0.2.1 — 2026-10-05

- The Harpia submodule is cloned over HTTPS instead of SSH. `pip install git+…@<tag>` clones submodules, and the SSH URL made installs fail on any machine without the maintainer's key (Docker builds included). No contract changes: pin `v0.2.1` instead of `v0.1.0`/`v0.2.0`.

## v0.2.0 — 2026-10-05

The contract between the STREAM camera app and the recorder (`camera-protocol` initiative).

- **Stream protocol v1** (`docs/stream-protocol-v1.md`): raw Annex-B H.264 over HTTP, a timestamp SEI on every frame, UDP clock sync, and the timing model. `mocap_contracts.stream_v1` is the reference reader and writer (stdlib only). Fixtures in `fixtures/stream-v1/`: a real tablet excerpt (checked against the eval's own `sei.py`), a decodable stream, garbled SEIs, sync packets.
- **`camera.harpia`**: `DeviceInfo` (every camera with every `ControlCapability`), `CameraStats`, `StreamSettings`, `ControlRequest` / `ControlReply`, with rules.
- **Java**: `make gen` also generates `gen/java/`, the Gradle project the camera app builds against (Android `minSdk 24`).
- **ZeroMQ**: `ControlRequest` / `ControlReply` (push/pull) and `CameraStats` (pub/sub) through `mocap_contracts.transport`, interoperating with Java. `make test-slow` runs a Java camera peer against the Python recorder side.

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
