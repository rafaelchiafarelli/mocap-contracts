"""The record ids and the root files of a film root (film.harpia).

    <film-root>/film.json        Film: format version, origin, parts, id spaces
    <film-root>/ids/<code>.json  IdCounters of one id space

A record id is `<kind>-<space>-<n>`, e.g. `character-w-12`: the kind of
record, the code of the space that made it, and that space's counter for the
kind (from 1, no padding). An id is never reused and never changes. A scene
has no record id: it is named by its scene number.

Ids and paths only: nothing here creates folders or touches files.
"""

from __future__ import annotations

import re

from mocap_contracts.errors import ContractError
from mocap_contracts.messages import RecordKind

FORMAT_VERSION = 1
FILM_FILE = "film.json"

# The kind words, in schema order: set, character, prop, wardrobe, annotation, proposal.
KINDS = tuple(
    name.removeprefix("RECORD_KIND_").lower()
    for name in RecordKind.keys()
    if name != "RECORD_KIND_UNSET"
)

WRITER_SPACE = "w"
SPACE_CODE = re.compile(r"^[a-z][a-z0-9]{0,7}$")
RECORD_ID = re.compile(rf"^({'|'.join(KINDS)})-[a-z][a-z0-9]{{0,7}}-[1-9][0-9]*$")


def check_space_code(value: str) -> str:
    """Return value if it is a space code, else raise ContractError."""
    if not isinstance(value, str) or not SPACE_CODE.fullmatch(value):
        raise ContractError(
            f"invalid space code {value!r}: 1-8 lower-case letters or digits, starting with a letter"
        )
    return value


def check_record_id(value: str) -> str:
    """Return value if it is a record id, else raise ContractError."""
    if not isinstance(value, str) or not RECORD_ID.fullmatch(value):
        raise ContractError(
            f"invalid record id {value!r}: <kind>-<space>-<n>, kind one of {list(KINDS)}"
        )
    return value


def record_id(kind: str, space: str, n: int) -> str:
    """The id of the n-th record of `kind` made in `space`."""
    if kind not in KINDS:
        raise ContractError(f"unknown record kind {kind!r}: one of {list(KINDS)}")
    check_space_code(space)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ContractError(f"record number must be an int >= 1, got {n!r}")
    return f"{kind}-{space}-{n}"


def ids_file(code: str) -> str:
    """Path of a space's counters, relative to the film root, `/` separated."""
    return f"ids/{check_space_code(code)}.json"
