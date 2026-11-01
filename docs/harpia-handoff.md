# Harpia handoff: what mocap-contracts needs from the Python SQLite target

From: `mocap-contracts` (Mocap Studio), 2026-10-31. Harpia version: **V5**
(`8f940f7`), Python target, SQLite backend.

Mocap Studio is adding its first table messages (`Proposal`, `Review`,
`Request` in `schema/Include/workflow.harpia`). Each film keeps them in a
SQLite file that lives for years and is opened by every later release of
`mocap-contracts`. Two behaviours of the generated Python DAOs and migrations
block that. Both were seen in the generated output only, not in Harpia's
source. Until Harpia fixes them, `mocap-contracts` `v0.8.0` (the database
module) waits.

## 1. Changing the root file breaks every existing database (blocker)

**Seen:** every table's primary key column is named `ID_<hash>`, as are
`STATUS_<hash>` and `ERROR_<hash>`. The hash comes from the root `.harpia`
file's text. Editing a module doesn't change it; editing the root does, for
example adding `import "new.harpia";`. After such a change, the newly
generated `migrate_<name>(conn)` on a database made by the previous
generation raises:

```
sqlite3.OperationalError: cannot drop PRIMARY KEY column: "ID_cb110dd8cf55c19c22ff64a9cdf4d22e"
```

The migration rolls back, so no rows are lost, but the new code can't open
the database. If the drop had worked, the key values would have been lost
anyway: the new `ID_<new hash>` column is added empty.

**To reproduce:**
1. A root that imports one module holding a table message
   (`message P { required unique string id; } p_table;`). Generate for
   Python.
2. `migrate_P(conn)` on a new SQLite file, then `P_dao(conn).create(...)`
   with its `ID_<hash>` set.
3. Add any `import` line to the root, generate again, and run the new
   `migrate_P(conn)` on the same file.

**What we need**, either of:
- a key column name that doesn't depend on the hash (e.g. `ID`), same for
  `STATUS` / `ERROR`; or
- `migrate_<name>` recognising its own `ID_/STATUS_/ERROR_<other hash>`
  columns and **renaming** them to the current hash (SQLite's `ALTER TABLE
  … RENAME COLUMN` works on a primary key column; tested here), the way
  `renamed_from` does for declared fields.

A note in USAGE §10 on what happens to existing databases when the root
file changes would also help.

Related, maybe intended: only modules the root imports directly are
generated. A root that imports one file which imports the rest generates
no messages, so the root can't be kept frozen to keep the hash stable.

## 2. Absent optional fields come back present and empty

**Seen:** an `optional string` field that isn't set is stored as `''`, not
`NULL`, and `read` / `list` return it **set** (`HasField` is true) with `""`.
The same happens to the optional fields of a nested message stored as flat
columns (`BibleValue.scene` becomes `value_scene`). A record written and read
back isn't equal to the original, and presence carries meaning for us (e.g.
"text only on an edited review", "a value holds either text or number").

**To reproduce:** `message R { required unique string id; optional string
note; } r_table;`. Create one with `id` set and `note` unset, `read` it back:
`r.HasField("note")` is `True`.

**What we need:** an unset optional field (scalar or nested) stored as
`NULL`, and a `NULL` read back as **not set**. A required field, or a set
one holding its default, stays as it is today.

## 3. Nice to have

- **Read by a `unique` field:** the DAO reads only by the integer key. Our
  records are found by their `unique` string `id`. A generated
  `read_by_<field>(value, out)` for `unique` fields would save us SQL of our
  own on Harpia's tables.
- **Key assignment:** the key is caller-assigned. An option for SQLite to
  assign it (`INTEGER PRIMARY KEY` without a value) would save a
  `max(key) + 1` per insert.

## When it's fixed

Tell `mocap-contracts` the Harpia tag. There, `third_party/harpia` moves to
it, `make gen` runs, and `workflow-records` task 2
(`initiatives/workflow-records/epics/workflow/tasks/2-python-database.md`)
goes on, then `v0.8.0` gets released for `mocap-preprod`.
