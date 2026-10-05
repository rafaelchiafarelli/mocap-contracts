## 3. Camera messages over Harpia ZeroMQ

- **Depends on:** 1; 2
- **Contract:**
  - In: `ControlRequest`/`ControlReply` (request → reply), `DeviceInfo` (on request), `CameraStats` (periodic, app → recorder)
  - Requires: the messages declared on Harpia's ZeroMQ transport (`push`/`pull`, `stream` for stats), under the compliance profile already declared (class_a, networked); Harpia used only through its documented interface
  - Delivers: generated Python (recorder) and Java/JeroMQ (app) endpoints for the camera messages, re-exported through `mocap_contracts` on the Python side
- **Pre-work:** **blocked** until Harpia documents ZeroMQ consumption for Python and Java (V4 USAGE §7.6 is C++ only). That's Harpia's backlog. Never work it out from Harpia's source.
- **Out of scope:** the video stream (stream-protocol)
- **Tests:** Python ↔ Java loopback: a control request gets its reply; stats arrive while a request is in flight
