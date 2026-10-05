## 2. Java generation of the contracts

- **Depends on:** 1; baseline bootstrap/2
- **Contract:**
  - In: `schema/`
  - Requires: Harpia's Java target (USAGE §5.1–5.2, `HARPIA_GEN_LANG=java`): a second generation run in `make gen`; the generated `java/` Gradle project committed under `gen/java/` (same rules as `gen/python/`: never hand-edited, `make check-gen` covers it)
  - Delivers: a Gradle project the app includes from a pinned mocap-contracts checkout (the app pins mocap-contracts by tag, just as Python consumers do)
- **Pre-work:** check that the generated Java project builds for Android at the app's `minSdk`. Harpia documents Android consumption as verified, but not at which API level. If it doesn't build there, stop and flag it.
- **Decisions (Claude, for Rafael's review, 2026-10-05):**
  - **The camera app targets `minSdk 24`** (Android 7.0), not the eval app's 21. Harpia documents its Java output as verified on Android in exactly that configuration (`HarpiaTest/app_example/android_consumer`: minSdk 24, full protobuf-java runtime, multidex), and the tablet measured so far (Multilaser M7) runs Android 13 / SDK 33.
  - The app consumes the subset Harpia documents for Android: message classes, JSON and the JeroMQ ZeroMQ client. The DB/REST/SOAP/server parts are never used on the device.
  - `make gen` runs Harpia twice (Python, then Java) and refuses if the two runs disagree on `schema_registry`.
  - The Java build check is a **slow test** (`make test-slow`, about 20 s) in the official `gradle:8.7-jdk17` image, pinned by digest. It isn't Harpia's image, so it doesn't rely on Harpia's internals.
- **Out of scope:** Java JSON helpers. The app talks ZeroMQ (task 3), not JSON files.
- **Tests:** `gradle build` of `gen/java/` in Docker; `make check-gen` covers both targets
