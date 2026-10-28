## 3. change.harpia (owner: mocap-writer)

- **Status:** Done (2026-10-28)

- **Depends on:** 1
- **Contract:**
  - In: `mocap-writer` file-format layout/2 (decided 2026-10-28)
  - Requires: enum `ChangeOp` (`CREATE`, `UPDATE`, `DELETE`); `Change`:
    `time` (UTC ISO-8601 with `Z`), `by`, `path` (a film path,
    `check_path`), `record` (optional record id), `op`, `before` and
    `after` (the file's JSON text: no `before` on create, no `after` on
    delete, both on update)
  - Delivers: the message and its rules; `mocap_contracts.film.history_file(time)`
    → `history/<yyyy-mm>.jsonl`
- **Tests:** a valid change of each op; each op with the wrong
  before/after refused; a bad time refused
