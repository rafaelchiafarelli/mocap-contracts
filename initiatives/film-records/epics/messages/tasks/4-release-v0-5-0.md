## 4. Release v0.5.0

- **Depends on:** 1–3
- **Contract:**
  - Requires: CHANGELOG entry; the full suite including `make test-slow`
  - Delivers: version 0.5.0 and tag `v0.5.0` on `dev`. **Breaking for
    film.json only:** the five rules refuse files `v0.4.0` accepted (no
    film was written with `v0.4.0`). `mocap-writer` pins it.
- **Tests:** install from the tag in a clean venv
