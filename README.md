# mocap-contracts

The **single source of every data contract** in Mocap Studio. The other
repositories never import each other's code. Everything they exchange is
defined here: messages, file formats, the session folder layout and the
camera stream protocol.

## Where it sits in the architecture

It runs nowhere on its own. It's a library installed into every Python repo
(`pip install git+…@<tag>`), and its generated Java goes into the camera app.

```
.harpia sources ──Harpia V5 (black box, Docker)──▶ generated Python + Java ──▶ every repo
```

| Module (`schema/Include/`) | Owner (who produces the data) | What it defines |
|---|---|---|
| `common.harpia` | shared | `Flag` (Harpia has no bool) |
| `camera_control.harpia` | mocap-capture (P1), also the camera app | every camera control: capability, setting, result |
| `session.harpia` | mocap-capture (P1) | session, actors, characters, casting, camera config, calibration board |
| `capture.harpia` | mocap-capture (P2) | take, sync markers, take report, hand-off events |
| `extract.harpia` | mocap-extract (P3) | extraction index, per-camera quality |
| `adapt.harpia` | mocap-adapt (P4) | `MocapTake`, the animation data Blender reads |
| `camera.harpia` | mocap-camera-app | device info, stats, control request/reply |

It also owns:
- **the session folder layout** (`mocap_contracts.layout`): where every file
  of a take lives, the same on both PCs
- **stream protocol v1**: the binary format the camera app streams in, as a
  spec with fixtures
- **the ZeroMQ channels** for the hand-off events and the camera control

## How it's used

```python
import mocap_contracts as mc
text = mc.to_json(msg)                     # declared fields only, rules checked
cfg = mc.from_json(mc.CameraConfig, text)  # raises ContractError with the path of any problem
```

Consumers import from `mocap_contracts` only, never from Harpia's generated
module names (they carry a hash that changes with the schema). A change that
crosses repositories always starts here, and other repos pin a released tag.

## Status

In progress: the generation pipeline, JSON helpers and the first messages
(camera controls, session) are built on the `baseline` initiative branches.
They aren't on `dev` yet; they land when the initiative is done, as release
`v0.1.0`. Plan: [`initiatives/`](initiatives). Architecture:
`mocap-studio/HANDOFF.md`.
