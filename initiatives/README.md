# Initiatives

The full process (initiative → epic → task → contract, branch chain, per-task
loop, stop-and-ask rules) lives in the **mocap-workflow** skill
(`.claude/skills/mocap-workflow/SKILL.md`). Read it before anything else.

Rules specific to this repository:

- **Layout:** `initiatives/<initiative>/epics/<epic>/tasks/<n>-<task>.md`.
  The number is the implementation order, and the file name is the branch name.
- **Done marker:** `-done` suffix on the **file name** (`git mv` in a separate
  commit, right after the implementation commit). Never a status line.
- **Order between epics:** in `initiatives/<initiative>/epics/README.md`.
- **Order between repositories:** in `mocap-studio/HANDOFF.md`.
- **Test suite:** `pytest` at the root (Python repositories) or
  `pio test -e native` (mocap-sync-fw). "Not broken" = green suite.
- **Contracts between repositories** only through the `mocap-contracts` package
  and the session folder layout. Never import code from another mocap repository.
  A change that crosses repositories starts in `mocap-contracts`.

## Index

| Initiative | Status |
|---|---|
| **baseline** — the generation pipeline, the JSON helpers and the first messages | Done — released as `v0.1.0` (2026-10-05; history: `git log -- initiatives/baseline`) |
| **camera-protocol** — stream protocol v1 and the camera's messages and control channel | Done — released as `v0.2.0` (2026-10-05; history: `git log -- initiatives/camera-protocol`) |
| **film-root** — a film root's index and record ids | Done — released as `v0.4.0` (2026-10-27; history: `git log -- initiatives/film-root`) |
| **film-records** — the film bible, its catalog and the change log | Done — released as `v0.5.0` (2026-10-28; history: `git log -- initiatives/film-records`) |
| **script-records** — a script's settings and annotations | Done — released as `v0.6.0` (2026-10-30; history: `git log -- initiatives/script-records`) |
| **preprod-records** — the scene index, change set and front matter | Done — released as `v0.7.0` (2026-10-31; history: `git log -- initiatives/preprod-records`) |
| **workflow-records** — the film's workflow database: proposals, reviews, requests | Done — released as `v0.8.0` (2026-11-01; history: `git log -- initiatives/workflow-records`) |
| [bugs](bugs/bugs.md) | Open — a backlog, fixed when a bug gets in the way |
