## 2. .harpia → .proto → Python pipeline

- **Depends on:** 1
- **Contract:**
  - In: `harpia/*.harpia` files
  - Requires: Harpia emits `.proto`; `protoc --python_out` generates `mocap_contracts/gen/`
  - Delivers: reproducible `make gen`; generated code **committed** (consumers don't need Harpia installed)
- **Pre-work:** **Confirm with Rafael** the Harpia command that emits only the `.proto` (stage 6) and the Harpia version to pin. Proposed decision: commit the generated code — confirm.
- **Out of scope:** Native Harpia Python output (when it exists, it becomes a new migration task)
- **Tests:** `make gen` on a clean tree produces no diff; import test of `gen`
