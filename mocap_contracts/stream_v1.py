"""Reference reader for stream protocol v1 (docs/stream-protocol-v1.md).

Stdlib only. Every STREAM receiver tests against this module and against
fixtures/stream-v1/. The writers (`build_timestamp_sei`, `sync_reply`) mirror
the camera side byte for byte, for tests and fixtures.
"""

from __future__ import annotations

import statistics
import struct
from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field

UUID = b"MOCAPSTUDIO-TS01"
SEI_PAYLOAD_TYPE = 5
SEI_PAYLOAD_SIZE = 40
NAL_SEI = 6
NAL_IDR = 5
NAL_SLICE = 1
NAL_SPS = 7
NAL_PPS = 8
SYNC_REPLY_SIZE = 24


class StreamError(ValueError):
    """Bytes that claim to be protocol v1 but can't be read as such."""


@dataclass(frozen=True)
class Timestamp:
    seq: int
    sensor_ns: int
    device_unix_ns: int  # informational only, never used for alignment


@dataclass
class Frame:
    """One access unit: its timestamp (None if it had no v1 SEI) and NAL types."""

    timestamp: Timestamp | None
    nal_types: list[int] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- NAL units

def nal_units(data: bytes) -> Iterator[tuple[int, bytes]]:
    """Yield (nal_unit_type, nal bytes without start code) from an Annex-B stream."""
    i = data.find(b"\x00\x00\x01")
    while i >= 0:
        start = i + 3
        nxt = data.find(b"\x00\x00\x01", start)
        end = len(data) if nxt < 0 else nxt
        # a 4-byte start code leaves one zero byte at the end of the previous unit
        nal = data[start:end]
        if nxt >= 0 and nal.endswith(b"\x00"):
            nal = nal[:-1]
        if nal:
            yield nal[0] & 0x1F, nal
        i = nxt


def unescape(payload: bytes) -> bytes:
    """Remove H.264 emulation prevention bytes (00 00 03 → 00 00)."""
    out, zeros = bytearray(), 0
    for v in payload:
        if zeros >= 2 and v == 3:
            zeros = 0
            continue
        out.append(v)
        zeros = zeros + 1 if v == 0 else 0
    return bytes(out)


def escape(rbsp: bytes) -> bytes:
    """Apply H.264 emulation prevention, as the camera does."""
    out, zeros = bytearray(), 0
    for v in rbsp:
        if zeros >= 2 and v <= 3:
            out.append(3)
            zeros = 0
        out.append(v)
        zeros = zeros + 1 if v == 0 else 0
    return bytes(out)


# ---------------------------------------------------------------- timestamp SEI

def build_timestamp_sei(seq: int, sensor_ns: int, device_unix_ns: int) -> bytes:
    """The timestamp SEI NAL unit with its 4-byte start code (mirror of TimestampSei.java)."""
    rbsp = bytes([SEI_PAYLOAD_TYPE, SEI_PAYLOAD_SIZE]) + UUID
    rbsp += struct.pack(">QQQ", seq, sensor_ns, device_unix_ns) + b"\x80"
    return b"\x00\x00\x00\x01" + bytes([NAL_SEI]) + escape(rbsp)


def parse_timestamp_sei(nal: bytes) -> Timestamp | None:
    """The v1 timestamp in an SEI NAL unit (without start code).

    None for any SEI that isn't v1 (other payload or UUID). StreamError for a
    v1 SEI that is garbled, so a broken one is never misread as a value.
    """
    if not nal or nal[0] & 0x1F != NAL_SEI:
        return None
    rbsp = unescape(nal[1:])
    if len(rbsp) < 18 or rbsp[2:18] != UUID:
        return None
    if rbsp[0] != SEI_PAYLOAD_TYPE or rbsp[1] != SEI_PAYLOAD_SIZE:
        raise StreamError(f"v1 SEI with payloadType {rbsp[0]} / payloadSize {rbsp[1]}, expected 5 / 40")
    if len(rbsp) < 2 + SEI_PAYLOAD_SIZE:
        raise StreamError(f"truncated v1 SEI: {len(rbsp) - 2} payload bytes, expected 40")
    seq, sensor_ns, unix_ns = struct.unpack(">QQQ", rbsp[18:42])
    return Timestamp(seq, sensor_ns, unix_ns)


