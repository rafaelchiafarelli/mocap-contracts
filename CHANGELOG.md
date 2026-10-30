# Changelog

## v0.6.0 — 2026-10-30

The records that belong to a script (`script-records` initiative), for `mocap-writer` fountain-native settings/1 and notes/1.

- **`script_settings.harpia`** (owner: `mocap-writer`): `ScriptSettings` is `settings/script-settings.json`: page setup, one `ElementStyle` per element (screen and export `TextStyle`), PDF flags and fonts, the printed strings, headers, completion lists, locations, the script's spelling words, and the title pages' layout with the Fountain title block it was saved with. Every field written; Trelby's limits refused, never clamped. Fixtures `fixtures/script-v1/`.
- **`annotation.harpia`** (owner: `mocap-writer`): `Annotation` is `annotations/<id>.json`: kind (note, character / prop / set / sound / general direction, special effect, transition, shot), anchor (scene number, element index, quoted text and its occurrence), text, author, a shot's number in its scene, and `BibleValue`s checked against the annotation catalog (`catalog/annotation-v1.json`, 66 fields). `ShotCounters` is `annotations/shot-counters.json`. `mocap_contracts.annotation`. Fixtures `fixtures/annotation-v1/`.
- **`to_json` writes fields in their declared order.** Before, protobuf put fields holding their default value last, so the order depended on the values. Files written by `v0.5.0` read the same; only their key order differs when written again.
- `tests/test_import.py` was left at `0.4.0` by the `v0.5.0` release, so that tag's suite has one failing test (the version check only); fixed here.

New messages only: nothing in `v0.5.0` changes meaning.

## v0.5.0 — 2026-10-28

The film's records besides its index (`film-records` initiative), for `mocap-writer` file-format layout/1 and layout/5 and film-bible contract/2.

- **Film rules** (decided 2026-10-28): `film.json` holds a `script` part and the `w` space owned by `writer`; part names are `script`, `settings`, `bible`, `annotations`, `history` or `proposals-<code>` with a listed space; owners are `writer` or kebab-case; every non-writer part owner has a space; paths are Windows-safe (no `<>:"|?*` or control characters, no segment ending in a dot or space, no reserved device names). `mocap_contracts.film` gains `PART_NAMES`, `OWNER`, `path_problem`, `check_path`, `history_file`. **Breaking for `film.json` only:** these refuse files `v0.4.0` accepted; no film was written with `v0.4.0`.
- **`bible.harpia`** (owner: `mocap-writer`): `BibleItem` (`item.json`) with generic `BibleValue`s (field, scene, text or decimal number + unit, note, state, source, department, by, revisit) and `BibleLink`s (scene, and for wardrobe the character); `NotProps`; the catalog messages. The approved field catalog ships as `mocap_contracts/catalog/bible-v1.json` (180 fields over sets, characters, props, wardrobe) and the rules check every item against it. `mocap_contracts.bible`: maps and their folders, `catalog()`, `fields(map)`, `map_of`, `slug`, the scene-number form.
- **`change.harpia`** (owner: `mocap-writer`): `Change`, one line of `history/<yyyy-mm>.jsonl` (time, by, path, record, op, before, after).
- Fixtures `fixtures/bible-v1/` and new invalid `fixtures/film-v1/` cases.

## v0.4.0 — 2026-10-27

The film root's index and record ids (`film-root` initiative), for `mocap-writer` file-format/layout/1.

- **`film.harpia`** (owner: `mocap-writer`): `Film` is `film.json` (`format_version` 1, `origin` program and version, `parts` with name, path and owner, `spaces` with code and owner); `IdCounters` is `ids/<code>.json` (`next`, one counter per record kind); `RecordKind` lists the kinds (`set`, `character`, `prop`, `wardrobe`, `annotation`, `proposal`). Rules: part paths relative to the film root with `/`, never leaving it, never `film.json` or under `ids/`, never inside another part's path; part names and space codes unique; space codes 1–8 lower-case letters or digits starting with a letter; counters ≥ 1.
- **`mocap_contracts.film`**: the record id `<kind>-<space>-<n>` (`RECORD_ID`, `record_id`, `check_record_id`), space codes, `film.json` and `ids_file(code)`.
- **Fixtures** `fixtures/film-v1/`: a valid film root index and counters; invalid files with the error each must raise (`invalid/expected.json`).
- `to_json` writes map keys sorted (no earlier message had a map).
- The reproducibility test compares files only, so it passes on a fresh clone (fixes/000097).

New messages only: nothing in `v0.3.0` changes.

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
