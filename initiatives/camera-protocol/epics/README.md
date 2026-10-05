# camera-protocol — epics (execution order)

1. **stream-protocol** — Video stream + clock sync wire format v1, spec and fixtures (2 tasks)
2. **camera-messages** — `camera.harpia`, Java generation, ZeroMQ channel, release v0.2.0 (4 tasks)

The two epics are independent; stream-protocol is what `mocap-capture` devices/5 needs first.
An epic only merges up into `epics` once all its tasks are `-done` and the suite is green.
