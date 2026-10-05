## 7. Hand-off event transport (Harpia ZeroMQ)

- **Depends on:** 3; bootstrap/2
- **Contract:**
  - In: `TakeClosed`, `CameraFileReady` (task 3)
  - Requires:
    - Harpia submodule bumped from `V4` to **`V5`**. V5 is V4 plus the docs for ZeroMQ in Python and Java (USAGE §7.6, §7.7, §7.9, §11); the generated code is the same, and `make check-gen` proves it.
    - Both messages declared **`push pull`**, without `critical` (Rafael, 2026-10-05). The recorder's sender (PUSH) connects to the processing PC's receiver (PULL, binds), and ZeroMQ queues messages while the receiver is down. Anything lost across a restart is recovered from the sidecars (`mocap-extract` watch rescans them). `critical` would only be a bounded in-memory queue that drops the oldest message on overflow, and Java doesn't support it.
    - The compliance profile already declared (class_a, networked): no CURVE, no ZAP.
  - Delivers: the generated Python sender/receiver for both events (`new_sender`/`new_receiver`, USAGE §7.6), re-exported through `mocap_contracts` under stable names, so consumers never import `harpia_generated.zmq.<name>_<hash>_zmq`
- **Decisions (Claude, for Rafael's review, 2026-10-05):**
  - The ZeroMQ factories are re-exported from a **separate** generated module, `mocap_contracts/zmq_endpoints.py`, because importing them needs pyzmq and not every consumer does (the Blender add-on doesn't). pyzmq is an optional `zmq` extra, copied from the generated `pyproject.toml`.
  - The stable API is `mocap_contracts.transport.new_sender(cls, ctx, endpoint)` / `new_receiver(cls, ctx, endpoint)`.
  - Each sender stamps Harpia's origin id into the message's bookkeeping field. That field isn't declared, so it never reaches a JSON file.
- **Pre-work:** none
- **Out of scope:** copying the files (rsync, `mocap-capture` handoff); every other Harpia transport
- **Tests:** loopback send/receive of both messages; a message sent before the receiver binds arrives once it does (same sender process); `recv` with a timeout returns `None`
