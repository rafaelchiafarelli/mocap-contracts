# preprod-records — mocap-contracts

**Goal:** the records that link `mocap-writer` to the pre-production
agents and print the film's front matter: the scene index the agents
read, the change set a Sync to spec writes, and the front matter record
(title page and three optional pages).

**Source of the contract:** `mocap-writer`
`initiatives/preprod-link/epics/contract/tasks/1-scene-index.md` and
`2-change-set.md` (planned 2026-10-24), and
`initiatives/front-matter/epics/contract/tasks/1-front-matter-message.md`
(decided 2026-10-31). Rafael gave the go-ahead on 2026-10-31.

**Scope:** `scene_index.harpia`, `change_set.harpia`,
`front_matter.harpia`; the film part names `front-matter` and `source`;
release `v0.7.0`.

**Out of scope:** the writer's code; how agents write proposals (open,
mocap-preprod).

**Initiative gate:** the fixtures read as the tasks say; `v0.7.0` installs
from its tag in a clean venv; `mocap-writer` pins it.

Epics: `messages` (4 tasks, in order).
