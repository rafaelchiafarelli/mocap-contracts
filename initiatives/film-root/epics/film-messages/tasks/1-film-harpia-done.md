## 1. film.harpia (owner: mocap-writer)

- **Status:** Done (2026-10-27)

- **Depends on:** baseline bootstrap (generation, `to_json` / `from_json`,
  `mocap_contracts.rules`); Harpia V5 `map<string,int>` (USAGE §3)
- **Contract:**
  - In: —
  - Requires: the "Decided" sections of `mocap-writer`
    `initiatives/file-format/epics/layout/tasks/1-root-index-and-ids.md`
    (Rafael, 2026-10-26), taken as they are. Every field and rule below says
    where it comes from: **decided** (written in layout/1), **derived**
    (follows from a decided sentence, quoted), or **not decided** (left out,
    question for Rafael at the end).
  - Delivers:
    - `schema/Include/film.harpia`, imported by `schema/mocap.harpia`:
      - `FilmOrigin` — `required string program`, `required string version`
        (decided: "`origin`: `program` and `version` of the last program that
        wrote it")
      - `FilmPart` — `required string name`, `required string path`,
        `required string owner` (decided)
      - `IdSpace` — `required string code`, `required string owner` (decided)
      - `Film` (`film.json`) — `required int format_version`,
        `required FilmOrigin origin`, `repeteable FilmPart parts`,
        `repeteable IdSpace spaces` (decided)
      - `IdCounters` (`ids/<space>.json`) — `required map<string,int> next`,
        e.g. `{"next": {"character": 13, "prop": 4}}` (decided)
      - `enum RecordKind` — `RECORD_KIND_UNSET = 0`, then `SET`, `CHARACTER`,
        `PROP`, `WARDROBE`, `ANNOTATION`, `PROPOSAL` (decided: the six kinds;
        "a new kind is a change to `film.harpia`, never made up by a
        program", so the list lives in the schema)

      The JSON field names are the decided ones; the message names are new
      (`Character` already exists in `session.harpia`, so the kinds are not
      messages here).
    - Rules (`mocap_contracts.rules`, run on read and on write, the path of the
      broken field in every error):
      - `Film.format_version` is `1` (decided: "`format_version` (int, `1`)";
        this contract knows no other version)
      - `FilmOrigin`: `program` and `version` not empty (derived: they say
        who last wrote the file)
      - `FilmPart.path`: relative to the film root, `/` as separator, never
        leaving the root: refused if empty, starting with `/`, holding `\`, a
        drive letter (`C:`), an empty segment (`a//b`), `.` or `..`
        (decided: "no `..`, no drive letter"; derived for `\`, `.` and empty
        segments: "`/` as separator", and a path must name one place). One
        trailing `/` is allowed (`bible/`, as in the default parts).
      - No part's path inside another's or equal to it, compared segment by
        segment (decided: "a part's path is never inside another part's
        path"); so `bible/` and `bible-old/` don't clash
      - Part names unique, not empty (derived: a part is looked up by name)
      - No part's path is `film.json` or inside `ids/` (derived: "the writer
        owns `film.json`"; "the `ids/<space>.json` counters are not parts:
        each one belongs to its space's owner")
      - `FilmPart.owner` and `IdSpace.owner` not empty (derived)
      - `IdSpace.code` matches `^[a-z][a-z0-9]{0,7}$` (decided: "1–8
        lower-case letters or digits, starting with a letter"); codes unique
        within the file (derived: "`film.json` maps every code to its owner")
      - `IdCounters.next`: every key is a kind word, every value ≥ 1
        (decided: "`next`, one entry per kind"; "a counter per kind … starting
        at 1"). A kind with no entry has made no record yet.
    - `mocap_contracts.film` (paths and ids only, like `layout.py`; it reads
      `RecordKind`, so not stdlib only):
      - `KINDS` — the kind words, read from `RecordKind`
        (`"set", "character", …`)
      - `RECORD_ID` — `^(set|character|prop|wardrobe|annotation|proposal)-[a-z][a-z0-9]{0,7}-[1-9][0-9]*$`,
        built from `KINDS`, equal to the regex of layout/1 (decided)
      - `SPACE_CODE` — `^[a-z][a-z0-9]{0,7}$`; `WRITER_SPACE = "w"` (decided)
      - `check_record_id(value)`, `record_id(kind, space, n)`,
        `check_space_code(value)` — raise `ContractError` naming the problem
      - `FILM_FILE = "film.json"`, `ids_file(code)` → `ids/<code>.json`
        (decided)
    - Fixtures in `fixtures/film-v1/`: `film.json` (the default parts of
      layout/1 for a new film, the writer space `w` and one agent space),
      `ids/w.json`, `ids/pcp.json`, and `invalid/<what>.json`, one broken
      field each, listed with the expected error in `invalid/expected.json`
      (built by `tools/make_film_fixtures.py`)
- **Decisions (Claude, for Rafael's review, 2026-10-27):**
  - message names `Film`, `FilmOrigin`, `FilmPart`, `IdSpace`,
    `IdCounters`, `RecordKind` (not visible in the JSON)
  - `to_json` writes map keys sorted: protobuf keeps no map order, so
    `ids/<code>.json` would otherwise change order on every write. No
    earlier message has a map, so nothing else changes.
  - `invalid/expected.json` so `mocap-writer` can run the same cases
- **Not decided (left out, not enforced — questions for Rafael):**
  1. Must every part's owner, and every space's owner, be listed in the other
     list (a part owner has a space, a space owner has a part)?
  2. Must `film.json` always hold the `script` part and the `w` space?
  3. Part names: a fixed set (`script`, `settings`, `bible`, `annotations`,
     `proposals-<code>`, `history`), or any name? Must `proposals-<code>`
     name a listed space?
  4. Owner form: `writer` or an agent's file name in
     `mocap-preprod/.claude/agents/` — checked as kebab-case, or free text?
  5. Characters a path may hold beyond `/`: Windows-safe names only?
  Each one is a stricter rule added later, which can refuse files that are
  valid today, so it is better answered before `mocap-writer` writes films.
- **Pre-work:** none
- **Out of scope:** the library that opens a film root, hands out ids and
  checks ownership (`mocap-writer` layout/1); the other film messages; the
  release (task 2)
- **Tests:** every fixture as above; `Film` and `IdCounters` samples in
  `tests/samples.py` (every message has one); `RECORD_ID` equals the layout/1
  regex text; ids from two spaces never collide; `record_id` refuses a bad
  kind, space or `n`
