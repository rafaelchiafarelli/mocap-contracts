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
import mocap_contracts
msg = mocap_contracts.ControlMenuOption(value=1, name="Manual Mode")
text = mocap_contracts.to_json(msg)          # declared fields only, defaults included
back = mocap_contracts.from_json(mocap_contracts.ControlMenuOption, text)
```

`from_json` raises `ContractError` on invalid JSON, on any key not declared in
`schema/` (Harpia's own `ID_/STATUS_/ERROR_<hash>` and `ORIGINATOR` fields
included), on a missing `required` field at any nesting level, and on any broken
per-message rule (`mocap_contracts/rules.py`), with the path of the problem. A `required` enum
holding its `*_UNSET` zero value counts as missing, and `to_json` refuses to
write what `from_json` would refuse to read.

Import from `mocap_contracts` only, never from `harpia_generated`. Its module
names carry a hash of the root `.harpia` and change with it. A change that
crosses repositories always starts here, and other repos pin a released tag.

## Layout

| Path | What | Edit? |
|---|---|---|
| `schema/mocap.harpia` | root file: imports only | yes |
| `schema/Include/*.harpia` | one module per owner repository | yes |
| `schema/project.harpia.yaml` | Harpia compliance profile (closed studio LAN) | rarely |
| `schema/schema_registry/` | frozen wire numbers, written by Harpia | **never delete**; commit |
| `gen/python/` | Harpia's generated Python project | no, regenerate |
| `mocap_contracts/messages.py` | re-exports every message under its declared name | no, regenerate |
| `mocap_contracts/rules.py` | per-message rules `required` can't express (e.g. a STREAM camera needs its host and four ports) | yes, with the message's task |
| `third_party/harpia/` | Harpia, pinned to `V4` (V5 from messages-v0/7; same generated code) (black box) | no |

## Develop

```bash
git submodule update --init          # Harpia, only needed to regenerate
python3.12 -m venv .venv
.venv/bin/pip install -e '.[test]'
make gen                             # after editing schema/ (needs Docker)
make test                            # full suite; the regeneration check is skipped without Docker
make check-gen                       # regenerate and fail on any diff
```

Writing `.harpia` (what Harpia's lexer accepts, beyond USAGE §3):
- comments: plain words only (`:` and similar punctuation are rejected)
- scalars: `int` (int32), `int64`, `float` (32-bit), `string`; there's no
  bool (use the `Flag` enum from `common.harpia`) and no double
- enums: one value per line; every enum's zero value is `<ENUM>_UNSET`, and
  every value is prefixed with its enum's name

## Status

In progress: the generation pipeline, JSON helpers and the first messages
(camera controls, session) are built on the `baseline` initiative branches.
They aren't on `dev` yet; they land when the initiative is done, as release
`v0.1.0`. Plan: [`initiatives/`](initiatives). Architecture:
`mocap-studio/HANDOFF.md`.
