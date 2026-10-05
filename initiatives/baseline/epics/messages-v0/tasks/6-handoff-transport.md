## 6. Hand-off event transport (Harpia ZeroMQ)

- **Depends on:** 2; bootstrap/2
- **Contract:**
  - In: `TakeClosed`, `CameraFileReady` (task 2)
  - Requires:
    - The `.harpia` declares both messages on Harpia's **ZeroMQ** transport, as `critical` messages (delivery guarantees), so a readiness event isn't silently dropped. Harpia's "events" are in-process only, so they can't cross PCs.
    - A **compliance profile** (`project.harpia.yaml`) declared in this repo for a closed studio LAN. Its values are Rafael's call and are written down, never left to Harpia's defaults (which turn on mTLS/CURVE/RBAC at higher risk classes).
    - Harpia stays a black box: only its documented interface (`USAGE.md` §4, §7.6, §7.9) is used.
  - Delivers: generated Python sender/receiver for the two events, re-exported through `mocap_contracts` (consumers never import Harpia's package names)
- **Pre-work:**
  - Harpia documents its **Python** ZeroMQ transport and `critical` delivery (V3's `USAGE.md` documents only the C++ ones). That's Harpia's backlog. Never work it out from Harpia's source.
  - Rafael sets the compliance profile values.
- **Out of scope:** copying the files (rsync, `mocap-capture` handoff); every other Harpia transport
- **Tests:** loopback send/receive of both messages; an event sent while the receiver is down arrives once it starts
