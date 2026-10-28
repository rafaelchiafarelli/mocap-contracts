# schema — the .harpia sources of every contract

**Role:** the one place messages are declared. Harpia turns it into
`gen/python`, `gen/java` and `mocap_contracts/messages.py` (`make gen`).

**Entry points:** `mocap.harpia` (imports only).

**Inputs → Outputs:** `.harpia` text → generated code (through
`tools/harpia_gen.py`); `schema_registry/` is written back by Harpia.

## Files

- `mocap.harpia` — root: imports every module.
- `project.harpia.yaml` — Harpia compliance profile (closed studio LAN, no PHI).
- `Include/common.harpia` — `Flag` (Harpia has no bool).
- `Include/camera_control.harpia` — camera controls (owner: mocap-capture).
- `Include/session.harpia` — session, actors, characters, cameras, board (mocap-capture P1).
- `Include/capture.harpia` — take, sync, report, hand-off events (mocap-capture P2).
- `Include/extract.harpia` — extraction index and quality (mocap-extract P3).
- `Include/adapt.harpia` — `MocapTake` (mocap-adapt P4).
- `Include/camera.harpia` — device info, stats, control request/reply (mocap-camera-app).
- `Include/film.harpia` — `Film` (`film.json`), `FilmOrigin`, `FilmPart`,
  `IdSpace`, `IdCounters` (`ids/<code>.json`, a `map<string,int>`) and the
  `RecordKind` enum (owner: mocap-writer).
- `schema_registry/mocap/*.fieldmap` — frozen wire numbers, one per message;
  never delete.

## Key facts / gotchas

- Comments take plain words only; see the README's "Writing `.harpia`".
- Changing `mocap.harpia` changes the hash in every generated module name;
  `messages.py` hides it.
- `RecordKind` is the list of record kinds: a new kind is a change here
  (`mocap_contracts/film.py:25` reads it).
- `Character` already exists in `session.harpia` (capture), so the film's
  kinds are enum values, not messages.

## Touchpoints

- `tools/harpia_gen.py`, `mocap_contracts/rules.py` (rules per message).
