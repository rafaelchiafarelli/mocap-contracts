## 7. Hand-off event transport (Harpia ZeroMQ)

- **Depends on:** 3; bootstrap/2
- **Contract:**
  - In: `TakeClosed`, `CameraFileReady` (task 3)
  - Requires:
    - Harpia submodule bumped from `V4` to **`V5`**. V5 is V4 plus the docs for ZeroMQ in Python and Java (USAGE §7.6, §7.7, §7.9, §11); the generated code is the same, and `make check-gen` proves it.
    - Both messages declared **`push pull`**, without `critical` (Rafael, 2026-10-05). The recorder's sender (PUSH) connects to the processing PC's receiver (PULL, binds), and ZeroMQ queues messages while the receiver is down. Anything lost across a restart is recovered from the sidecars (`mocap-extract` watch rescans them). `critical` would only be a bounded in-memory queue that drops the oldest message on overflow, and Java doesn't support it.
    - The compliance profile already declared (class_a, networked): no CURVE, no ZAP.
  - Delivers: the generated Python sender/receiver for both events (`new_sender`/`new_receiver`, USAGE §7.6), re-exported through `mocap_contracts` under stable names, so consumers never import `harpia_generated.zmq.<name>_<hash>_zmq`
- **Pre-work:** none
- **Out of scope:** copying the files (rsync, `mocap-capture` handoff); every other Harpia transport
- **Tests:** loopback send/receive of both messages; a message sent before the receiver binds arrives once it does (same sender process); `recv` with a timeout returns `None`
