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
  `RecordKind` enum (owner: mocap-writer); `request` added for the
  workflow records, and the part `workflow` (`workflow.sqlite`, owner
  `shared`, per-table ownership in the comments).
- `Include/bible.harpia` — the film bible (owner: mocap-writer):
  `BibleItem` (`item.json`), `BibleValue`, `BibleLink`, `NotProps`, the
  catalog messages `BibleCatalog`, `CatalogMap`, `CatalogGroup`,
  `CatalogField`, enums `BibleMap`, `FieldType`, `ValueState`.
- `Include/change.harpia` — the change log (owner: mocap-writer): `Change`
  (one line of `history/<yyyy-mm>.jsonl`: time, by, path, record, op,
  before, after) and `ChangeOp`.
- `Include/script_settings.harpia` — a script's settings (owner:
  mocap-writer): `ScriptSettings` (`settings/script-settings.json`) with
  `PageSettings`, `ElementStyle` / `TextStyle`, `PdfSettings` /
  `PdfFont`, `ScriptStrings`, `HeaderSettings` / `HeaderLine`,
  `AutoCompletionList`, `LocationGroup`, `TitlePages` / `TitlePageLayout`
  / `TitleString`; enums `ScriptElement`, `TextAlign`, `TitleFont`.
- `Include/annotation.harpia` — a script's annotations (owner:
  mocap-writer): `Annotation` (`annotations/<id>.json`),
  `AnnotationAnchor`, `ShotCounters` (`annotations/shot-counters.json`),
  the catalog messages `AnnotationCatalog` / `CatalogKind` (reusing
  `CatalogGroup`), enum `AnnotationKind`; values are `BibleValue`s.
- `Include/scene_index.harpia` — the scene index (owner: mocap-writer):
  `SceneIndex` (`bible/scene-index.json`: the script's hash and one
  `SceneEntry` per numbered scene: number, order, heading parts, set id,
  `SceneCharacter`s with `speaks`, `SceneProp`s, page and line range, the
  scene text's hash), read by the pre-production agents.
- `Include/change_set.harpia` — a Sync to spec's change set (owner:
  mocap-writer): `ChangeSet` (`bible/sync/<time>-changes.json`: time, the
  two index hashes, the changes), `SceneChange` (type, scene, old and new
  value), enum `SceneChangeType`.
- `Include/front_matter.harpia` — a film's front matter (owner:
  mocap-writer): `FrontMatter` (`settings/front-matter.json`, part
  `front-matter`) with `TitlePage` (title, subtitle, episode, author,
  co-authors, e-mail), `Overview` (include and what it computes: cast,
  sets, acts), `Pitch` (include, pitch, logline, target audience),
  `Argument` (include, text).
- `Include/workflow.harpia` — the film's workflow records (owner: shared;
  ownership per table): `autokey` table messages `Proposal` (`proposal_table`: an
  agent's `BibleValue` for an existing bible item, its time and the change
  set it answered), `Review` (`review_table`: the creator's outcome of one
  proposal, unique by `proposal`), `Request` (`request_table`: from an
  agent to an agent or the creator, items, scenes, what, status, answer);
  enums `ReviewOutcome`, `RequestStatus`. Harpia generates their SQLite
  DAOs, migrations and dbio in `gen/python/harpia_generated/{db,migrate,dbio}/`.
- `schema_registry/mocap/*.fieldmap` — frozen wire numbers, one per message;
  never delete.

## Key facts / gotchas

- Comments take plain words only; see the README's "Writing `.harpia`".
- Changing `mocap.harpia` changes the hash in every generated module name;
  `messages.py` hides it.
- `RecordKind` is the list of record kinds: a new kind is a change here
  (`mocap_contracts/film.py:25` reads it).
- `map` is a Harpia keyword: `CatalogMap`'s field is `bible_map`.
- `BibleValue.number` is decimal text: Harpia's `float` is 32-bit and would
  change `1.85` on a round trip.
- A message with a trailing table name (`} proposal_table;`) is a table:
  Harpia adds the DAOs, a `read_by_<field>` per `unique` field, and the Java
  run then also fills `generated/{db,rest,soap}`. `autokey` lets the database
  assign its key, `HARPIA_ID`.
- Since Harpia V6 the hidden fields are `HARPIA_ID/_STATUS/_ERROR/_ORIGINATOR`
  on their old wire numbers, so a changed root renames generated files but
  no column: film databases keep opening.
- `Character` already exists in `session.harpia` (capture), so the film's
  kinds are enum values, not messages.

## Touchpoints

- `tools/harpia_gen.py`, `mocap_contracts/rules.py` (rules per message).
