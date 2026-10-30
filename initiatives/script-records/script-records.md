# script-records — mocap-contracts

**Goal:** the film records that belong to the script: its settings (page
setup, element styles, headers, title layout...) and its annotations
(notes and scene annotations anchored to the script's text), so
`mocap-writer` (fountain-native settings/1 and notes/1) and the previz and
pre-production tools read the same files.

**Source of the contract:** `mocap-writer`
`initiatives/fountain-native/epics/settings/tasks/1-script-settings.md`
(fields approved 2026-10-26) and `.../notes/tasks/1-span-notes.md`
("Decided: the `annotation` message", 2026-10-30), with the annotation
kinds' fields of film-bible contract/1 (approved 2026-10-26, "Scene
annotations"). Rafael gave the go-ahead on 2026-10-30.

**Scope:** `script_settings.harpia`; `annotation.harpia` with the
annotation catalog; release `v0.6.0`.

**Out of scope:** the writer's code; `scene_index`, `change_set`.

**Initiative gate:** the fixtures read as the tasks say; `v0.6.0` installs
from its tag in a clean venv; `mocap-writer` pins it.

Epics: `messages` (3 tasks, in order).
