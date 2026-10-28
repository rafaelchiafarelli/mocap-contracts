# fixtures — committed test data other repositories can reuse

**Role:** small files with known content, read by `tests/` here and by
consumers that implement the same formats.

**Entry points:** —

**Inputs → Outputs:** built once by `tools/make_*_fixtures.py`, committed.

## Files

- `stream-v1/` — stream protocol v1: a tablet excerpt and its timestamps, a
  decodable stream, garbled SEIs, `sync.json` (`tools/make_stream_fixtures.py`).
- `film-v1/` — film.harpia (`tools/make_film_fixtures.py`):
  - `film.json` — a new film's root index: the default parts of mocap-writer
    file-format/layout/1, spaces `w` and `pcp`.
  - `ids/w.json`, `ids/pcp.json` — those spaces' counters.
  - `invalid/<what>.json` — one broken field each; `invalid/expected.json`
    gives the message to read each as and a text its error holds.

## Key facts / gotchas

- The valid film fixtures are byte-for-byte what `to_json` writes
  (`tests/test_film.py`), counter keys sorted.
- The agent name `props-continuity-planner` is a neutral example, no film
  material.

## Touchpoints

- `tests/test_stream_v1.py`, `tests/test_film.py`.
