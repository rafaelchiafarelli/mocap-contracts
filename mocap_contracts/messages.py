"""Every contract message and enum, under its declared name.

Written by tools/harpia_gen.py (`make gen`); do not edit. Harpia's
module names carry a hash of the root .harpia file and change with it;
import from here (or from mocap_contracts) instead."""

from harpia_generated.protofiles.Actor_af98f0786af1eb31da6209cc006a6a92_pb2 import Actor
from harpia_generated.protofiles.BodyLength_af98f0786af1eb31da6209cc006a6a92_pb2 import BodyLength
from harpia_generated.protofiles.CalibrationBoard_af98f0786af1eb31da6209cc006a6a92_pb2 import CalibrationBoard
from harpia_generated.protofiles.CameraConfig_af98f0786af1eb31da6209cc006a6a92_pb2 import CameraConfig
from harpia_generated.protofiles.CameraSource_af98f0786af1eb31da6209cc006a6a92_pb2 import CameraSource
from harpia_generated.protofiles.Casting_af98f0786af1eb31da6209cc006a6a92_pb2 import Casting
from harpia_generated.protofiles.Character_af98f0786af1eb31da6209cc006a6a92_pb2 import Character
from harpia_generated.protofiles.ControlBackend_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlBackend
from harpia_generated.protofiles.ControlCapability_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlCapability
from harpia_generated.protofiles.ControlMenuOption_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlMenuOption
from harpia_generated.protofiles.ControlResult_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlResult
from harpia_generated.protofiles.ControlSetting_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlSetting
from harpia_generated.protofiles.ControlStatus_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlStatus
from harpia_generated.protofiles.ControlValueType_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlValueType
from harpia_generated.protofiles.ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2 import ControlValue
from harpia_generated.protofiles.Crop_af98f0786af1eb31da6209cc006a6a92_pb2 import Crop
from harpia_generated.protofiles.Flag_af98f0786af1eb31da6209cc006a6a92_pb2 import Flag
from harpia_generated.protofiles.PreprocessSpec_af98f0786af1eb31da6209cc006a6a92_pb2 import PreprocessSpec
from harpia_generated.protofiles.Session_af98f0786af1eb31da6209cc006a6a92_pb2 import Session
from harpia_generated.protofiles.TakeType_af98f0786af1eb31da6209cc006a6a92_pb2 import TakeType

# Field names as declared in schema/ (Harpia's bookkeeping fields excluded).
DECLARED_FIELDS: dict[str, tuple[str, ...]] = {
    'Actor': ('id', 'name', 'height_m', 'lengths'),
    'BodyLength': ('segment', 'length_m'),
    'CalibrationBoard': ('squares_x', 'squares_y', 'square_length_mm', 'marker_length_mm', 'aruco_dictionary', 'measured_square_length_mm'),
    'CameraConfig': ('role', 'source', 'width', 'height', 'fps', 'notes', 'preprocess', 'controls', 'device_hint', 'stream_host', 'video_port', 'sync_port', 'control_port', 'stats_port'),
    'Casting': ('actor_id', 'character_id'),
    'Character': ('id', 'name'),
    'ControlCapability': ('backend', 'key', 'value_type', 'min_value', 'max_value', 'step', 'options', 'default_value', 'current_value', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'applied', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': ('int_value', 'float_value', 'flag_value', 'text_value', 'int_values', 'float_values'),
    'Crop': ('x', 'y', 'width', 'height'),
    'PreprocessSpec': ('crop', 'output_width', 'output_height'),
    'Session': ('id', 'date', 'actors', 'characters', 'casting'),
}

# Fields declared `required` (proto3 doesn't keep it).
REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    'Actor': ('id', 'name', 'height_m'),
    'BodyLength': ('segment', 'length_m'),
    'CalibrationBoard': ('squares_x', 'squares_y', 'square_length_mm', 'marker_length_mm', 'aruco_dictionary', 'measured_square_length_mm'),
    'CameraConfig': ('role', 'source', 'width', 'height', 'fps', 'notes'),
    'Casting': ('actor_id', 'character_id'),
    'Character': ('id', 'name'),
    'ControlCapability': ('backend', 'key', 'value_type', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': (),
    'Crop': ('x', 'y', 'width', 'height'),
    'PreprocessSpec': ('output_width', 'output_height'),
    'Session': ('id', 'date'),
}

__all__ = [
    "Actor",
    "BodyLength",
    "CalibrationBoard",
    "CameraConfig",
    "CameraSource",
    "Casting",
    "Character",
    "ControlBackend",
    "ControlCapability",
    "ControlMenuOption",
    "ControlResult",
    "ControlSetting",
    "ControlStatus",
    "ControlValue",
    "ControlValueType",
    "Crop",
    "Flag",
    "PreprocessSpec",
    "Session",
    "TakeType",
]
