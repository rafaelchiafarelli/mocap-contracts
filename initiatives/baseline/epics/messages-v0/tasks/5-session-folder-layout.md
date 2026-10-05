## 5. Session folder layout

- **Depends on:** 1
- **Contract:**
  - In: data root + ids
  - Requires: stdlib only (`pathlib`); the same layout on the recorder PC and the processing PC (the hand-off copies a take folder as-is)
  - Delivers: `mocap_contracts.layout` module: `session_dir`, `take_dir`, `raw_dir`, `prep_dir` (recorder preprocessing output), `extract_dir`, `adapt_dir`, `blender_dir`, standard file names (`take.json`, `report.json`, `manifest.json`, `index.json`)
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** deterministic paths; invalid ids rejected
