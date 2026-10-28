## 2. Release v0.4.0

- **Status:** Done (2026-10-27)

- **Depends on:** 1
- **Contract:**
  - In: —
  - Requires: CHANGELOG entry; full suite including `make test-slow` (the
    Java build gains the new messages)
  - Delivers: version 0.4.0 and tag `v0.4.0` on `dev`. New messages only,
    nothing existing changes, so consumers of `v0.3.0` can move up freely.
    `mocap-writer` pins it for layout/1.
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** install from the tag in a clean venv
