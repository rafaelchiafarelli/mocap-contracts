# camera-protocol — mocap-contracts

**Goal:** The contract between the tablet camera app (`mocap-camera-app`) and the recorder (`mocap-capture` STREAM source): the video stream wire format, the clock sync exchange, and the control/info/status messages.

**Scope:**
- **Stream protocol v1**, a written spec plus small binary fixtures. It covers the H.264 stream, the capture-time SEI on every frame and the UDP clock sync. These are binary formats Harpia can't express, so they're a spec, not `.harpia`.
- **`camera.harpia`** (owner: `mocap-camera-app`): device info, stats, control request, applied controls.
- **Java generation** of the contracts, for the app.
- **Harpia ZeroMQ** as the channel for the camera messages (Rafael, 2026-10-05): push/pull legs plus pub/sub for stats, since Harpia has no request/reply pattern.

**Out of scope:** the app itself (`mocap-camera-app`); the recorder side (`mocap-capture` devices/5); live preview (`mocap-capture` live-monitor).

**Initiative gate:** the fixtures parse identically with the spec's reference reader; `camera.harpia` messages round-trip in Python and Java; a control request and its applied-controls reply cross a ZeroMQ loopback Python ↔ Java.

Harpia V5 documents ZeroMQ for Python and Java (USAGE §7.6), so nothing in this initiative is blocked on Harpia.

General context, cross-repository order and open questions:
`mocap-studio/HANDOFF.md`.
