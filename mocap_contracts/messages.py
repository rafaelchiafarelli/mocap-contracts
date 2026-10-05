"""Every contract message and enum, under its declared name.

Written by tools/harpia_gen.py (`make gen`); do not edit. Harpia's
module names carry a hash of the root .harpia file and change with it;
import from here (or from mocap_contracts) instead."""

from harpia_generated.protofiles.ControlBackend_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlBackend
from harpia_generated.protofiles.ControlCapability_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlCapability
from harpia_generated.protofiles.ControlMenuOption_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlMenuOption
from harpia_generated.protofiles.ControlResult_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlResult
from harpia_generated.protofiles.ControlSetting_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlSetting
from harpia_generated.protofiles.ControlStatus_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlStatus
from harpia_generated.protofiles.ControlValueType_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlValueType
from harpia_generated.protofiles.ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2 import ControlValue
from harpia_generated.protofiles.Flag_5f4d7690e05d3b2a18b01aae2e150601_pb2 import Flag

# Field names as declared in schema/ (Harpia's bookkeeping fields excluded).
DECLARED_FIELDS: dict[str, tuple[str, ...]] = {
    'ControlCapability': ('backend', 'key', 'value_type', 'min_value', 'max_value', 'step', 'options', 'default_value', 'current_value', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'applied', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': ('int_value', 'float_value', 'flag_value', 'text_value', 'int_values', 'float_values'),
}

# Fields declared `required` (proto3 doesn't keep it).
REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    'ControlCapability': ('backend', 'key', 'value_type', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': (),
}

__all__ = [
    "ControlBackend",
    "ControlCapability",
    "ControlMenuOption",
    "ControlResult",
    "ControlSetting",
    "ControlStatus",
    "ControlValue",
    "ControlValueType",
    "Flag",
]
