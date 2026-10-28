# film-records — mocap-contracts

**Goal:** the records a film root holds besides its index: the five rules
`film-root` left open, the film bible's items with the approved field
catalog, and the change log, so `mocap-writer` (file-format layout/1 and
layout/5, film-bible contract/2) and the `mocap-preprod` agents read and
write the same files.

**Source of the contract:** `mocap-writer` decisions of 2026-10-28
(Rafael): `initiatives/file-format/epics/layout/tasks/1-root-index-and-ids.md`
("the five rules"), `2-history.md` ("a change log"),
`initiatives/film-bible/epics/contract/tasks/1-field-catalog.md` (the
approved catalog, 2026-10-26) and `2-bible-contract.md` ("Decided").
Rafael gave the go-ahead for this repository on 2026-10-28.

**Scope:** the film rules; `bible.harpia` and `catalog/bible-v1.json`;
`change.harpia`; release `v0.5.0`.

**Out of scope:** the writer's libraries; the `script_settings`,
`annotation`, `scene_index` and `change_set` messages (planned later);
annotation kinds in the catalog (fountain-native/notes/1).

**Initiative gate:** the fixtures read as the tasks say; `v0.5.0` installs
from its tag in a clean venv; `mocap-writer` pins it.

Epics: `messages` (4 tasks, in order).
