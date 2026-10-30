## 1. script_settings.harpia (owner: mocap-writer)

- **Depends on:** `v0.5.0`
- **Contract:**
  - Requires: `ScriptSettings` (`settings/script-settings.json`) with the
    approved fields: `page`, `elements` (one `ElementStyle` per element,
    a `screen` and an `export` `TextStyle`), `pdf` (flags and four
    `PdfFont`s), `strings`, `headers`, `auto_completion`, `locations`,
    `spelling_words`, `title_page` (pages of `TitleString`s and the
    Fountain block they were saved with); enums `ScriptElement`,
    `TextAlign`, `TitleFont`; every field written, defaults included
  - Rules: values outside Trelby's limits are refused with their path
    (font size 4–72, margins 0–900 mm, paper 50–1000 × 100–1000 mm, page
    break lines 1–30, scene-continued indent −20–80, spacing 0–50 and
    0–20 tenths, indent 0–80, width 5–80, header line 1–5, header offset
    −100–100, empty lines after 0–5, title size 4–288); one style per
    element, each element once; a PDF font name without the characters a
    PostScript name refuses
  - Delivers: the messages, `fixtures/script-v1/` (a default settings
    file, invalid ones with `invalid/expected.json`)
- **Tests:** fixtures; samples
