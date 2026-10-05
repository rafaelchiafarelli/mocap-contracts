## 3. JSON helpers

- **Depends on:** 2
- **Contract:**
  - In: generated messages
  - Requires: the JSON serialization Harpia generates for Python, if its documented interface has one; otherwise `google.protobuf.json_format`. Field names kept as declared either way.
  - Delivers: `to_json(msg)` / `from_json(cls, text)` with a clear error on invalid JSON
- **Pre-work:** after task 2, read the documented Python output and record which serializer this task wraps
- **Out of scope:** —
- **Tests:** round-trip per message (parametrized)
