## 2. .harpia → Python pipeline (Harpia V3)

- **Depends on:** 1
- **Contract:**
  - In: `harpia/*.harpia` (one root file + `Include/` modules, as Harpia's input folder requires)
  - Requires: Harpia as a submodule pinned to tag **`V3`** (the first release with the Python target), used as a black box through its documented interface only (`run_harpia.sh` / Docker); `make gen` runs it and places the Python output under `mocap_contracts/gen/`
  - Delivers: reproducible `make gen`; generated Python code **committed** (consumers need neither Harpia nor Docker); `mocap_contracts` re-exports the generated messages, so consumers never import Harpia's own package names directly
- **Pre-work:**
  - Harpia V3's `USAGE.md` doesn't document how to ask for the Python target, or what the Python output looks like. That has to be documented on Harpia's side (Harpia's backlog, not this task) before this task starts. Never work it out from Harpia's source.
  - Check that the protobuf range the generated package declares includes **4.25.x** (MediaPipe 0.10.14 needs `protobuf>=4.25.3,<5`, see `mocap-studio/DEPENDENCIES.md`). If it doesn't, stop and flag it.
- **Out of scope:** the hand-off event transport and compliance profile (messages-v0/6). Harpia's database and other transports aren't used in the baseline.
- **Tests:** `make gen` on a clean tree gives no diff; every generated message imports through `mocap_contracts`
