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
- `Character` already exists in `session.harpia` (capture), so the film's
  kinds are enum values, not messages.

## Touchpoints

- `tools/harpia_gen.py`, `mocap_contracts/rules.py` (rules per message).
