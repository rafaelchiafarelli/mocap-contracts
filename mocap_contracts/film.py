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

WRITER = "writer"
WRITER_SPACE = "w"
# A part name is one of these, or "proposals-<code>" with <code> a listed space.
PART_NAMES = ("script", "settings", "bible", "annotations", "history")
PROPOSALS_PREFIX = "proposals-"
SCRIPT_PART = "script"
# An owner is "writer" or an agent's file name in kebab-case.
OWNER = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
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


_DRIVE = re.compile(r"^[A-Za-z]:")
_UNSAFE = re.compile(r'[<>:"|?*\x00-\x1f]')
_RESERVED = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$", re.IGNORECASE)


def segments(path: str) -> tuple[str, ...]:
    """The segments of a film path, one trailing `/` ignored."""
    return tuple(path.removesuffix("/").split("/"))


def path_problem(path: str) -> str | None:
    """Why `path` can't name a place in a film root, or None.

    Relative to the film root, `/` as separator, never leaving it, and a
    name Windows accepts in every segment, so a film copied between Linux
    and Windows still opens. One trailing `/` (a folder) is allowed.
    """
    if not path:
        return "path is empty"
    if path.startswith("/") or "\\" in path or _DRIVE.match(path):
        return f"path must be relative to the film root with '/' as separator, got {path!r}"
    segs = segments(path)
    if any(s in ("", ".", "..") for s in segs):
        return f"path can't hold empty, '.' or '..' segments, got {path!r}"
    for s in segs:
        if _UNSAFE.search(s):
            return f"path can't hold <>:\"|?* or control characters, got {path!r}"
        if s[-1] in ". ":
            return f"a path segment can't end in a dot or a space, got {path!r}"
        if _RESERVED.match(s):
            return f"path can't use the reserved Windows name {s!r}, got {path!r}"
    return None


def check_path(value: str) -> str:
    """Return value if it is a film path (see path_problem), else raise ContractError."""
    if problem := path_problem(value):
        raise ContractError(problem)
    return value
