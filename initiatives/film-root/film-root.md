# film-root — mocap-contracts

**Goal:** the messages a film root is made of, starting with its root index
`film.json` and the record ids, so the writer (`mocap-writer`) and the
pre-production agents (`mocap-preprod`) read and write the same film without
colliding.

**Source of the contract:** `mocap-writer`
`initiatives/file-format/epics/layout/tasks/1-root-index-and-ids.md`, its
"Decided" sections (Rafael, 2026-10-26), and option A of
`initiatives/file-format/epics/study/tasks/3-options.md` (a folder of Harpia
JSON records, ISOXML-style, Rafael 2026-10-25). Rafael gave the go-ahead for
this repository (2026-10-27).

**Scope:**
- **`film.harpia`** (owner: `mocap-writer`): `film.json` (format version,
  origin, parts, id spaces), the `ids/<space>.json` counters, the record kinds.
- `mocap_contracts.film`: the record id form and its regex, the space-code
  form, the two file names.
- Fixtures: a valid film root's `film.json` and counters; invalid files, each
  naming its broken field.
- Release `v0.4.0`, so `mocap-writer` can pin it.

**Out of scope:** the writer-side library that opens a film root (layout/1 in
`mocap-writer`); the `script_settings`, `bible`, `annotation`, `scene_index`
and `change_set` messages (one task each, planned later, `film` first);
history (`mocap-writer` layout/2).

**Initiative gate:** the fixtures read as the task says (valid ones round
trip byte for byte, each invalid one is refused with its field in the
message); `v0.4.0` installs from its tag in a clean venv.

General context, cross-repository order and open questions:
`mocap-studio/HANDOFF.md`.
