# baseline — epics (execution order)

1. **bootstrap** — Package skeleton and generation pipeline (3 tasks)
2. **messages-v0** — v0 messages (camera controls, session, capture, extract, adapt), layout, hand-off event transport, release (8 tasks)

An epic only merges up into `epics` once all its tasks are `-done` and the suite is green.
