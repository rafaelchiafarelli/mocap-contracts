"""ZeroMQ factories of every message declared with a ZeroMQ modifier.

Written by tools/harpia_gen.py (`make gen`); do not edit. Needs pyzmq
(`pip install mocap-contracts[zmq]`). Use mocap_contracts.transport."""

from types import ModuleType

from harpia_generated.zmq import CameraFileReady_acbcec83d1091de463df65590ca62e7d_zmq as _CameraFileReady
from harpia_generated.zmq import CameraStats_acbcec83d1091de463df65590ca62e7d_zmq as _CameraStats
from harpia_generated.zmq import ControlReply_acbcec83d1091de463df65590ca62e7d_zmq as _ControlReply
from harpia_generated.zmq import ControlRequest_acbcec83d1091de463df65590ca62e7d_zmq as _ControlRequest
from harpia_generated.zmq import TakeClosed_acbcec83d1091de463df65590ca62e7d_zmq as _TakeClosed

ENDPOINTS: dict[str, ModuleType] = {
    "CameraFileReady": _CameraFileReady,
    "CameraStats": _CameraStats,
    "ControlReply": _ControlReply,
    "ControlRequest": _ControlRequest,
    "TakeClosed": _TakeClosed,
}
