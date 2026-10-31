## 2. change_set.harpia (owner: mocap-writer)

- **Status:** Done (2026-10-31)

- **Depends on:** 1
- **Contract:**
  - Requires: `ChangeSet` (`bible/sync/<time>-changes.json`): `time`
    (UTC ISO-8601, as `Change`), `from_hash` (the last accepted index's
    sha256, empty on a first sync), `to_hash`, `changes`
    (`SceneChange`: `type`, `scene`, optional `old_value` / `new_value`);
    enum `SceneChangeType`: scene added, removed, moved, heading changed,
    text changed, character entered, character left, prop added, prop
    removed, set link changed
  - Rules: time as `Change`; hashes 64 hex (`from_hash` may be empty);
    scene numbers in the writer's form
  - Delivers: the messages and fixtures
- **Tests:** fixtures round-trip; invalid ones refused
