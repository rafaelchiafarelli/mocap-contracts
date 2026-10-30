# tools — generation and fixture scripts

**Role:** scripts a maintainer runs; nothing imports them.

**Entry points:** `make gen` (`harpia_gen.py`); the four fixture builders.

**Inputs → Outputs:** `schema/` → generated code; known values → `fixtures/`.

## Files

- `harpia_gen.py` — runs Harpia in Docker for Python and Java
  (`run_harpia`, `harpia_gen.py:50`), copies `gen/`, `schema_registry/`, and
  writes `mocap_contracts/messages.py` and `zmq_endpoints.py`. `--into DIR`
  writes elsewhere (the reproducibility test).
- `make_stream_fixtures.py` — builds `fixtures/stream-v1/` (needs ffmpeg and
  an eval recording).
- `make_film_fixtures.py` — builds `fixtures/film-v1/` from plain dicts
  (`FILM`, `IDS`, `INVALID`, `make_film_fixtures.py:26-121`), stdlib only so the
  fixtures don't come from the code they test.
- `make_bible_fixtures.py` — builds `fixtures/bible-v1/` the same way
  (`ITEMS`, `INVALID`, `make_bible_fixtures.py:53-138`).
- `make_script_fixtures.py` — builds `fixtures/script-v1/`: `DEFAULTS`,
  the writer's defaults as of 2026-10-30, in declared order, and
  `INVALID`.

## Key facts / gotchas

- `harpia_gen.py` reads declared and required fields from `schema/` itself
  (`schema_fields`, `harpia_gen.py:82`): proto3 loses `required`.
- The fixture builders are run once and their outputs committed.

## Touchpoints

- `schema/`, `fixtures/`, `tests/test_gen_reproducible.py`.
