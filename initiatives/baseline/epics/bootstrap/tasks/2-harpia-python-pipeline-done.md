## 2. .harpia → Python pipeline (Harpia V4)

- **Depends on:** 1
- **Contract:**
  - In: `schema/mocap.harpia` (the one root file, imports only) + `schema/Include/*.harpia` (one module per owner), as Harpia's input folder requires (USAGE §2)
  - Requires:
    - Harpia as a submodule at `third_party/harpia`, pinned to tag **`V4`** (V3's code + the Python target documented in USAGE §5.1–5.4). It's a black box: only its documented interface is used.
    - Generation per USAGE §5.1: `Docker/run.sh env HARPIA_GEN_LANG=python … python3 main.py` (`run_harpia.sh` doesn't forward the language). Input and output paths must sit under the Harpia mount, or be mounted explicitly.
  - Delivers:
    - Reproducible `make gen`.
    - The generated **`python/`** output committed under `gen/python/`, so consumers need neither Harpia nor Docker. Only `python/` is committed, not the C++ project Harpia always emits next to it (vendored third-party code we don't use; a deliberate deviation from USAGE §5.4's "commit it as a whole").
    - **`schema/schema_registry/` committed**: Harpia's frozen wire numbers (USAGE §5.4). Never deleted.
    - The wheel ships `harpia_generated` and `harpia_runtime` **as top-level packages, unmoved** (the documented import path is top-level; relocating them would break their imports). Their runtime dependencies are copied from the generated `pyproject.toml` into ours.
    - `mocap_contracts` re-exports the messages under stable names. **The re-export module is written by `make gen`**, because generated module names carry `<hash>` (md5 of the root `.harpia`) and change whenever the root changes. Consumers never see a hash or a Harpia package name.
- **Pre-work:**
  - Check that the protobuf range the generated `pyproject.toml` declares includes **4.25.x** (MediaPipe 0.10.14 needs `protobuf>=4.25.3,<5`, `mocap-studio/DEPENDENCIES.md`). If it doesn't, stop and flag it.
  - Docker available on the machine running `make gen`.
- **Out of scope:** the real messages (messages-v0/1–4). Until those land, the pipeline runs on a one-message placeholder module, which messages-v0/1 replaces. Also out: the hand-off event transport and compliance profile (messages-v0/6); Harpia's database and other transports.
- **Tests:** `make gen` on a clean tree gives no diff; the placeholder message imports through `mocap_contracts` from an installed wheel in a clean venv
