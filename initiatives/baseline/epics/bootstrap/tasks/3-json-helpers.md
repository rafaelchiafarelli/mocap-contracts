## 3. JSON helpers

- **Depends on:** 2
- **Contract:**
  - In: generated protobuf messages
  - Requires: `google.protobuf.json_format`; field names preserved
  - Delivers: `to_json(msg)` / `from_json(cls, text)` with a clear error on invalid JSON
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** round-trip per message (parametrized)
