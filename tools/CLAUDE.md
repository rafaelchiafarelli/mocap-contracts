# tools — generation and fixture scripts

**Role:** scripts a maintainer runs; nothing imports them.

**Entry points:** `make gen` (`harpia_gen.py`); the two fixture builders.

**Inputs → Outputs:** `schema/` → generated code; known values → `fixtures/`.

## Files

- `harpia_gen.py` — runs Harpia in Docker for Python and Java
  (`run_harpia`, `harpia_gen.py:50`), copies `gen/`, `schema_registry/`, and
  writes `mocap_contracts/messages.py` and `zmq_endpoints.py`. `--into DIR`
  writes elsewhere (the reproducibility test).
- `make_stream_fixtures.py` — builds `fixtures/stream-v1/` (needs ffmpeg and
  an eval recording).
- `make_film_fixtures.py` — builds `fixtures/film-v1/` from plain dicts
  (`FILM`, `IDS`, `INVALID`, `make_film_fixtures.py:26-64`), stdlib only so the
  fixtures don't come from the code they test.

## Key facts / gotchas

- `harpia_gen.py` reads declared and required fields from `schema/` itself
  (`schema_fields`, `harpia_gen.py:82`): proto3 loses `required`.
- The fixture builders are run once and their outputs committed.

## Touchpoints

- `schema/`, `fixtures/`, `tests/test_gen_reproducible.py`.
