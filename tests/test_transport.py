"""messages-v0/7: the hand-off events over Harpia ZeroMQ (push/pull)."""

import socket

import pytest
from samples import file_ready, take_closed

zmq = pytest.importorskip("zmq")

import mocap_contracts as mc  # noqa: E402
from mocap_contracts import ContractError, transport  # noqa: E402


def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture
def ctx():
    c = zmq.Context()
    yield c
    c.destroy(linger=0)


def _pair(cls, ctx, port):
    rx = transport.new_receiver(cls, ctx, f"tcp://127.0.0.1:{port}")
    rx.socket.rcvtimeo = 2000
    tx = transport.new_sender(cls, ctx, f"tcp://127.0.0.1:{port}")
    return tx, rx


@pytest.mark.parametrize("cls, sample", [(mc.TakeClosed, take_closed), (mc.CameraFileReady, file_ready)])
def test_loopback(ctx, cls, sample):
    tx, rx = _pair(cls, ctx, _free_port())
    msg = sample()
    assert tx.send(msg)
    got = rx.recv()
    assert isinstance(got, cls)
    for field in mc.messages.DECLARED_FIELDS[cls.DESCRIPTOR.name]:
        assert getattr(got, field) == getattr(msg, field), field
    tx.close(); rx.close()


def test_received_event_is_still_a_valid_contract(ctx):
    tx, rx = _pair(mc.CameraFileReady, ctx, _free_port())
    tx.send(file_ready())
    got = rx.recv()
    assert mc.from_json(mc.CameraFileReady, mc.to_json(got)) == mc.from_json(mc.CameraFileReady, mc.to_json(file_ready()))
    tx.close(); rx.close()


def test_sent_before_the_receiver_binds_arrives_once_it_does(ctx):
    port = _free_port()
    tx = transport.new_sender(mc.TakeClosed, ctx, f"tcp://127.0.0.1:{port}")
    assert tx.send(take_closed(take_id="early"))       # nobody listening yet: ZeroMQ queues it
    rx = transport.new_receiver(mc.TakeClosed, ctx, f"tcp://127.0.0.1:{port}")
    rx.socket.rcvtimeo = 5000
    got = rx.recv()
    assert got is not None and got.take_id == "early"
    tx.close(); rx.close()


def test_recv_with_timeout_returns_none(ctx):
    rx = transport.new_receiver(mc.TakeClosed, ctx, f"tcp://127.0.0.1:{_free_port()}")
    rx.socket.rcvtimeo = 100
    assert rx.recv() is None
    rx.close()


def test_message_without_zmq_transport_is_refused(ctx):
    with pytest.raises(ContractError, match="has no ZeroMQ transport"):
        transport.new_sender(mc.Session, ctx, "tcp://127.0.0.1:1")


def test_stats_publish_subscribe(ctx):
    import time

    from samples import camera_stats

    port = _free_port()
    pub = transport.new_publisher(mc.CameraStats, ctx, f"tcp://127.0.0.1:{port}")
    sub = transport.new_subscriber(mc.CameraStats, ctx, f"tcp://127.0.0.1:{port}")
    sub.socket.rcvtimeo = 200
    got = None
    for _ in range(25):  # a subscriber misses what was published before it connected
        pub.send(camera_stats())
        if (got := sub.recv()) is not None:
            break
        time.sleep(0.02)
    assert got is not None and got.serial == "200138"
    pub.close(); sub.close()


def test_control_request_reply_legs_are_push_pull(ctx):
    from samples import control_reply, control_request

    for cls, sample in ((mc.ControlRequest, control_request), (mc.ControlReply, control_reply)):
        tx, rx = _pair(cls, ctx, _free_port())
        assert tx.send(sample())
        assert rx.recv().request_id == "r-17"
        tx.close(); rx.close()
