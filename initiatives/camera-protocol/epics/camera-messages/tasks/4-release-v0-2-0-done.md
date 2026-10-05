## 4. Release v0.2.0

- **Depends on:** 1–3; stream-protocol
- **Contract:**
  - In: —
  - Requires: CHANGELOG entry; full suite including `make test-slow`
  - Delivers: version 0.2.0 and tag `v0.2.0`. The camera app and mocap-capture's STREAM source pin it.
- **Decisions (Claude, for Rafael's review, 2026-10-05):** added at the end of the initiative, because nothing else gave the camera app a version to pin. It mirrors baseline messages-v0/8.
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** install from the tag in a clean venv
