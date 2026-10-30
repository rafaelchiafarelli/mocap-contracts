"""The annotations of a script (annotation.harpia): kinds, catalog, files.

    <film-root>/annotations/<id>.json            Annotation
    <film-root>/annotations/shot-counters.json   ShotCounters

An annotation is anchored to the script by its scene number, the element's
index in the scene (the heading is 0; none: the whole scene) and the quoted
text with its occurrence (none: the whole element). Nothing is written in
the Fountain text. Its values are bible values checked against the
annotation catalog (`catalog/annotation-v1.json`, an AnnotationCatalog) by
kind. A shot carries its number in its scene (`S<n>`); the next number of
each scene is in the shot counters, so a number never comes back.

Names and checks only: nothing here creates folders or touches files.
"""

from __future__ import annotations

import functools
from pathlib import Path

from mocap_contracts import bible
from mocap_contracts.messages import AnnotationKind

CATALOG_FILE = Path(__file__).resolve().parent / "catalog" / "annotation-v1.json"
SHOT_COUNTERS_FILE = "shot-counters.json"

# The kind words, in schema order: note, character_direction, ..., shot.
KINDS = tuple(
    name.removeprefix("ANNOTATION_KIND_").lower()
    for name in AnnotationKind.keys()
    if name != "ANNOTATION_KIND_UNSET"
)


def kind_word(value: int) -> str:
    return AnnotationKind.Name(value).removeprefix("ANNOTATION_KIND_").lower()


def kind_value(word: str) -> int:
    return AnnotationKind.Value("ANNOTATION_KIND_" + word.upper())


def file_name(record_id: str) -> str:
    """An annotation's file in the annotations part."""
    return f"{record_id}.json"


def shot_name(scene: str, shot: int) -> str:
    """The full name of a shot: `12.A S4`; in a file name use shot_file_name."""
    return f"{scene} S{shot}"


def shot_file_name(scene: str, shot: int) -> str:
    return f"{scene}_S{shot}"


@functools.cache
def catalog():
    """The approved annotation catalog, read and checked once."""
    from mocap_contracts.jsonio import from_json  # jsonio -> rules -> annotation
    from mocap_contracts.messages import AnnotationCatalog

    return from_json(AnnotationCatalog, CATALOG_FILE.read_text(encoding="utf-8"))


@functools.cache
def fields(kind: str) -> dict[str, bible.Field]:
    """The fields of one kind by full name `<group>.<field>`, in catalog order."""
    for k in catalog().kinds:
        if kind_word(k.kind) == kind:
            return bible.fields_of(k.groups)
    raise KeyError(f"no kind {kind!r} in the annotation catalog: one of {list(KINDS)}")
