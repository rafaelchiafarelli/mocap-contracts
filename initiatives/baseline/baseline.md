# baseline — mocap-contracts

**Goal:** Single source of the data contracts between repositories: `.harpia` messages (one module per owner), the generated Python package and the session folder layout.

**Scope:** Session, capture, extraction and adaptation messages (body and hands). Face/emotion fields exist in the frame but stay empty in the baseline.

**Out of scope:** Database, ZMQ/REST, native Harpia Python output (Harpia's own backlog — see HANDOFF).

**Initiative gate:** `pip install git+...@v0.1.0` in a clean environment imports every message; JSON round-trip of every message passes.

General context, cross-repository order and open questions:
`mocap-studio/HANDOFF.md`.
