## 3. front_matter.harpia (owner: mocap-writer)

- **Depends on:** 2
- **Contract:**
  - Requires: `FrontMatter` (`settings/front-matter.json`, part
    `front-matter`): `title` (`TitlePage`: title, subtitle, episode,
    author, repeated co_authors, email), `overview` (`Overview`: include,
    cast, sets, acts Flags: what the printed page computes), `pitch`
    (`Pitch`: include Flag, pitch, logline, target_audience), `argument`
    (`Argument`: include Flag, text); every field written, empty strings
    allowed. Film part names gain `front-matter` and `source` (the
    original of an imported script, mocap-writer import-to-film)
  - Rules: co-authors not empty
  - Delivers: the messages, `PART_NAMES`, fixtures
- **Tests:** fixtures round-trip; an empty co-author refused; a film with
  the two new parts is valid
