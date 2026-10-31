## 1. scene_index.harpia (owner: mocap-writer)

- **Status:** Done (2026-10-31)

- **Depends on:** `v0.6.0`
- **Contract:**
  - Requires: `SceneIndex` (`bible/scene-index.json`): `script_hash`
    (sha256 hex of the script's text) and one `SceneEntry` per numbered
    scene, in script order: `scene` (number), `order` (from 1),
    `int_ext`, `location`, `time_of_day` (as written), optional `set_id`,
    `characters` (`SceneCharacter`: `name` as written, optional `id`,
    `speaks` Flag), `props` (`SceneProp`: `word` as written, optional
    `id`), `first_page` / `last_page`, `first_line` / `last_line`,
    `text_hash` (sha256 hex of the scene's text)
  - Rules: scene numbers in the writer's form, each once; order 1..n in
    sequence; ids record ids of the right kind (`set-`, `character-`,
    `prop-`); hashes 64 lower-case hex; pages and lines from 1, last ≥
    first; names and words not empty
  - Delivers: the messages, `fixtures/preprod-v1/scene-index.json`,
    invalid fixtures with `invalid/expected.json`
- **Tests:** fixtures round-trip byte for byte; each invalid one refused
  naming its field
