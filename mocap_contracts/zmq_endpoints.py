"""ZeroMQ factories of every message declared with a ZeroMQ modifier.

Written by tools/harpia_gen.py (`make gen`); do not edit. Needs pyzmq
(`pip install mocap-contracts[zmq]`). Use mocap_contracts.transport."""

from types import ModuleType

from harpia_generated.zmq import CameraFileReady_61c8c10158ef4d464aeae2ffe73974e6_zmq as _CameraFileReady
from harpia_generated.zmq import TakeClosed_61c8c10158ef4d464aeae2ffe73974e6_zmq as _TakeClosed

ENDPOINTS: dict[str, ModuleType] = {
    "CameraFileReady": _CameraFileReady,
    "TakeClosed": _TakeClosed,
}
