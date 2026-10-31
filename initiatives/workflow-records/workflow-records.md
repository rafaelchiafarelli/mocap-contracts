# workflow-records — mocap-contracts

**Goal:** the film's workflow database: the records the pre-production
agents and the writer exchange (proposals for bible values, the creator's
reviews of them, requests between agents and to the creator), declared as
Harpia table messages and read and written through the SQLite access code
Harpia generates for Python.

**Decided (Rafael, 2026-10-31):**
- The records live in one SQLite file in the film root, not in one JSON
  file per record: a film can hold thousands of proposals.
- Agents write through a tool (an MCP server in `mocap-preprod`) that uses
  this package, never by editing files; the writer reads and writes the
  same database with the same code. The bible stays the writer's JSON.
- One program writes at a time (one creator for now). Several users or
  several agents writing at once would need a central service, planned
  only when that happens.
- One id space per agent; an agent proposes for an existing bible item
  only, never creates items or scene links.

**Source of the contract:** `mocap-preprod`
`initiatives/preprod-link/preprod-link.md` (planned 2026-10-31).

**Scope:** `workflow.harpia` (`Proposal`, `Review`, `Request`), the record
kind `request`, the generated SQLite access in the package, the film part
`workflow`; release `v0.8.0`.

**Out of scope:** the worklist and the decision register (later, with
`mocap-dashboard`'s workflow model); which version of the script a
proposal answers (waits for the writer's `versioning` initiative); the
MCP server (`mocap-preprod`); the writer's review of proposals
(`mocap-writer` `workflow-link`).

**Initiative gate:** the fixtures read as the tasks say; a database made
with `mocap_contracts.db` round-trips each table; `v0.8.0` installs from
its tag in a clean venv.

Epics: `workflow` (4 tasks, in order).
