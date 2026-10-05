"""Every contract message and enum, under its declared name.

Written by tools/harpia_gen.py (`make gen`); do not edit. Harpia's
module names carry a hash of the root .harpia file and change with it;
import from here (or from mocap_contracts) instead."""

from harpia_generated.protofiles.Actor_17f8b54225d6d535e6d691175cc18809_pb2 import Actor
from harpia_generated.protofiles.BodyLength_17f8b54225d6d535e6d691175cc18809_pb2 import BodyLength
from harpia_generated.protofiles.CalibrationBoard_17f8b54225d6d535e6d691175cc18809_pb2 import CalibrationBoard
from harpia_generated.protofiles.CameraConfig_17f8b54225d6d535e6d691175cc18809_pb2 import CameraConfig
from harpia_generated.protofiles.CameraControls_17f8b54225d6d535e6d691175cc18809_pb2 import CameraControls
from harpia_generated.protofiles.CameraFileReady_17f8b54225d6d535e6d691175cc18809_pb2 import CameraFileReady
from harpia_generated.protofiles.CameraSource_17f8b54225d6d535e6d691175cc18809_pb2 import CameraSource
from harpia_generated.protofiles.CameraTakeReport_17f8b54225d6d535e6d691175cc18809_pb2 import CameraTakeReport
from harpia_generated.protofiles.Casting_17f8b54225d6d535e6d691175cc18809_pb2 import Casting
from harpia_generated.protofiles.Character_17f8b54225d6d535e6d691175cc18809_pb2 import Character
from harpia_generated.protofiles.ControlBackend_17f8b54225d6d535e6d691175cc18809_pb2 import ControlBackend
from harpia_generated.protofiles.ControlCapability_17f8b54225d6d535e6d691175cc18809_pb2 import ControlCapability
from harpia_generated.protofiles.ControlMenuOption_17f8b54225d6d535e6d691175cc18809_pb2 import ControlMenuOption
from harpia_generated.protofiles.ControlResult_17f8b54225d6d535e6d691175cc18809_pb2 import ControlResult
from harpia_generated.protofiles.ControlSetting_17f8b54225d6d535e6d691175cc18809_pb2 import ControlSetting
from harpia_generated.protofiles.ControlStatus_17f8b54225d6d535e6d691175cc18809_pb2 import ControlStatus
from harpia_generated.protofiles.ControlValueType_17f8b54225d6d535e6d691175cc18809_pb2 import ControlValueType
from harpia_generated.protofiles.ControlValue_17f8b54225d6d535e6d691175cc18809_pb2 import ControlValue
from harpia_generated.protofiles.Crop_17f8b54225d6d535e6d691175cc18809_pb2 import Crop
from harpia_generated.protofiles.FileKind_17f8b54225d6d535e6d691175cc18809_pb2 import FileKind
from harpia_generated.protofiles.Flag_17f8b54225d6d535e6d691175cc18809_pb2 import Flag
from harpia_generated.protofiles.FrameGap_17f8b54225d6d535e6d691175cc18809_pb2 import FrameGap
from harpia_generated.protofiles.PreprocessSpec_17f8b54225d6d535e6d691175cc18809_pb2 import PreprocessSpec
from harpia_generated.protofiles.Session_17f8b54225d6d535e6d691175cc18809_pb2 import Session
from harpia_generated.protofiles.SyncEvent_17f8b54225d6d535e6d691175cc18809_pb2 import SyncEvent
from harpia_generated.protofiles.SyncKind_17f8b54225d6d535e6d691175cc18809_pb2 import SyncKind
from harpia_generated.protofiles.SyncSource_17f8b54225d6d535e6d691175cc18809_pb2 import SyncSource
from harpia_generated.protofiles.TakeCamera_17f8b54225d6d535e6d691175cc18809_pb2 import TakeCamera
from harpia_generated.protofiles.TakeClosed_17f8b54225d6d535e6d691175cc18809_pb2 import TakeClosed
from harpia_generated.protofiles.TakeReport_17f8b54225d6d535e6d691175cc18809_pb2 import TakeReport
from harpia_generated.protofiles.TakeType_17f8b54225d6d535e6d691175cc18809_pb2 import TakeType
from harpia_generated.protofiles.Take_17f8b54225d6d535e6d691175cc18809_pb2 import Take

