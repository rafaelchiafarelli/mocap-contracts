"""The film bible (bible.harpia): maps, the field catalog, folder names.

    <film-root>/bible/<map folder>/<slug>/item.json   BibleItem
    <film-root>/bible/<map folder>/<slug>/<child>/    a child item, same map
    <film-root>/bible/not-props.json                  NotProps

An item's map is the kind of its id (`prop-w-3` is a prop). The catalog
(`catalog/bible-v1.json`, a BibleCatalog) names every field of every map
as `<group>.<field>` with its type; the rules refuse a value whose field it
doesn't list. A scene is named by its scene number in the writer's form.

Names and checks only: nothing here creates folders or touches files.
"""

from __future__ import annotations

import functools
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from mocap_contracts.messages import BibleMap, FieldType, Flag

CATALOG_FILE = Path(__file__).resolve().parent / "catalog" / "bible-v1.json"
ITEM_FILE = "item.json"
NOT_PROPS_FILE = "not-props.json"

# The map words, in schema order: set, character, prop, wardrobe (also record kinds).
MAPS = tuple(
    name.removeprefix("BIBLE_MAP_").lower()
    for name in BibleMap.keys()
    if name != "BIBLE_MAP_UNSET"
)
MAP_FOLDERS = {"set": "sets", "character": "characters", "prop": "props", "wardrobe": "wardrobe"}

# A scene number in the writer's form: 12, 12.A, 12.A.1, 12.A.1.B ...
SCENE = re.compile(r"^[1-9][0-9]*(\.[A-Z]\.[1-9][0-9]*)*(\.[A-Z])?$")
DECIMAL = re.compile(r"^-?[0-9]+(\.[0-9]+)?$")
KEY = re.compile(r"^[a-z][a-z0-9_]*$")
# Who set a value: the creator, the writer, or an agent (its kebab-case name).
BY = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Field:
    """One catalog field of a map, under its full name `<group>.<field>`."""

    name: str
    label: str
    type: str  # text, number, choice, list, file, link
    options: tuple[str, ...]
    unit: str | None
    link_kind: str | None
    group: str
    group_label: str
    per_scene: bool
    department: str

    @property
    def repeats(self) -> bool:
        """A list, file or link field may hold several values per scene key."""
        return self.type in ("list", "file", "link")


def type_word(value: int) -> str:
    return FieldType.Name(value).removeprefix("FIELD_TYPE_").lower()


def map_word(value: int) -> str:
    return BibleMap.Name(value).removeprefix("BIBLE_MAP_").lower()


@functools.cache
def catalog():
    """The approved catalog, read and checked once."""
    from mocap_contracts.jsonio import from_json  # jsonio -> rules -> bible
    from mocap_contracts.messages import BibleCatalog

    return from_json(BibleCatalog, CATALOG_FILE.read_text(encoding="utf-8"))


@functools.cache
def fields(map_: str) -> dict[str, Field]:
    """The fields of one map by full name, in catalog order."""
    for m in catalog().maps:
        if map_word(m.bible_map) == map_:
            return {
                f"{g.key}.{f.key}": Field(
                    name=f"{g.key}.{f.key}", label=f.label, type=type_word(f.type),
                    options=tuple(f.options), unit=f.unit if f.HasField("unit") else None,
                    link_kind=f.link_kind if f.HasField("link_kind") else None,
                    group=g.key, group_label=g.label,
                    per_scene=g.per_scene == Flag.Value("FLAG_ON"),
                    department=g.department,
                )
                for g in m.groups for f in g.fields
            }
    raise KeyError(f"no map {map_!r} in the catalog: one of {list(MAPS)}")


def map_of(record_id: str) -> str | None:
    """The map of an item id (its kind), or None if the kind is not a map."""
    kind = record_id.split("-", 1)[0]
    return kind if kind in MAPS else None


def slug(name: str) -> str:
    """The folder name of an item: `Xícara Azul` -> `xicara-azul`.

    ASCII lower case, accents dropped, every other run of characters a single
    `-`; `item` when nothing is left. A clash in the same folder is the
    caller's to resolve (`-2`, `-3`...).
    """
    ascii_ = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-") or "item"
