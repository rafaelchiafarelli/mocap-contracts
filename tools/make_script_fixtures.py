"""Build fixtures/script-v1/ (script_settings.harpia test fixtures).

Run once; the outputs are committed. Stdlib only, so the fixtures don't come
from the code they test.

    python3 tools/make_script_fixtures.py

Writes:
- settings/script-settings.json: a new script's settings, every field at
  mocap-writer's defaults (Trelby's Config, AutoCompletion and Headers as
  of 2026-10-30), as the writer writes them for a new film.
- invalid/<what>.json: one broken field each, and invalid/expected.json.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "fixtures" / "script-v1"

ON, OFF = "FLAG_ON", "FLAG_OFF"


def _style(caps=False, bold=False, italic=False, underlined=False):
    return {"caps": ON if caps else OFF, "bold": ON if bold else OFF,
            "italic": ON if italic else OFF, "underlined": ON if underlined else OFF}


def _element(name, before, intra, indent, width, screen, export):
    return {"element": f"SCRIPT_ELEMENT_{name}", "before_spacing_tenths": before,
            "intra_spacing_tenths": intra, "indent_chars": indent, "width_chars": width,
            "screen": _style(*screen), "export": _style(*export)}


def _font():
    return {"pdf_name": "", "filename": ""}


TRANSITIONS = ["BACK TO:", "CROSSFADE:", "CUT TO:", "DISSOLVE TO:", "FADE IN:", "FADE OUT",
               "FADE TO BLACK", "FLASHBACK TO:", "JUMP CUT TO:", "MATCH CUT TO:",
               "SLOW FADE TO BLACK", "SMASH CUT TO:", "TIME CUT:"]

DEFAULTS = {
    "page": {
        "paper_width_mm": 210.0, "paper_height_mm": 297.0,
        "margin_top_mm": 12.7, "margin_bottom_mm": 25.4,
        "margin_left_mm": 38.1, "margin_right_mm": 25.4,
        "font_size_pt": 12, "page_break_action_lines": 2, "page_break_dialogue_lines": 2,
        "scene_continueds": OFF, "scene_continued_indent_chars": 45,
    },
    "elements": [
        _element("SCENE", 10, 0, 0, 60, (1, 1, 0, 0), (1, 0, 0, 0)),
        _element("ACTION", 10, 0, 0, 60, (0, 0, 0, 0), (0, 0, 0, 0)),
        _element("CHARACTER", 10, 0, 22, 38, (1, 0, 0, 0), (1, 0, 0, 0)),
        _element("DIALOGUE", 0, 0, 10, 35, (0, 0, 0, 0), (0, 0, 0, 0)),
        _element("PAREN", 0, 0, 16, 25, (0, 0, 0, 0), (0, 0, 0, 0)),
        _element("TRANSITION", 10, 0, 45, 20, (1, 0, 0, 0), (1, 0, 0, 0)),
        _element("SHOT", 10, 0, 0, 60, (1, 0, 0, 0), (1, 0, 0, 0)),
        _element("ACT_BREAK", 10, 0, 25, 10, (1, 1, 0, 1), (1, 0, 0, 1)),
        _element("NOTE", 10, 0, 5, 55, (0, 0, 1, 0), (0, 0, 1, 0)),
    ],
    "pdf": {
        "show_scene_numbers": OFF, "include_toc": ON, "show_toc": ON,
        "open_on_current_page": ON, "remove_notes": OFF, "outline_notes": ON,
        "show_margins": OFF, "show_line_numbers": OFF,
        "normal": _font(), "bold": _font(), "italic": _font(), "bold_italic": _font(),
    },
    "strings": {
        "more": "(MORE)", "continued_page_end": "(CONTINUED)",
        "continued_page_start": "CONTINUED:", "dialogue_continued": " (cont'd)",
    },
    "headers": {
        "empty_lines_after": 1,
        "lines": [{"line": 1, "x_offset_chars": 0, "align": "TEXT_ALIGN_RIGHT",
                   "bold": OFF, "italic": OFF, "underlined": OFF, "text": "${PAGE}."}],
    },
    "auto_completion": [
        {"element": "SCRIPT_ELEMENT_SCENE", "enabled": ON, "items": []},
        {"element": "SCRIPT_ELEMENT_CHARACTER", "enabled": ON, "items": []},
        {"element": "SCRIPT_ELEMENT_TRANSITION", "enabled": ON, "items": TRANSITIONS},
        {"element": "SCRIPT_ELEMENT_SHOT", "enabled": ON, "items": []},
    ],
    "locations": [],
    "spelling_words": [],
    "title_page": {"pages": [], "fountain_title": ""},
}


def _ordered(d):
    """In declared order, as to_json writes them (DEFAULTS is written so)."""
    return d


def _bad(edit):
    data = copy.deepcopy(DEFAULTS)
    edit(data)
    return _ordered(data)


INVALID = {
    "font-size": ("ScriptSettings", _bad(lambda d: d["page"].update(font_size_pt=80)),
                  "ScriptSettings.page: font_size_pt must be 4..72, got 80"),
    "width": ("ScriptSettings", _bad(lambda d: d["elements"][0].update(width_chars=2)),
              "ScriptSettings.elements[0]: width_chars must be 5..80"),
    "element-twice": ("ScriptSettings", _bad(lambda d: d["elements"].__setitem__(1, copy.deepcopy(d["elements"][0]))),
                      "ScriptSettings: elements: one style per element, twice ['SCRIPT_ELEMENT_SCENE']"),
    "element-missing": ("ScriptSettings", _bad(lambda d: d["elements"].pop()),
                        "ScriptSettings: elements: no style for ['SCRIPT_ELEMENT_NOTE']"),
    "pdf-name": ("ScriptSettings", _bad(lambda d: d["pdf"]["bold"].update(pdf_name="My Font")),
                 "ScriptSettings.pdf.bold: pdf_name can't hold"),
    "header-line": ("ScriptSettings", _bad(lambda d: d["headers"]["lines"][0].update(line=6)),
                    "ScriptSettings.headers.lines[0]: line must be 1..5"),
    "no-page": ("ScriptSettings", _bad(lambda d: d.pop("page")),
                "ScriptSettings: missing required field(s) ['page']"),
}


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    _write(OUT / "settings" / "script-settings.json", _ordered(DEFAULTS))
    expected = {}
    for name, (message, data, error) in INVALID.items():
        _write(OUT / "invalid" / f"{name}.json", data)
        expected[f"{name}.json"] = {"message": message, "error": error}
    _write(OUT / "invalid" / "expected.json", expected)


if __name__ == "__main__":
    main()
