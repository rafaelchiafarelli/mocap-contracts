"""camera-protocol camera-messages/2-3: the generated Java (gen/java). Slow.

The Java peer below plays the camera app with nothing but the generated
messages and ZeroMQ factories: it binds its ControlRequest receiver, answers
on the recorder's ControlReply receiver, and publishes CameraStats. The test
plays the recorder in Python with mocap_contracts.transport.
"""

import socket
import subprocess
import threading
import time

import pytest
from java_harness import SKIP_REASON, SLOW, docker_ok, gradle, gradle_cmd, stage_java

pytestmark = pytest.mark.skipif(not (SLOW and docker_ok()), reason=SKIP_REASON)

PEER = r"""
package mocap;

import com.harpia.generated.*;
import com.harpia.generated.zmq.*;
import com.harpia.runtime.zmq.HarpiaZmq;
import org.zeromq.ZContext;

/** Plays the camera app: one ControlRequest in, its ControlReply out, then stats. */
public final class CameraPeer {
    public static void main(String[] args) throws Exception {
        String req = args[0], reply = args[1], stats = args[2];
        try (ZContext ctx = new ZContext()) {
            HarpiaZmq.Receiver rx = ControlRequest_zmq.newReceiver(ctx, "tcp://127.0.0.1:" + req);
            HarpiaZmq.Sender tx = ControlReply_zmq.newSender(ctx, "tcp://127.0.0.1:" + reply);
            HarpiaZmq.Sender pub = CameraStats_zmq.newPublisher(ctx, "tcp://127.0.0.1:" + stats);
            rx.socket().setReceiveTimeOut(60000);
            System.out.println("READY");
            System.out.flush();
            ControlRequest.Builder in = ControlRequest.newBuilder();
            if (!rx.receive(in)) { System.out.println("NO_REQUEST"); System.exit(2); }
            ControlRequest r = in.build();
            ControlReply.Builder out = ControlReply.newBuilder()
                .setRequestId(r.getRequestId()).setSerial(r.getSerial());
            for (ControlSetting s : r.getSettingsList()) {
                boolean unsupported = s.getKey().equals("android.sensor.exposureTime");
                ControlResult.Builder res = ControlResult.newBuilder().setKey(s.getKey()).setRequested(s.getValue())
                    .setStatus(unsupported ? ControlStatus.CONTROL_STATUS_UNSUPPORTED : ControlStatus.CONTROL_STATUS_APPLIED)
                    .setNote(unsupported ? "LIMITED device without MANUAL_SENSOR" : "");
                if (!unsupported) res.setApplied(s.getValue());
                out.addResults(res);
            }
            tx.send(out.build());
            for (int i = 0; i < 50; i++) {
                pub.send(CameraStats.newBuilder().setSerial(r.getSerial()).setSensorNs(1_000_000L * i)
                    .setCameraFps(29.9f).setEncoderFps(29.9f).setDroppedFrames(0).setCpuPercent(40f)
                    .setBatteryTempC(35.5f).setThermalStatus(0).build());
                Thread.sleep(100);
            }
            tx.socket().setLinger(1000);
            System.out.println("DONE");
        }
    }
}
"""

TASK = """

// added by tests/test_java.py (staged copy only): run the camera peer
tasks.register('peer', JavaExec) {
    classpath = sourceSets.main.runtimeClasspath
    mainClass = 'mocap.CameraPeer'
    args = (project.findProperty('peerArgs') ?: '').tokenize(',')
}
"""


def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def test_generated_java_project_builds():
    java = stage_java()
    r = gradle("build")
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert list((java / "build" / "libs").glob("*.jar"))


def test_python_recorder_and_java_camera_talk_over_zeromq():
    zmq = pytest.importorskip("zmq")
    from samples import control_request

    import mocap_contracts as mc
    from mocap_contracts import transport

    java = stage_java({"src/main/java/mocap/CameraPeer.java": PEER})
    (java / "build.gradle").write_text((java / "build.gradle").read_text() + TASK)
    assert gradle("compileJava").returncode == 0

    req_port, reply_port, stats_port = _free_port(), _free_port(), _free_port()
    ctx = zmq.Context()
    replies = transport.new_receiver(mc.ControlReply, ctx, f"tcp://127.0.0.1:{reply_port}")  # recorder binds
    replies.socket.rcvtimeo = 30000
    peer = subprocess.Popen(gradle_cmd(f"peer -PpeerArgs={req_port},{reply_port},{stats_port}"),
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines: list[str] = []
    threading.Thread(target=lambda: lines.extend(peer.stdout), daemon=True).start()
    try:
        deadline = time.time() + 120
        while "READY\n" not in lines:
            assert time.time() < deadline and peer.poll() is None, "".join(lines)[-3000:]
            time.sleep(0.2)

        stats = transport.new_subscriber(mc.CameraStats, ctx, f"tcp://127.0.0.1:{stats_port}")
        stats.socket.rcvtimeo = 30000
        sender = transport.new_sender(mc.ControlRequest, ctx, f"tcp://127.0.0.1:{req_port}")
        request = control_request()
        assert sender.send(request)

        reply = replies.recv()
        assert reply is not None, "".join(lines)[-3000:]
        assert (reply.request_id, reply.serial) == (request.request_id, request.serial)
        statuses = {r.key: mc.ControlStatus.Name(r.status) for r in reply.results}
        assert statuses == {"android.control.aeMode": "CONTROL_STATUS_APPLIED",
                            "android.sensor.exposureTime": "CONTROL_STATUS_UNSUPPORTED"}
        # what Java sent is a valid contract on the Python side
        assert mc.from_json(mc.ControlReply, mc.to_json(reply)).request_id == "r-17"

        got = stats.recv()
        assert got is not None and got.serial == "200138" and got.thermal_status == 0
        assert peer.wait(timeout=60) == 0, "".join(lines)[-3000:]
    finally:
        if peer.poll() is None:
            peer.kill()
        ctx.destroy(linger=0)
