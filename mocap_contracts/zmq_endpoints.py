"""ZeroMQ factories of every message declared with a ZeroMQ modifier.

Written by tools/harpia_gen.py (`make gen`); do not edit. Needs pyzmq
(`pip install mocap-contracts[zmq]`). Use mocap_contracts.transport."""

from types import ModuleType

from harpia_generated.zmq import CameraFileReady_e51d6d03132b4baa0ced72cde01af9d0_zmq as _CameraFileReady
from harpia_generated.zmq import CameraStats_e51d6d03132b4baa0ced72cde01af9d0_zmq as _CameraStats
from harpia_generated.zmq import ControlReply_e51d6d03132b4baa0ced72cde01af9d0_zmq as _ControlReply
from harpia_generated.zmq import ControlRequest_e51d6d03132b4baa0ced72cde01af9d0_zmq as _ControlRequest
from harpia_generated.zmq import TakeClosed_e51d6d03132b4baa0ced72cde01af9d0_zmq as _TakeClosed

ENDPOINTS: dict[str, ModuleType] = {
    "CameraFileReady": _CameraFileReady,
    "CameraStats": _CameraStats,
    "ControlReply": _ControlReply,
    "ControlRequest": _ControlRequest,
    "TakeClosed": _TakeClosed,
}
