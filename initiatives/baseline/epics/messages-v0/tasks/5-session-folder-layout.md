## 5. Session folder layout

- **Depends on:** 1
- **Contract:**
  - In: data root + ids
  - Requires: stdlib only (`pathlib`)
  - Delivers: `mocap_contracts.layout` module: `session_dir`, `take_dir`, `raw_dir`, `extract_dir`, `adapt_dir`, `blender_dir`, standard file names (`take.json`, `report.json`, `index.json`)
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** deterministic paths; invalid ids rejected
