## 6. Session folder layout

- **Depends on:** 2
- **Contract:**
  - In: data root + ids
  - Requires: stdlib only (`pathlib`); the same layout on the recorder PC and the processing PC (hand-off copies files to the same relative paths)
  - Delivers: `mocap_contracts.layout`:
    ```
    <root>/<session>/session.json
    <root>/<session>/calibration/calibration.toml
    <root>/<session>/takes/<take>/take.json, report.json, closed.json
                                 raw/<role>.mkv, raw/<role>.timestamps.csv
                                 prep/<role>.mkv
                                 extract/index.json, quality.json, quality.md, synced/<role>.mp4
                                 adapt/mocap_take.json
                                 blender/
    <file>.ready.json            next to the file it announces
    ```
    - functions for every folder and file above, plus `ready_sidecar(path)`
    - `TIMESTAMPS_COLUMNS = ("frame", "host_ts_ns")`, the header of every timestamps CSV
    - `check_id(kind, value)`: session, take and role ids match `[A-Za-z0-9][A-Za-z0-9_-]{0,63}`
- **Decisions (Claude, for Rafael's review, 2026-10-05):**
  - takes live under `takes/` so session-level folders (calibration) can't collide with a take id
  - a single id pattern that is safe as a folder or file name on Linux and Windows
  - the message rules apply the same pattern to Session.id, Take.id/session_id and CameraConfig.role, so an id that can't be a folder never gets into a file
  - one `adapt/mocap_take.json` per take for now (one performer per take in the baseline); its naming for several performers is decided when that happens
- **Pre-work:** none
- **Out of scope:** creating folders or moving files (each repo does its own I/O)
- **Tests:** deterministic paths; invalid ids rejected; sidecar path of a file is deterministic
