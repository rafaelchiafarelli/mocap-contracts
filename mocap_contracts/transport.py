"""ZeroMQ endpoints for contract messages, under stable names.

Wraps Harpia's generated factories (USAGE §7.6) so consumers never import
`harpia_generated.zmq.<name>_<hash>_zmq`. Needs pyzmq: install
`mocap-contracts[zmq]`.

    import zmq
    from mocap_contracts import TakeClosed, transport

    ctx = zmq.Context()
    rx = transport.new_receiver(TakeClosed, ctx, "tcp://*:5600")         # PULL, binds
    tx = transport.new_sender(TakeClosed, ctx, "tcp://processing:5600")  # PUSH, connects
    tx.send(msg)                       # True when queued; ZeroMQ queues while the receiver is down
    rx.socket.rcvtimeo = 1000          # ms; without it recv() blocks
    got = rx.recv()                    # the message, or None on timeout or an unparsable frame

push/pull messages (TakeClosed, CameraFileReady, ControlRequest, ControlReply)
use new_sender/new_receiver. pub/sub messages (CameraStats) use
new_publisher (binds) / new_subscriber (connects; it misses whatever was
published before it connected, as with any ZeroMQ subscriber).
"""

from __future__ import annotations

from types import ModuleType
from typing import Any

from mocap_contracts.errors import ContractError
from mocap_contracts.zmq_endpoints import ENDPOINTS


def _factories(message_cls: type) -> ModuleType:
    try:
        return ENDPOINTS[message_cls.DESCRIPTOR.name]
    except (KeyError, AttributeError):
        raise ContractError(
            f"{getattr(message_cls, '__name__', message_cls)} has no ZeroMQ transport; "
            f"messages with one: {sorted(ENDPOINTS)}"
        ) from None


def new_sender(message_cls: type, ctx: Any, endpoint: str, origin: str | None = None) -> Any:
    """PUSH socket that connects to `endpoint` and sends `message_cls` messages."""
    return _factories(message_cls).new_sender(ctx, endpoint, origin=origin)


def new_receiver(message_cls: type, ctx: Any, endpoint: str) -> Any:
    """PULL socket that binds `endpoint` and receives `message_cls` messages."""
    return _factories(message_cls).new_receiver(ctx, endpoint)


def new_publisher(message_cls: type, ctx: Any, endpoint: str, origin: str | None = None) -> Any:
    """PUB socket that binds `endpoint` and publishes `message_cls` messages (`.send(msg)`)."""
    return _factories(message_cls).new_publisher(ctx, endpoint, origin=origin)


def new_subscriber(message_cls: type, ctx: Any, endpoint: str) -> Any:
    """SUB socket that connects to `endpoint` and receives every `message_cls` message."""
    return _factories(message_cls).new_subscriber(ctx, endpoint)
