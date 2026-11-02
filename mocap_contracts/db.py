"""The film's workflow database (workflow.harpia): one SQLite file in the film root.

    with mocap_contracts.db.open(film_root / "workflow.sqlite") as db:
        db.proposals.create(proposal)
        db.reviews.read("proposal-pcp-1")

Harpia generates the SQL: one DAO and one migration per table message, reached
through db_tables.py. This module opens the file, names the tables and keeps
them to the contract: a record is found by its own key, never by Harpia's
HARPIA_ID, and every write runs the rules of mocap_contracts.rules first, so
a broken record is refused and nothing is written.

One program writes at a time. Two writing at once would need a central
service, planned only when that happens. The journal is SQLite's rollback
journal, not WAL: WAL needs shared memory that a film root on a Windows drive
seen from WSL can't give.
"""

from __future__ import annotations

import sqlite3
from os import PathLike
from typing import Generic, TypeVar

from google.protobuf.message import Message

from mocap_contracts.db_tables import TABLES
from mocap_contracts.errors import ContractError
from mocap_contracts.jsonio import to_json

M = TypeVar("M", bound=Message)


class Table(Generic[M]):
    """One table: records found by `key`, their unique field."""

    def __init__(self, conn: sqlite3.Connection, name: str, key: str) -> None:
        self._dao = TABLES[name][0](conn)
        self._key = key

    def _find(self, value: str) -> M | None:
        row = self._dao.MESSAGE()
        return row if getattr(self._dao, f"read_by_{self._key}")(value, row) else None

    @staticmethod
    def _public(row: M) -> M:
        row.ClearField("HARPIA_ID")
        return row

    def create(self, msg: M) -> None:
        """Add a record. A broken one, or one whose key is taken, raises ContractError."""
        to_json(msg)  # required fields and rules, the same checks as a file
        row = self._dao.MESSAGE()
        row.CopyFrom(msg)
        row.ClearField("HARPIA_ID")  # 0: the database assigns it
        try:
            self._dao.create(row)
        except sqlite3.IntegrityError:
            value = getattr(msg, self._key)
            raise ContractError(f"{msg.DESCRIPTOR.name}: {self._key} {value!r} already exists") from None

    def read(self, key: str) -> M | None:
        """The record with this key, or None."""
        row = self._find(key)
        return self._public(row) if row else None

    def list(self, offset: int | None = None, limit: int | None = None) -> list[M]:
        """Every record in the order they were made, or one page of them."""
        return [self._public(row) for row in self._dao.list(offset, limit)]

    def update(self, msg: M) -> bool:
        """Overwrite the record with msg's key. False if there is none; a broken one raises."""
        to_json(msg)
        found = self._find(getattr(msg, self._key))
        if found is None:
            return False
        row = self._dao.MESSAGE()
        row.CopyFrom(msg)
        row.HARPIA_ID = found.HARPIA_ID
        return self._dao.update(row)


class Database:
    """An open workflow database. Close it, or use it in a `with`."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self._conn = conn
        self.proposals = Table(conn, "Proposal", "id")
        self.reviews = Table(conn, "Review", "proposal")
        self.requests = Table(conn, "Request", "id")

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> Database:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def open(path: str | PathLike[str]) -> Database:  # noqa: A001
    """Open or create the database at `path`: tables made, older ones migrated, version stamped."""
    conn = sqlite3.connect(path)
    try:
        conn.execute("PRAGMA journal_mode=DELETE")
        for _, migrate in TABLES.values():
            migrate(conn)
    except BaseException:
        conn.close()
        raise
    return Database(conn)
