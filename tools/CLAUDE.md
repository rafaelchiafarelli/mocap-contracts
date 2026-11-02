# tools — generation and fixture scripts

**Role:** scripts a maintainer runs; nothing imports them.

**Entry points:** `make gen` (`harpia_gen.py`); the `make_*_fixtures.py` builders.

**Inputs → Outputs:** `schema/` → generated code; known values → `fixtures/`.

## Files

- `harpia_gen.py` — runs Harpia in Docker for Python and Java
  (`run_harpia`, `harpia_gen.py:54`), copies `gen/`, `schema_registry/`, and
  writes `mocap_contracts/messages.py`, `zmq_endpoints.py` and
  `db_tables.py`. `--into DIR`
  writes elsewhere (the reproducibility test).
- `make_stream_fixtures.py` — builds `fixtures/stream-v1/` (needs ffmpeg and
  an eval recording).
- `make_film_fixtures.py` — builds `fixtures/film-v1/` from plain dicts
  (`FILM`, `IDS`, `INVALID`, `make_film_fixtures.py:26-128`), stdlib only so the
  fixtures don't come from the code they test.
- `make_bible_fixtures.py` — builds `fixtures/bible-v1/` the same way
  (`ITEMS`, `INVALID`, `make_bible_fixtures.py:52-139`).
- `make_annotation_fixtures.py` — builds `fixtures/annotation-v1/`
  (`ANNOTATIONS`, `COUNTERS`, `INVALID`).
- `make_preprod_fixtures.py` — builds `fixtures/preprod-v1/`: `INDEX`
  (hashes computed from the neutral `SCENES`), `CHANGES`, `FRONT` and `INVALID`.
- `make_script_fixtures.py` — builds `fixtures/script-v1/`: `DEFAULTS`,
  the writer's defaults as of 2026-10-30, in declared order, and
  `INVALID`.
- `make_workflow_fixtures.py` — builds `fixtures/workflow-v1/`: `PROPOSAL`,
  `REVIEW`, `REQUEST` (one record of each table as JSON) and `INVALID`.

## Key facts / gotchas

- `harpia_gen.py` reads declared and required fields from `schema/` itself
  (`schema_fields`, `harpia_gen.py:86`): proto3 loses `required`.
- The fixture builders are run once and their outputs committed.

## Touchpoints

- `schema/`, `fixtures/`, `tests/test_gen_reproducible.py`.