# Field names as declared in schema/ (Harpia's bookkeeping fields excluded).
DECLARED_FIELDS: dict[str, tuple[str, ...]] = {
    'Actor': ('id', 'name', 'height_m', 'lengths'),
    'BodyLength': ('segment', 'length_m'),
    'CalibrationBoard': ('squares_x', 'squares_y', 'square_length_mm', 'marker_length_mm', 'aruco_dictionary', 'measured_square_length_mm'),
    'CameraConfig': ('role', 'source', 'width', 'height', 'fps', 'notes', 'preprocess', 'controls', 'device_hint', 'stream_host', 'video_port', 'sync_port', 'control_port', 'stats_port'),
    'CameraControls': ('exposure_ns', 'iso', 'gain_raw', 'focus_diopters', 'focus_raw', 'white_balance_k', 'power_line_hz', 'auto_exposure', 'auto_focus', 'auto_white_balance'),
    'CameraFileReady': ('take_id', 'role', 'kind', 'path', 'size_bytes', 'sha256', 'frames', 'first_ts_ns', 'last_ts_ns'),
    'CameraTakeReport': ('role', 'frames', 'fps_measured', 'fps_cv', 'gaps', 'first_ts_ns', 'last_ts_ns'),
    'Casting': ('actor_id', 'character_id'),
    'Character': ('id', 'name'),
    'ControlCapability': ('backend', 'key', 'value_type', 'min_value', 'max_value', 'step', 'options', 'default_value', 'current_value', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'applied', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': ('int_value', 'float_value', 'flag_value', 'text_value', 'int_values', 'float_values'),
    'Crop': ('x', 'y', 'width', 'height'),
    'FrameGap': ('after_frame', 'duration_ns'),
    'PreprocessSpec': ('crop', 'output_width', 'output_height'),
    'Session': ('id', 'date', 'actors', 'characters', 'casting'),
    'SyncEvent': ('kind', 'host_ts_ns', 'source'),
    'Take': ('id', 'session_id', 'type', 'start', 'end', 'casting', 'board', 'cameras'),
    'TakeCamera': ('config', 'control_results', 'applied_controls', 'applied_preprocess'),
    'TakeClosed': ('take_id', 'roles', 'start', 'end'),
    'TakeReport': ('take_id', 'ok', 'problems', 'reports'),
}

# Fields declared `required` (proto3 doesn't keep it).
REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    'Actor': ('id', 'name', 'height_m'),
    'BodyLength': ('segment', 'length_m'),
    'CalibrationBoard': ('squares_x', 'squares_y', 'square_length_mm', 'marker_length_mm', 'aruco_dictionary', 'measured_square_length_mm'),
    'CameraConfig': ('role', 'source', 'width', 'height', 'fps', 'notes'),
    'CameraControls': (),
    'CameraFileReady': ('take_id', 'role', 'kind', 'path', 'size_bytes', 'sha256', 'frames', 'first_ts_ns', 'last_ts_ns'),
    'CameraTakeReport': ('role', 'frames', 'fps_measured', 'fps_cv', 'first_ts_ns', 'last_ts_ns'),
    'Casting': ('actor_id', 'character_id'),
    'Character': ('id', 'name'),
    'ControlCapability': ('backend', 'key', 'value_type', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': (),
    'Crop': ('x', 'y', 'width', 'height'),
    'FrameGap': ('after_frame', 'duration_ns'),
    'PreprocessSpec': ('output_width', 'output_height'),
    'Session': ('id', 'date'),
    'SyncEvent': ('kind', 'host_ts_ns', 'source'),
    'Take': ('id', 'session_id', 'type', 'start'),
    'TakeCamera': ('config',),
    'TakeClosed': ('take_id', 'start', 'end'),
    'TakeReport': ('take_id', 'ok'),
}

__all__ = [
    "Actor",
    "BodyLength",
    "CalibrationBoard",
    "CameraConfig",
    "CameraControls",
    "CameraFileReady",
    "CameraSource",
    "CameraTakeReport",
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
    "FileKind",
    "Flag",
    "FrameGap",
    "PreprocessSpec",
    "Session",
    "SyncEvent",
    "SyncKind",
    "SyncSource",
    "Take",
    "TakeCamera",
    "TakeClosed",
    "TakeReport",
    "TakeType",
]
