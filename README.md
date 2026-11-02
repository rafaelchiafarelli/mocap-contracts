# mocap-contracts

The **single source of every data contract** in Mocap Studio. The other
repositories never import each other's code. Everything they exchange is
defined here: messages, file formats, the session folder layout and the
camera stream protocol.

## Where it sits in the architecture

It runs nowhere on its own. It's a library installed into every Python repo
(`pip install git+…@<tag>`), and its generated Java goes into the camera app.

```
.harpia sources ──Harpia V6 (black box, Docker)──▶ generated Python + Java ──▶ every repo
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
| `bible.harpia` | mocap-writer | a film's bible: `item.json` per item (generic values with state, source, department, by), scene links, the field catalog messages, `not-props.json` |
| `change.harpia` | mocap-writer | the change log: one `Change` per line of `history/<yyyy-mm>.jsonl` |
| `script_settings.harpia` | mocap-writer | a script's settings: page setup, element styles, PDF, strings, headers, completion lists, locations, spelling words, title page layout |
| `annotation.harpia` | mocap-writer | a script's notes and scene annotations, anchored by scene, element and quote, with values checked against the annotation catalog; shot numbers per scene |
| `scene_index.harpia` | mocap-writer | a script's scene index for the pre-production agents: per numbered scene its heading parts, set, characters and prop words (bible ids when known), page and line range, text hash |
| `change_set.harpia` | mocap-writer | what a Sync to spec found changed between two scene indexes, scene by scene, matched by scene number |
| `front_matter.harpia` | mocap-writer | a film's front matter: the title page and the overview, pitch and argument pages, each with its include flag |
| `film.harpia` | mocap-writer | a film root's `film.json` (parts and their owners, id spaces), the `ids/<space>.json` counters, the record kinds |
| `workflow.harpia` | shared (per table) | the film's workflow database tables: an agent's `Proposal` for a bible value, the creator's `Review` of it, a `Request` between agents or to the creator |

It also owns:
- **the session folder layout** (`mocap_contracts.layout`): where every file
  of a take lives, the same on both PCs
- **the film root ids** (`mocap_contracts.film`): the record id form
  `<kind>-<space>-<n>` and its regex, space codes, `film.json` and
  `ids/<code>.json`
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
`schema/` (Harpia's own `HARPIA_ID/_STATUS/_ERROR/_ORIGINATOR` fields
included), on a missing `required` field at any nesting level, and on any broken
per-message rule (`mocap_contracts/rules.py`), with the path of the problem. A `required` enum
holding its `*_UNSET` zero value counts as missing, and `to_json` refuses to
write what `from_json` would refuse to read.

The film's workflow records live in one SQLite file, read and written through
`mocap_contracts.db` (rules run on every write, one program writes at a time):

```python
with mocap_contracts.db.open(film_root / "workflow.sqlite") as db:
    db.proposals.create(proposal)            # also db.reviews, db.requests
    db.proposals.read("proposal-pcp-1")      # None if there is none
```

Import from `mocap_contracts` only, never from `harpia_generated`. Its module
names carry a hash of the root `.harpia` and change with it. A change that
crosses repositories always starts here, and other repos pin a released tag
(`mocap-preprod` takes the newest one when its image is built).

## Layout

| Path | What | Edit? |
|---|---|---|
| `schema/mocap.harpia` | root file: imports only | yes |
| `schema/Include/*.harpia` | one module per owner repository | yes |
| `schema/project.harpia.yaml` | Harpia compliance profile (closed studio LAN) | rarely |
| `schema/schema_registry/` | frozen wire numbers, written by Harpia | **never delete**; commit |
| `gen/python/` | Harpia's generated Python project | no, regenerate |
| `mocap_contracts/messages.py` | re-exports every message under its declared name | no, regenerate |
| `mocap_contracts/db_tables.py` | the DAO and migration of each table message | no, regenerate |
| `mocap_contracts/db.py` | the film's workflow database (`workflow.sqlite`) | yes, with the tables' tasks |
| `mocap_contracts/rules.py` | per-message rules `required` can't express (e.g. a STREAM camera needs its host and four ports) | yes, with the message's task |
| `third_party/harpia/` | Harpia, pinned to `V6` (black box) | no |

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
- maps: `map<string,int>`; `to_json` writes their keys sorted (protobuf keeps
  no map order)
- enums: one value per line; every enum's zero value is `<ENUM>_UNSET`, and
  every value is prefixed with its enum's name

## Status

Released: see [`CHANGELOG.md`](CHANGELOG.md); the newest tag is the current
contract. Work still to do: [`initiatives/`](initiatives). Architecture:
`mocap-studio/HANDOFF.md`.
