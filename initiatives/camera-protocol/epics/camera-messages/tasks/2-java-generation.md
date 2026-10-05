## 2. Java generation of the contracts

- **Depends on:** 1; baseline bootstrap/2
- **Contract:**
  - In: `schema/`
  - Requires: Harpia's Java target (USAGE §5.1–5.2, `HARPIA_GEN_LANG=java`): a second generation run in `make gen`; the generated `java/` Gradle project committed under `gen/java/` (same rules as `gen/python/`: never hand-edited, `make check-gen` covers it)
  - Delivers: a Gradle project the app includes from a pinned mocap-contracts checkout (the app pins mocap-contracts by tag, just as Python consumers do)
- **Pre-work:** check that the generated Java project builds for Android at the app's `minSdk`. Harpia documents Android consumption as verified, but not at which API level. If it doesn't build there, stop and flag it.
- **Out of scope:** Java JSON helpers. The app talks ZeroMQ (task 3), not JSON files.
- **Tests:** `gradle build` of `gen/java/` in Docker; `make check-gen` covers both targets
