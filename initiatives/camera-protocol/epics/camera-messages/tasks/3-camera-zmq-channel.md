## 3. Camera messages over Harpia ZeroMQ

- **Depends on:** 1; 2
- **Contract:**
  - In: `ControlRequest`/`ControlReply` (request → reply), `DeviceInfo` (on request), `CameraStats` (periodic, app → recorder)
  - Requires: Harpia ≥ V5 (USAGE §7.6). There's no request/reply pattern, so the channel is:
    - `ControlRequest` `push pull`: each app binds a receiver (PULL) on its declared port, and the recorder's sender connects to each app.
    - `ControlReply` `push pull`: the recorder binds one receiver, and every app's sender connects to it. Replies are matched by request_id + device serial.
    - `CameraStats` `event` (pub/sub): each app publishes (PUB, binds), and the recorder subscribes to each. Not `stream`: Java has no stream lifecycle class.
    - `DeviceInfo`: sent as the reply to a `ControlRequest` that asks for it, so there's no extra socket.
    - No `critical` (Java doesn't support it). The compliance profile already declared (class_a, networked) means no CURVE.
  - Delivers: generated Python (recorder) and Java/JeroMQ (app) endpoints for the camera messages, re-exported through `mocap_contracts` on the Python side
- **Pre-work:** none (Harpia V5 documents both sides). Ports and which side binds go in the recorder's `config.yaml` per STREAM camera; they're never discovered.
- **Out of scope:** the video stream (stream-protocol)
- **Tests:** Python ↔ Java loopback: a control request gets its reply; stats arrive while a request is in flight
