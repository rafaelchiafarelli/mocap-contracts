## 1. The reproducibility test fails on every fresh clone

- **Status:** Fixed (2026-10-27) — fixes/000097/gen-test-empty-dirs
- **Symptom:** `tests/test_gen_reproducible.py` fails with
  `only in one side: test, db, rest, soap`. Harpia's Java run creates the
  empty folders `gen/java/src/test/` and `com/harpia/generated/{db,rest,soap}/`;
  git can't store an empty folder, so a fresh clone lacks them, while the
  clone that ran `make gen` keeps them on disk and passes.
- **Where:** `tests/test_gen_reproducible.py:30` (`_diff` compared folders,
  not files)
- **Reproduce:** clone `dev`, `git submodule update --init`, `.venv/bin/pytest`
  with Docker running (2026-10-27, lane C session).
- **Impact:** the suite is red on any new clone, so no task there can meet
  its DoD.
