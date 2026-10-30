"""Build fixtures/annotation-v1/ (annotation.harpia test fixtures).

Run once; the outputs are committed. Stdlib only, so the fixtures don't come
from the code they test.

    python3 tools/make_annotation_fixtures.py

Writes a neutral annotations folder as mocap-writer keeps it under
<film-root>/annotations/: a note on a quoted span, a character direction on
a whole element, a shot on a scene with its counters, and invalid ones with
invalid/expected.json.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "fixtures" / "annotation-v1"


def _v(field, text=None, *, number=None, unit=None, state="VALUE_STATE_CREATOR_APPROVED",
       source="decision 2026-10-30", department="camera", by="creator"):
    v = {"field": field}
    if text is not None:
        v["text"] = text
    if number is not None:
        v["number"], v["unit"] = number, unit
    v.update(state=state, source=source, department=department, by=by)
    return v


def _ann(id_, kind, anchor, *, text=None, by="creator", shot=None, values=()):
    d = {"id": id_, "kind": f"ANNOTATION_KIND_{kind}", "anchor": anchor}
    if text is not None:
        d["text"] = text
    d["by"] = by
    if shot is not None:
        d["shot"] = shot
    d["values"] = list(values)
    return d


ANNOTATIONS = {
    "annotation-w-1": _ann("annotation-w-1", "NOTE",
                           {"scene": "1", "element": 1, "quote": "runs down the street", "occurrence": 1},
                           text="Faster than in the rehearsal."),
    "annotation-w-2": _ann("annotation-w-2", "CHARACTER_DIRECTION", {"scene": "1", "element": 3},
                           values=[_v("direction.character", "character-w-1", department="capture"),
                                   _v("direction.intensity", "high", department="capture")]),
    "annotation-w-3": _ann("annotation-w-3", "SHOT", {"scene": "1.A", "element": 2}, shot=4,
                           values=[_v("framing.size", "close-up"),
                                   _v("lens.focal_length", number="50", unit="mm"),
                                   _v("framing.characters", "character-w-1"),
                                   _v("framing.characters", "character-w-2")]),
    # an agent's proposal on a whole scene
    "annotation-pcp-1": _ann(
        "annotation-pcp-1", "PROP_DIRECTION", {"scene": "2"}, by="props-continuity-planner",
        values=[_v("direction.prop", "prop-w-1", state="VALUE_STATE_PROPOSAL", source="2",
                   department="props", by="props-continuity-planner"),
                _v("direction.action", "breaks", state="VALUE_STATE_PROPOSAL", source="2",
                   department="props", by="props-continuity-planner")]),
}
COUNTERS = {"next": {"1.A": 5}}

BASE = ANNOTATIONS["annotation-w-3"]


def _bad(edit, base=BASE):
    data = copy.deepcopy(base)
    edit(data)
    return data


INVALID = {
    "unknown-field": ("Annotation", _bad(lambda d: d["values"][0].update(field="framing.mood")),
                      "Annotation: values[0]: 'framing.mood' is not a shot field of the catalog"),
    "shot-without-number": ("Annotation", _bad(lambda d: d.pop("shot")),
                            "Annotation: a shot needs its number in the scene"),
    "number-on-a-note": ("Annotation", _bad(lambda d: d.update(shot=1), ANNOTATIONS["annotation-w-1"]),
                         "Annotation: only a shot has a shot number, not a note"),
    "quote-without-element": ("Annotation", _bad(lambda d: d["anchor"].pop("element"),
                                                 ANNOTATIONS["annotation-w-1"]),
                              "Annotation.anchor: a quote needs its element"),
    "bad-scene": ("Annotation", _bad(lambda d: d["anchor"].update(scene="1a")),
                  "Annotation.anchor: scene must be a scene number"),
    "value-with-scene": ("Annotation", _bad(lambda d: d["values"][0].update(scene="1.A")),
                         "Annotation: values[0]: framing.size is not per scene"),
    "bad-id": ("Annotation", _bad(lambda d: d.update(id="prop-w-1")),
               "Annotation: id must be an annotation id"),
    "counters-bad-scene": ("ShotCounters", {"next": {"one": 2}},
                           "ShotCounters: next: keys must be scene numbers"),
}


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    for rid, data in ANNOTATIONS.items():
        _write(OUT / f"{rid}.json", data)
    _write(OUT / "shot-counters.json", COUNTERS)
    expected = {}
    for name, (message, data, error) in INVALID.items():
        _write(OUT / "invalid" / f"{name}.json", data)
        expected[f"{name}.json"] = {"message": message, "error": error}
    _write(OUT / "invalid" / "expected.json", expected)


if __name__ == "__main__":
    main()
