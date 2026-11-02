## 2. The SQLite access in the package

- **Depends on:** 1
- **Harpia V6 (2026-11-01):** the pre-work found that V5's key column
  `ID_<hash>` broke every film database when the root `.harpia` changed, and
  an absent optional field read back present and empty. Rafael chose to wait
  for Harpia; V6 fixes both.
- **Pre-work:** check that Harpia's Python target emits the CRUDL code
  (`harpia_runtime.db` and one DAO per table message, `PyDatabase/`) for
  the three messages, nested `BibleValue` included. If it can't express
  one of them, stop and bring it to Rafael (Harpia is a black box).
- **Contract:**
  - `tools/harpia_gen.py` keeps Harpia's generated database code in the
    package as `mocap_contracts.db`, committed like the rest.
  - `mocap_contracts.db.open(path)` opens or creates the film's database:
    tables made, older databases migrated (Harpia's `migrate_<name>`,
    schema version stamped), rollback journal (no WAL: film roots can sit
    on a Windows drive seen from WSL).
  - The rules of task 1 run on every write; a broken record is refused
    and nothing is written.
  - Documented limit: one program writes at a time.
- **Tests:** create, read, list, update of each table on a temporary
  database; an invalid record refused; a database made by this version
  opens again after a no-op migration