def frames(data: bytes) -> list[Frame]:
    """Split a v1 stream into access units, each opened by its timestamp SEI.

    Units before the first frame (SPS, PPS, SEIs of other UUIDs) belong to no frame.
    A slice that arrives without a preceding v1 SEI makes an untimed frame
    with a problem noted; a garbled SEI does too.
    """
    out: list[Frame] = []
    current: Frame | None = None
    for nal_type, nal in nal_units(data):
        if nal_type == NAL_SEI:
            try:
                ts = parse_timestamp_sei(nal)
            except StreamError as e:
                current = Frame(None, [nal_type], [str(e)])
                out.append(current)
                continue
            if ts is not None:
                current = Frame(ts, [nal_type])
                out.append(current)
                continue
        if nal_type in (NAL_IDR, NAL_SLICE):
            if current is None or _has_slice(current):
                current = Frame(None, [], ["slice without a v1 timestamp SEI"])
                out.append(current)
        elif current is None:
            continue  # stream-level units before the first frame: SPS, PPS, other SEIs
        current.nal_types.append(nal_type)
    return out


def _has_slice(frame: Frame) -> bool:
    return any(t in (NAL_IDR, NAL_SLICE) for t in frame.nal_types)


def seq_gaps(timestamps: Sequence[Timestamp]) -> list[tuple[int, int]]:
    """(last seq before, first seq after) for every jump in the sequence."""
    return [(a.seq, b.seq) for a, b in zip(timestamps, timestamps[1:]) if b.seq != a.seq + 1]


# ---------------------------------------------------------------- clock sync

def sync_request(token: int) -> bytes:
    """An 8-byte probe; the token comes back in the reply."""
    return struct.pack(">Q", token)


def sync_reply(token: int, sensor_ns: int, device_unix_ns: int) -> bytes:
    """The camera's 24-byte reply (mirror of TimeSyncServer.java)."""
    return struct.pack(">QQQ", token, sensor_ns, device_unix_ns)


def parse_sync_reply(data: bytes) -> tuple[int, int, int]:
    """(token, sensor_ns, device_unix_ns) from a reply; StreamError if it's short."""
    if len(data) < SYNC_REPLY_SIZE:
        raise StreamError(f"sync reply of {len(data)} bytes, expected {SYNC_REPLY_SIZE}")
    return struct.unpack(">QQQ", data[:SYNC_REPLY_SIZE])


@dataclass(frozen=True)
class Probe:
    """One answered probe, timed on the host clock (Unix ns)."""

    t_send_ns: int
    t_recv_ns: int
    sensor_ns: int

    @property
    def rtt_ns(self) -> int:
        return self.t_recv_ns - self.t_send_ns

    @property
    def offset_ns(self) -> int:
        return self.t_send_ns + self.rtt_ns // 2 - self.sensor_ns


def sync_offset(probes: Sequence[Probe]) -> int:
    """Host-minus-sensor offset of one sync: median over the fastest 10% (at least 3)."""
    if len(probes) < 3:
        raise StreamError(f"a sync needs at least 3 answered probes, got {len(probes)}")
    fastest = sorted(probes, key=lambda p: p.rtt_ns)[: max(3, len(probes) // 10)]
    return int(statistics.median(p.offset_ns for p in fastest))


def host_ts_ns(sensor_ns: int, before: tuple[int, int], after: tuple[int, int]) -> int:
    """A frame's time on the host clock, with the offset interpolated linearly
    over the sensor clock between the syncs before and after the take.

    `before` and `after` are (sensor_ns at the sync, offset_ns of the sync).
    """
    (s0, o0), (s1, o1) = before, after
    if s1 == s0:
        return sensor_ns + o0
    return sensor_ns + o0 + round((o1 - o0) * (sensor_ns - s0) / (s1 - s0))
