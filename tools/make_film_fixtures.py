"""Build fixtures/film-v1/ (film.harpia test fixtures).

Run once; the outputs are committed. Stdlib only, so the fixtures don't come
from the code they test.

    python3 tools/make_film_fixtures.py

Writes:
- film.json: a new film's root index, with the default parts of mocap-writer
  file-format/layout/1, the writer space `w` and one agent space.
- ids/w.json, ids/pcp.json: the counters of those two spaces.
- invalid/<what>.json: one broken field each, and invalid/expected.json, which
  says for each file the message to read it as and a text the error must
  hold (the path of the broken field). Consumers can run the same list.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "fixtures" / "film-v1"

FILM = {
    "format_version": 1,
    "origin": {"program": "mocap-writer", "version": "1.0.0"},
    "parts": [
        {"name": "script", "path": "script.fountain", "owner": "writer"},
        {"name": "settings", "path": "settings/script-settings.json", "owner": "writer"},
        {"name": "bible", "path": "bible/", "owner": "writer"},
        {"name": "annotations", "path": "annotations/", "owner": "writer"},
        {"name": "proposals-pcp", "path": "proposals/props-continuity-planner/",
         "owner": "props-continuity-planner"},
        {"name": "history", "path": "history/", "owner": "writer"},
    ],
    "spaces": [
        {"code": "w", "owner": "writer"},
        {"code": "pcp", "owner": "props-continuity-planner"},
    ],
}
IDS = {
    "w": {"next": {"character": 13, "prop": 4, "set": 2}},
    "pcp": {"next": {"proposal": 3}},
}


def _film(edit) -> dict:
    data = copy.deepcopy(FILM)
    edit(data)
    return data


def _part(i: int, **kw):
    return lambda d: d["parts"][i].update(kw)


def _space(i: int, **kw):
    return lambda d: d["spaces"][i].update(kw)


# name: (message, data, text the error must hold)
INVALID = {
    "film-format-version": ("Film", _film(lambda d: d.update(format_version=2)),
                            "Film: format_version must be 1"),
    "film-no-origin": ("Film", _film(lambda d: d.pop("origin")),
                       "Film: missing required field(s) ['origin']"),
    "film-origin-empty-program": ("Film", _film(lambda d: d["origin"].update(program="")),
                                  "Film.origin: empty ['program']"),
    "film-unknown-field": ("Film", _film(lambda d: d.update(title="x")),
                           "Film: unknown field(s) ['title']"),
    "part-no-owner": ("Film", _film(lambda d: d["parts"][0].pop("owner")),
                      "Film.parts[0]: missing required field(s) ['owner']"),
    "part-leaves-root": ("Film", _film(_part(0, path="../script.fountain")),
                         "Film.parts[0]: path can't hold"),
    "part-absolute": ("Film", _film(_part(0, path="/script.fountain")),
                      "Film.parts[0]: path must be relative"),
    "part-drive-letter": ("Film", _film(_part(0, path="G:/films/script.fountain")),
                          "Film.parts[0]: path must be relative"),
    "part-backslash": ("Film", _film(_part(1, path="settings\\script-settings.json")),
                       "Film.parts[1]: path must be relative"),
    "part-in-ids": ("Film", _film(_part(5, path="ids/history/")),
                    "Film.parts[5]: path can't be film.json or inside ids/"),
    "part-inside-another": ("Film", _film(lambda d: d["parts"].append(
                                {"name": "sync", "path": "bible/sync/", "owner": "writer"})),
                            "Film: parts 'bible' and 'sync': one path is inside the other"),
    "part-duplicate-name": ("Film", _film(_part(5, name="bible")),
                            "Film: duplicate part names ['bible']"),
    "space-bad-code": ("Film", _film(_space(1, code="PCP")),
                       "Film.spaces[1]: code must be"),
    "space-duplicate-code": ("Film", _film(_space(1, code="w")),
                             "Film: duplicate space codes ['w']"),
    # The five rules decided on 2026-10-28 (film-records messages/1).
    "film-no-script": ("Film", _film(lambda d: d["parts"].pop(0)),
                       "Film: parts: no 'script' part"),
    "film-no-writer-space": ("Film", _film(lambda d: d["spaces"].pop(0)),
                             "Film: spaces: no 'w' space owned by 'writer'"),
    "part-owner-no-space": ("Film", _film(_part(4, owner="set-designer")),
                            "Film: parts: owners ['set-designer'] have no space"),
    "part-bad-name": ("Film", _film(_part(5, name="notes")),
                      "Film.parts[5]: name must be one of"),
    "part-proposals-no-space": ("Film", _film(_part(4, name="proposals-xyz")),
                                "Film: part 'proposals-xyz': no space 'xyz'"),
    "part-bad-owner": ("Film", _film(_part(1, owner="Writer")),
                       "Film.parts[1]: owner must be 'writer' or an agent name"),
    "space-bad-owner": ("Film", _film(_space(1, owner="Props Planner")),
                        "Film.spaces[1]: owner must be 'writer' or an agent name"),
    "part-windows-unsafe": ("Film", _film(_part(0, path="script?.fountain")),
                            "Film.parts[0]: path can't hold <>"),
    "part-trailing-dot": ("Film", _film(_part(2, path="bible./")),
                          "Film.parts[2]: a path segment can't end in a dot or a space"),
    "part-reserved-name": ("Film", _film(_part(0, path="CON.fountain")),
                           "Film.parts[0]: path can't use the reserved Windows name"),
    "ids-unknown-kind": ("IdCounters", {"next": {"scene": 3}},
                         "IdCounters: next: unknown record kinds ['scene']"),
    "ids-zero": ("IdCounters", {"next": {"prop": 0}},
                 "IdCounters: next: counters start at 1"),
    "ids-no-next": ("IdCounters", {},
                    "IdCounters: missing required field(s) ['next']"),
}


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    _write(OUT / "film.json", FILM)
    for code, counters in IDS.items():
        _write(OUT / "ids" / f"{code}.json", counters)
    expected = {}
    for name, (message, data, error) in INVALID.items():
        _write(OUT / "invalid" / f"{name}.json", data)
        expected[f"{name}.json"] = {"message": message, "error": error}
    _write(OUT / "invalid" / "expected.json", expected)


if __name__ == "__main__":
    main()
