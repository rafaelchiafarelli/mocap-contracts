"""ZeroMQ factories of every message declared with a ZeroMQ modifier.

Written by tools/harpia_gen.py (`make gen`); do not edit. Needs pyzmq
(`pip install mocap-contracts[zmq]`). Use mocap_contracts.transport."""

from types import ModuleType

from harpia_generated.zmq import CameraFileReady_7656bad163803b596999eb3843b4995c_zmq as _CameraFileReady
from harpia_generated.zmq import CameraStats_7656bad163803b596999eb3843b4995c_zmq as _CameraStats
from harpia_generated.zmq import ControlReply_7656bad163803b596999eb3843b4995c_zmq as _ControlReply
from harpia_generated.zmq import ControlRequest_7656bad163803b596999eb3843b4995c_zmq as _ControlRequest
from harpia_generated.zmq import TakeClosed_7656bad163803b596999eb3843b4995c_zmq as _TakeClosed

ENDPOINTS: dict[str, ModuleType] = {
    "CameraFileReady": _CameraFileReady,
    "CameraStats": _CameraStats,
    "ControlReply": _ControlReply,
    "ControlRequest": _ControlRequest,
    "TakeClosed": _TakeClosed,
}
