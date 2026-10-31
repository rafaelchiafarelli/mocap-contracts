"""Build fixtures/preprod-v1/ (scene_index, change_set and front_matter
test fixtures).

Run once; the outputs are committed. Stdlib only, so the fixtures don't come
from the code they test.

    python3 tools/make_preprod_fixtures.py

Writes:
- bible/scene-index.json: the index of a neutral three-scene script, one
  set and one character linked, one prop word unknown.
- bible/sync/changes.json: a sync's change set, one change of each type.
- invalid/<what>.json: one broken field each, and invalid/expected.json.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "fixtures" / "preprod-v1"


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


SCENES = [
    ("INT. DINING ROOM - NIGHT\n\nANA lifts the BLUE CUP.\n\nANA\nGood morning.\n", "1"),
    ("EXT. STREET - DAY\n\nBia walks past with a MATCHBOX.\n", "2"),
    ("INT. DINING ROOM - DAY\n\nNothing.\n", "2.A"),
]

INDEX = {
    "script_hash": _sha("".join(t for t, _n in SCENES)),
    "scenes": [
        {"scene": "1", "order": 1, "int_ext": "INT.", "location": "DINING ROOM",
         "time_of_day": "NIGHT", "set_id": "set-w-1",
         "characters": [{"name": "ANA", "id": "character-w-2", "speaks": "FLAG_ON"}],
         "props": [{"word": "BLUE CUP", "id": "prop-pcp-1"}],
         "first_page": 1, "last_page": 1, "first_line": 1, "last_line": 7,
         "text_hash": _sha(SCENES[0][0])},
        {"scene": "2", "order": 2, "int_ext": "EXT.", "location": "STREET",
         "time_of_day": "DAY",
         "characters": [{"name": "Bia", "speaks": "FLAG_OFF"}],
         "props": [{"word": "MATCHBOX"}],
         "first_page": 1, "last_page": 2, "first_line": 8, "last_line": 10,
         "text_hash": _sha(SCENES[1][0])},
        {"scene": "2.A", "order": 3, "int_ext": "INT.", "location": "DINING ROOM",
         "time_of_day": "DAY", "set_id": "set-w-1", "characters": [], "props": [],
         "first_page": 2, "last_page": 2, "first_line": 11, "last_line": 13,
         "text_hash": _sha(SCENES[2][0])},
    ],
}


T = "SCENE_CHANGE_TYPE_"
CHANGES = {
    "time": "2026-10-31T12:00:00Z",
    "from_hash": _sha("last accepted index"),
    "to_hash": _sha("current index"),
    "changes": [
        {"type": T + "SCENE_ADDED", "scene": "3"},
        {"type": T + "SCENE_REMOVED", "scene": "2.A"},
        {"type": T + "SCENE_MOVED", "scene": "2", "old_value": "2", "new_value": "1"},
        {"type": T + "HEADING_CHANGED", "scene": "2", "old_value": "EXT. STREET - DAY",
         "new_value": "EXT. STREET - NIGHT"},
        {"type": T + "TEXT_CHANGED", "scene": "1"},
        {"type": T + "CHARACTER_ENTERED", "scene": "1", "new_value": "Bia"},
        {"type": T + "CHARACTER_LEFT", "scene": "2", "old_value": "Bia"},
        {"type": T + "PROP_ADDED", "scene": "1", "new_value": "MATCHBOX"},
        {"type": T + "PROP_REMOVED", "scene": "2", "old_value": "MATCHBOX"},
        {"type": T + "SET_LINK_CHANGED", "scene": "1", "old_value": "set-w-1",
         "new_value": "set-w-3"},
    ],
}


def _write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _broken(base, change):
    obj = copy.deepcopy(base)
    change(obj)
    return obj


INVALID = {
    "index-bad-scene.json": ("SceneIndex", lambda o: o["scenes"][0].update(scene="1a"),
                             "scene must be a scene number"),
    "index-scene-twice.json": ("SceneIndex", lambda o: o["scenes"][1].update(scene="1"),
                               "each scene once"),
    "index-order-gap.json": ("SceneIndex", lambda o: o["scenes"][2].update(order=4),
                             "order must run"),
    "index-bad-hash.json": ("SceneIndex", lambda o: o["scenes"][0].update(text_hash="abc"),
                            "text_hash must be 64"),
    "index-set-not-a-set.json": ("SceneIndex", lambda o: o["scenes"][0].update(set_id="prop-w-1"),
                                 "id must be a set id"),
    "index-character-bad-id.json": ("SceneIndex",
                                    lambda o: o["scenes"][0]["characters"][0].update(id="ana"),
                                    "id must be a character id"),
    "index-empty-prop.json": ("SceneIndex", lambda o: o["scenes"][1]["props"][0].update(word=" "),
                              "word is empty"),
    "index-lines-backwards.json": ("SceneIndex", lambda o: o["scenes"][1].update(last_line=2),
                                   "last_line 2 is before first_line 8"),
    "changes-bad-time.json": ("ChangeSet", lambda o: o.update(time="2026-10-31 12:00"),
                              "time must be UTC"),
    "changes-bad-from-hash.json": ("ChangeSet", lambda o: o.update(from_hash="x"),
                                   "from_hash must be 64"),
    "changes-bad-scene.json": ("ChangeSet", lambda o: o["changes"][0].update(scene="three"),
                               "scene must be a scene number"),
    "changes-type-unset.json": ("ChangeSet", lambda o: o["changes"][0].pop("type"), "type"),
    "index-speaks-unset.json": ("SceneIndex",
                                lambda o: o["scenes"][1]["characters"][0].pop("speaks"),
                                "speaks"),
}


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    _write(OUT / "bible" / "scene-index.json", INDEX)
    expected = {}
    _write(OUT / "bible" / "sync" / "changes.json", CHANGES)
    for name, (message, change, error) in INVALID.items():
        _write(OUT / "invalid" / name, _broken(INDEX if message == "SceneIndex" else CHANGES, change))
        expected[name] = {"message": message, "error": error}
    _write(OUT / "invalid" / "expected.json", expected)


if __name__ == "__main__":
    main()
