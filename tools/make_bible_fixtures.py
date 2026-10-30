"""Build fixtures/bible-v1/ (bible.harpia test fixtures).

Run once; the outputs are committed. Stdlib only, so the fixtures don't come
from the code they test.

    python3 tools/make_bible_fixtures.py

Writes a neutral bible folder as mocap-writer keeps it under <film-root>/bible/:
- sets/dining-room/item.json and its child sets/dining-room/table/item.json
- characters/ana/item.json, props/blue-cup/item.json, wardrobe/red-coat/item.json
- not-props.json
- invalid/<what>.json: one broken field each, and invalid/expected.json, which
  says for each file the message to read it as and a text the error must hold.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "fixtures" / "bible-v1"


def _v(field, text=None, *, number=None, unit=None, scene=None, note=None,
       state="VALUE_STATE_SCRIPT_STATED", source="1", department="art", by="writer", revisit=None):
    v = {"field": field}
    if scene is not None:
        v["scene"] = scene
    if text is not None:
        v["text"] = text
    if number is not None:
        v["number"], v["unit"] = number, unit
    if note is not None:
        v["note"] = note
    v.update(state=state, source=source, department=department, by=by)
    if revisit is not None:
        v["revisit"] = revisit
    return v


def _item(id_, name, values, *, aliases=(), parent=None, links=()):
    d = {"id": id_, "name": name, "aliases": list(aliases)}
    if parent:
        d["parent"] = parent
    d["values"] = values
    d["links"] = list(links)
    return d


ITEMS = {
    "sets/dining-room": _item("set-w-1", "Dining Room", [
        _v("space.int_ext", "interior"),
        _v("size.width", number="4.5", unit="m", state="VALUE_STATE_CREATOR_APPROVED",
           source="decision 2026-10-28", by="creator"),
        _v("size.floor_plan", "plans/floor.png", state="VALUE_STATE_CREATOR_APPROVED",
           source="decision 2026-10-28", by="creator"),
        _v("connections.adjoins", "set-w-2", note="through the kitchen door"),
        _v("continuity.changes", "the window is broken", scene="2"),
        _v("light.color_temperature", number="3200", unit="K", state="VALUE_STATE_PROPOSAL",
           department="lighting", by="visual-development-analyst"),
    ], links=[{"scene": "1"}, {"scene": "2"}, {"scene": "2.A"}]),
    "sets/dining-room/table": _item("set-w-3", "Table", [
        _v("dressing.state", "dirty plates"),
    ], parent="set-w-1"),
    "characters/ana": _item("character-w-1", "Ana", [
        _v("identity.age", number="34", unit="year", department="story"),
        _v("identity.species", "human", department="story"),
        _v("relationships.with", "character-w-2", note="sister", department="story"),
        _v("per_scene.emotional_state", "calm", scene="1", department="story"),
        _v("per_scene.wardrobe", "wardrobe-w-1", scene="1", department="story"),
        _v("voice.pitch", "low", state="VALUE_STATE_TBD", department="sound",
           revisit="after the voice casting"),
    ], aliases=["Aninha"], links=[{"scene": "1"}]),
    "props/blue-cup": _item("prop-pcp-1", "Blue Cup", [
        _v("look.color", "blue", department="props"),
        _v("look.material", "enamel", department="props"),
        _v("state.state", "full", scene="1", department="props"),
        _v("ownership.owner", "character-w-1", state="VALUE_STATE_PROPOSAL",
           department="props", by="props-continuity-planner"),
    ], links=[{"scene": "1"}]),
    "wardrobe/red-coat": _item("wardrobe-w-1", "Red Coat", [
        _v("piece.garment", "coat", department="wardrobe"),
        _v("condition.condition", "wet", department="wardrobe"),
        _v("hair_makeup.hair", "wet, flat", scene="1", department="hair-makeup"),
    ], links=[{"scene": "1", "item": "character-w-1"}]),
}
NOT_PROPS = {"words": ["OK", "TV"]}

BASE = ITEMS["props/blue-cup"]


def _bad(edit) -> dict:
    data = copy.deepcopy(BASE)
    edit(data)
    return data


def _value(i: int, **kw):
    return lambda d: d["values"][i].update(kw)


# name: (message, data, text the error must hold)
INVALID = {
    "item-unknown-field": ("BibleItem", _bad(_value(0, field="look.smell")),
                           "BibleItem: values[0]: 'look.smell' is not a prop field of the catalog"),
    "item-not-a-map": ("BibleItem", _bad(lambda d: d.update(id="annotation-w-1")),
                       "BibleItem: id must be a record id of a map"),
    "item-number-as-text": ("BibleItem", _bad(lambda d: d["values"].append(
                                _v("touch.weight", "heavy", department="props"))),
                            "BibleItem: values[4]: touch.weight is a number"),
    "item-number-no-unit": ("BibleItem", _bad(lambda d: d["values"].append(
                                {**_v("touch.weight", department="props"), "number": "0.3"})),
                            "BibleItem.values[4]: a number has a unit"),
    "item-tbd-no-revisit": ("BibleItem", _bad(_value(0, state="VALUE_STATE_TBD")),
                            "BibleItem.values[0]: a TBD value needs its revisit trigger"),
    "item-link-wrong-kind": ("BibleItem", _bad(_value(3, text="prop-w-2")),
                             "BibleItem: values[3]: ownership.owner links to a character id"),
    "item-per-scene-no-scene": ("BibleItem", _bad(lambda d: d["values"][2].pop("scene")),
                                "BibleItem: values[2]: state.state is per scene"),
    "item-scene-not-per-scene": ("BibleItem", _bad(_value(0, scene="1")),
                                 "BibleItem: values[0]: look.color is not per scene"),
    "item-twice": ("BibleItem", _bad(lambda d: d["values"].append(copy.deepcopy(d["values"][0]))),
                   "BibleItem: values[4]: look.color holds one value"),
    "item-bad-scene": ("BibleItem", _bad(lambda d: d["links"].append({"scene": "12a"})),
                       "BibleItem.links[1]: scene must be a scene number"),
    "item-parent-other-map": ("BibleItem", _bad(lambda d: d.update(parent="set-w-1")),
                              "BibleItem: parent must be a prop id"),
    "item-link-item-not-wardrobe": ("BibleItem", _bad(lambda d: d["links"][0].update(item="character-w-1")),
                                    "BibleItem: links: only a wardrobe link names an item"),
    "item-bad-by": ("BibleItem", _bad(_value(0, by="Rafael")),
                    "BibleItem.values[0]: by must be"),
    "item-file-leaves": ("BibleItem", _bad(lambda d: d["values"].append(
                             _v("look.drawings", "../x.png", department="props"))),
                         "BibleItem: values[4]: path can't hold"),
    "not-props-duplicate": ("NotProps", {"words": ["TV", "TV"]},
                            "NotProps: duplicate words ['TV']"),
}


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    for folder, item in ITEMS.items():
        _write(OUT / folder / "item.json", item)
    _write(OUT / "not-props.json", NOT_PROPS)
    expected = {}
    for name, (message, data, error) in INVALID.items():
        _write(OUT / "invalid" / f"{name}.json", data)
        expected[f"{name}.json"] = {"message": message, "error": error}
    _write(OUT / "invalid" / "expected.json", expected)


if __name__ == "__main__":
    main()
