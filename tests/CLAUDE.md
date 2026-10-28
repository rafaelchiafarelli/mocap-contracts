# tests — the mocap-contracts test suite

**Role:** checks every contract message, its rules, its JSON form, the
generated code and the transports. "Not broken" means this suite is green
(`initiatives/README.md`).

**Entry points:** `make test` (`.venv/bin/pytest`); `make test-slow` also
runs the Gradle and Python ↔ Java tests (`MOCAP_SLOW_TESTS=1`,
`java_harness.py:18`).

**Inputs → Outputs:** the committed schema, generated code and fixtures →
pass/fail. Nothing is written into the repository.

## Files

- `samples.py` — one realistic, fully populated sample per contract message
  (`SAMPLES`); `test_jsonio.py` fails if a message has none.
- `java_harness.py` — runs Gradle on `gen/java` in Docker; the slow-test switch.
- `test_jsonio.py` — every message: a sample, round trip, declared fields
  only, `required` and `*_UNSET` enforced, on write and on read.
- `test_messages.py` — exports without the hash; every enum has UNSET as 0.
- `test_schema_parser.py` — `tools/harpia_gen.py`'s reading of the grammar.
- `test_gen_reproducible.py` — `make gen` into a temp dir equals what is
  committed; skipped without Docker or the Harpia submodule.
- `test_generated_deps.py` — `pyproject.toml` deps match the generated package.
- `test_import.py` — the package imports with its version.
- `test_session.py`, `test_capture.py`, `test_extract.py`, `test_adapt.py`,
  `test_camera_control.py`, `test_camera.py` — one per `.harpia` module, its
  rules.
- `test_layout.py` — the session folder layout and id pattern.
- `test_film.py` — film.harpia: `fixtures/film-v1/` (valid ones byte for
  byte, every invalid one with its field), the record id form against the
  layout/1 regex, map key order, film paths and owners.
- `test_transport.py` — the ZeroMQ legs (loopback).
- `test_java.py` — slow: the Java build and a Python ↔ Java exchange.
- `test_stream_v1.py` — the stream protocol v1 reader against `fixtures/stream-v1/`.

## Key facts / gotchas

- `test_gen_reproducible.py:30` compares **files only**. Harpia's Java run
  makes empty folders (`gen/java/src/test`, `generated/{db,rest,soap}`) that
  git can't keep, so comparing folders failed on every fresh clone
  (bug 1 gen-test-empty-dirs, fixed 2026-10-27 in fixes/000097).
- `test_gen_reproducible.py` runs Harpia in Docker (a few seconds once the
  image is built).

## Touchpoints

- `tools/harpia_gen.py` (`make gen`) and the generated `gen/`,
  `mocap_contracts/messages.py`.
