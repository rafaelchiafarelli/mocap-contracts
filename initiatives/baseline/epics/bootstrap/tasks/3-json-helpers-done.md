## 3. JSON helpers

- **Depends on:** 2
- **Contract:**
  - In: generated messages (re-exported by `mocap_contracts`); the `.harpia` sources in `schema/`
  - Requires: `google.protobuf.json_format` (Harpia V4 documents no Python JSON API, USAGE §7.2 is C++ only); field names exactly as declared in `.harpia`
  - Delivers:
    - `to_json(msg)` / `from_json(cls, text)`, with a clear error on invalid JSON
    - **Only declared fields** in the JSON. Harpia adds bookkeeping fields to every message (`ID_<hash>`, `STATUS_<hash>`, `ERROR_<hash>`, `ORIGINATOR`), and some carry the root file's hash in their name. `to_json` never writes them, and `from_json` rejects any key that isn't declared.
    - **`required` enforced.** It doesn't survive into proto3 (generated as a plain field), so the declared and required field sets per message are extracted from `schema/` by `make gen` into `mocap_contracts/messages.py`. `to_json` always writes every non-`optional` field, defaults included, so the files are explicit. `from_json` rejects JSON missing a required key, at any nesting level.
- **Pre-work:** none
- **Out of scope:** validating values (ranges, units). That belongs to each message's task.
- **Tests:** round-trip per message (parametrized); bookkeeping fields never written; unknown key rejected; missing required key rejected (top level and nested); a required field holding its default value (0, "") survives the round trip
