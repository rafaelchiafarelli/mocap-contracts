## 5. Session folder layout

- **Depends on:** 1
- **Contract:**
  - In: data root + ids
  - Requires: stdlib only (`pathlib`); the same layout on the recorder PC and the processing PC (hand-off copies files to the same relative paths)
  - Delivers: `mocap_contracts.layout` module: `session_dir`, `take_dir`, `raw_dir`, `prep_dir` (recorder preprocessing output), `extract_dir`, `adapt_dir`, `blender_dir`; standard file names (`take.json`, `report.json`, `index.json`); the hand-off sidecars: `closed.json` (the `TakeClosed` event, in the take folder) and `<file>.ready.json` (the `CameraFileReady` event, next to the file it describes)
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** deterministic paths; invalid ids rejected; sidecar path of a file is deterministic
