## 1. The five film.json rules

- **Depends on:** `film-root` (`v0.4.0`)
- **Contract:**
  - In: the five questions of `film-root/epics/film-messages/tasks/1-film-harpia-done.md`
  - Requires (Rafael, 2026-10-28, all five, enforced here):
    1. every part whose owner is not `writer` has a space with that owner
       (a space may outlive its part);
    2. `film.json` holds a `script` part and the space `w` owned by
       `writer`;
    3. part names: `script`, `settings`, `bible`, `annotations`,
       `history`, or `proposals-<code>` with `<code>` a listed space;
    4. owners: `writer` or kebab-case `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`;
    5. Windows-safe paths: no `<>:"|?*` or control characters, no segment
       ending in `.` or a space, no reserved device name (`CON`, `PRN`,
       `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9`, with or without an
       extension).
  - Delivers: the rules in `mocap_contracts.rules`; `mocap_contracts.film`
    gains `PART_NAMES`, `OWNER`, `check_path(value)` (rule 5 plus the
    relative-path rules, for any path a film record holds); one invalid
    fixture per rule in `fixtures/film-v1/invalid/`
- **Tests:** the valid fixture still round trips; each new invalid
  fixture is refused naming its field
