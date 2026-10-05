# Stream protocol v1

How a STREAM camera (`mocap-camera-app`) delivers video to the recorder
(`mocap-capture`). It describes exactly what the evaluation app in
`mocap-studio/camera-stream-eval` does today, so devices measured with it are
measured on the real protocol. Camera control, device info and stats are
**not** part of this protocol: they are `camera.harpia` messages over Harpia
ZeroMQ.

The reference reader is `mocap_contracts.stream_v1` (stdlib only). Every
receiver tests against it and against the fixtures in `fixtures/stream-v1/`.

## 1. Ports

Both are declared per camera in the recorder's `config.yaml`
(`CameraConfig.video_port`, `CameraConfig.sync_port`), never discovered. The
evaluation app uses 8080 and 8081.

| Port | Transport | What |
|---|---|---|
| `video_port` | TCP, HTTP/1.0 | the video stream (§2) |
| `sync_port` | UDP | the clock sync (§4) |

## 2. Video transport

The receiver sends `GET /h264.raw HTTP/1.0`. The camera answers:

```
HTTP/1.0 200 OK
Content-Type: video/h264
Cache-Control: no-cache
Connection: close

<H.264 Annex-B elementary stream until either side closes>
```

- The body is a raw H.264 **Annex-B** byte stream. NAL units are separated by
  start codes (`00 00 00 01`, or `00 00 01`; receivers accept both).
- It starts with the **codec configuration** (SPS, NAL type 7, then PPS, type
  8) and then **access units starting at a key frame**. The camera holds back
  frames until a key frame, so the receiver can decode from its first frame.
- **Every access unit is the timestamp SEI (§3) followed by the encoder's NAL
  units for that frame** (an IDR slice, type 5, or a non-IDR slice, type 1).
  The SEI is what identifies a frame, so a frame without one is untimed and is
  reported, never guessed.
- **Frames can be skipped** when a receiver reads too slowly: the camera
  serves the latest frame and never queues. A skip shows up as a jump in the
  SEI sequence number. After a skip the camera resumes at the next key frame,
  because the reference chain is broken. Receivers report every jump as a gap.
- The multipart `/stream` endpoint of the evaluation app is **not** part of
  v1.

## 3. Timestamp SEI

One SEI NAL unit (`nal_unit_type` 6) per frame, placed before the frame's
slice:

| Bytes (RBSP, after removing emulation prevention) | Value |
|---|---|
| 1 | `0x05`: payloadType 5, `user_data_unregistered` |
| 1 | `0x28`: payloadSize 40 |
| 16 | UUID, ASCII `MOCAPSTUDIO-TS01` (this is what makes it protocol v1) |
| 8 | `seq`: unsigned, big-endian. Starts at 1 and is +1 for every encoded frame. |
| 8 | `sensor_ns`: unsigned, big-endian. The frame's capture time on the device's **sensor clock** (Camera2 `SENSOR_TIMESTAMP`, which is boottime or monotonic per device). |
| 8 | `device_unix_ns`: unsigned, big-endian. `sensor_ns` plus the device's wall-clock offset at encode time. **Informational only**: the device's wall clock is synced to nothing, so it must never be used for alignment. |
| 1 | `0x80`: rbsp trailing bits |

The NAL unit is the header byte `0x06` followed by the RBSP, with H.264
emulation prevention applied (an `0x03` is inserted after any two zero bytes
that are followed by a byte ≤ `0x03`).

All values fit in 63 bits, since the sender writes Java `long`s.

A receiver **ignores SEIs with any other UUID**, which is how a future v2 can
coexist with v1. It **reports** an SEI with this UUID but a wrong
payloadType/size or a truncated payload as garbled, and never reads values out
of it.

## 4. Clock sync

NTP-style probes over UDP to `sync_port`. The device answers each one
immediately, on the same sensor clock as the SEI `sensor_ns`.

| Direction | Bytes | Content |
|---|---|---|
| request | ≥ 8 | the first 8 bytes are an opaque **token** chosen by the receiver (the evaluation scripts use the probe index, big-endian). Only those 8 bytes are read. |
| reply | 24 | `token` (8, echoed) + `sensor_ns` (8, u64 BE, sensor clock when the request arrived) + `device_unix_ns` (8, u64 BE, informational, as in §3) |

## 5. Timing model

The goal is to put every frame on the **recorder's host clock**: Unix time in
ns (`CLOCK_REALTIME`), the same clock UVC cameras are stamped with.

1. **One sync** sends N probes (the evaluation uses 200, 10 ms apart). For
   each reply, `rtt = t_recv − t_send` on the host, and
   `offset = (t_send_unix + rtt / 2) − sensor_ns`. Keep the fastest 10% of
   round trips (at least 3), and the sync's offset is the **median** of
   their offsets.
2. **Before and after every take**, run a sync: `(t_before, offset_before)`
   and `(t_after, offset_after)`, each `t` taken on the host clock.
3. Each frame's host time is `host_ts_ns = sensor_ns + offset(sensor_ns)`, where
   `offset` is **interpolated linearly** between the two syncs over the sensor
   clock. That removes the device's clock drift, about −20 ppm on the first
   tablets measured.
4. A sanity check: capture→host latency is never negative.

`mocap_contracts.stream_v1` implements steps 1 and 3. Steps 2 and 4 are the
receiver's job.

## 6. Versioning

The SEI UUID carries the version (`…-TS01`). Any change to §2–§4 is a new
version with a new UUID, written as a new spec next to this one, with its own
fixtures. A receiver may support several versions; a camera speaks exactly
one.
