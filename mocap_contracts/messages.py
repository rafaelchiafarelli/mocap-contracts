"""Every contract message and enum, under its declared name.

Written by tools/harpia_gen.py (`make gen`); do not edit. Harpia's
module names carry a hash of the root .harpia file and change with it;
import from here (or from mocap_contracts) instead."""

from harpia_generated.protofiles.Actor_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Actor
from harpia_generated.protofiles.BodyLength_9741ae31683aa8e5c6ffec2922711a8d_pb2 import BodyLength
from harpia_generated.protofiles.BoneStability_9741ae31683aa8e5c6ffec2922711a8d_pb2 import BoneStability
from harpia_generated.protofiles.CalibrationBoard_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CalibrationBoard
from harpia_generated.protofiles.CameraAblation_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraAblation
from harpia_generated.protofiles.CameraAlignment_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraAlignment
from harpia_generated.protofiles.CameraConfig_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraConfig
from harpia_generated.protofiles.CameraControls_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraControls
from harpia_generated.protofiles.CameraFileReady_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraFileReady
from harpia_generated.protofiles.CameraQuality_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraQuality
from harpia_generated.protofiles.CameraSource_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraSource
from harpia_generated.protofiles.CameraTakeReport_9741ae31683aa8e5c6ffec2922711a8d_pb2 import CameraTakeReport
from harpia_generated.protofiles.Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Casting
from harpia_generated.protofiles.Character_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Character
from harpia_generated.protofiles.ControlBackend_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlBackend
from harpia_generated.protofiles.ControlCapability_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlCapability
from harpia_generated.protofiles.ControlMenuOption_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlMenuOption
from harpia_generated.protofiles.ControlResult_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlResult
from harpia_generated.protofiles.ControlSetting_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlSetting
from harpia_generated.protofiles.ControlStatus_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlStatus
from harpia_generated.protofiles.ControlValueType_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlValueType
from harpia_generated.protofiles.ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ControlValue
from harpia_generated.protofiles.Crop_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Crop
from harpia_generated.protofiles.ExtractIndex_9741ae31683aa8e5c6ffec2922711a8d_pb2 import ExtractIndex
from harpia_generated.protofiles.FileKind_9741ae31683aa8e5c6ffec2922711a8d_pb2 import FileKind
from harpia_generated.protofiles.Flag_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Flag
from harpia_generated.protofiles.FrameGap_9741ae31683aa8e5c6ffec2922711a8d_pb2 import FrameGap
from harpia_generated.protofiles.LengthUnit_9741ae31683aa8e5c6ffec2922711a8d_pb2 import LengthUnit
from harpia_generated.protofiles.PointSet_9741ae31683aa8e5c6ffec2922711a8d_pb2 import PointSet
from harpia_generated.protofiles.PreprocessSpec_9741ae31683aa8e5c6ffec2922711a8d_pb2 import PreprocessSpec
from harpia_generated.protofiles.QualityReport_9741ae31683aa8e5c6ffec2922711a8d_pb2 import QualityReport
from harpia_generated.protofiles.Session_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Session
from harpia_generated.protofiles.SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2 import SyncEvent
from harpia_generated.protofiles.SyncKind_9741ae31683aa8e5c6ffec2922711a8d_pb2 import SyncKind
from harpia_generated.protofiles.SyncSource_9741ae31683aa8e5c6ffec2922711a8d_pb2 import SyncSource
from harpia_generated.protofiles.SyncedVideo_9741ae31683aa8e5c6ffec2922711a8d_pb2 import SyncedVideo
from harpia_generated.protofiles.TakeCamera_9741ae31683aa8e5c6ffec2922711a8d_pb2 import TakeCamera
from harpia_generated.protofiles.TakeClosed_9741ae31683aa8e5c6ffec2922711a8d_pb2 import TakeClosed
from harpia_generated.protofiles.TakeReport_9741ae31683aa8e5c6ffec2922711a8d_pb2 import TakeReport
from harpia_generated.protofiles.TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2 import TakeType
from harpia_generated.protofiles.Take_9741ae31683aa8e5c6ffec2922711a8d_pb2 import Take
from harpia_generated.protofiles.UpAxis_9741ae31683aa8e5c6ffec2922711a8d_pb2 import UpAxis

# Field names as declared in schema/ (Harpia's bookkeeping fields excluded).
DECLARED_FIELDS: dict[str, tuple[str, ...]] = {
    'Actor': ('id', 'name', 'height_m', 'lengths'),
    'BodyLength': ('segment', 'length_m'),
    'BoneStability': ('bone', 'mean_length_m', 'rsd'),
    'CalibrationBoard': ('squares_x', 'squares_y', 'square_length_mm', 'marker_length_mm', 'aruco_dictionary', 'measured_square_length_mm'),
    'CameraAblation': ('removed_role', 'mean_shift_m', 'mean_rsd_change'),
    'CameraAlignment': ('role', 'offset_ns', 'drift_ppm', 'frames_in', 'frames_out'),
    'CameraConfig': ('role', 'source', 'width', 'height', 'fps', 'notes', 'preprocess', 'controls', 'device_hint', 'stream_host', 'video_port', 'sync_port', 'control_port', 'stats_port'),
    'CameraControls': ('exposure_ns', 'iso', 'gain_raw', 'focus_diopters', 'focus_raw', 'white_balance_k', 'power_line_hz', 'auto_exposure', 'auto_focus', 'auto_white_balance'),
    'CameraFileReady': ('take_id', 'role', 'kind', 'path', 'size_bytes', 'sha256', 'frames', 'first_ts_ns', 'last_ts_ns'),
    'CameraQuality': ('role', 'detection_rate_body', 'detection_rate_left_hand', 'detection_rate_right_hand', 'jitter_px', 'reproj_err_px'),
    'CameraTakeReport': ('role', 'frames', 'fps_measured', 'fps_cv', 'gaps', 'first_ts_ns', 'last_ts_ns'),
    'Casting': ('actor_id', 'character_id'),
    'Character': ('id', 'name'),
    'ControlCapability': ('backend', 'key', 'value_type', 'min_value', 'max_value', 'step', 'options', 'default_value', 'current_value', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'applied', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': ('int_value', 'float_value', 'flag_value', 'text_value', 'int_values', 'float_values'),
    'Crop': ('x', 'y', 'width', 'height'),
    'ExtractIndex': ('take_id', 'calibration_take_id', 'calibration_path', 'fps', 'frames', 't0_ns', 'length_unit', 'up_axis', 'synced_videos', 'alignment', 'points_3d', 'points_2d'),
    'FrameGap': ('after_frame', 'duration_ns'),
    'PointSet': ('name', 'role', 'path', 'frames', 'point_names'),
    'PreprocessSpec': ('crop', 'output_width', 'output_height'),
    'QualityReport': ('take_id', 'calibration_reproj_err_px', 'cameras', 'bones', 'ablation'),
    'Session': ('id', 'date', 'actors', 'characters', 'casting'),
    'SyncEvent': ('kind', 'host_ts_ns', 'source'),
    'SyncedVideo': ('role', 'path'),
    'Take': ('id', 'session_id', 'type', 'start', 'end', 'casting', 'board', 'cameras'),
    'TakeCamera': ('config', 'control_results', 'applied_controls', 'applied_preprocess'),
    'TakeClosed': ('take_id', 'roles', 'start', 'end'),
    'TakeReport': ('take_id', 'ok', 'problems', 'reports'),
}

# Fields declared `required` (proto3 doesn't keep it).
REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    'Actor': ('id', 'name', 'height_m'),
    'BodyLength': ('segment', 'length_m'),
    'BoneStability': ('bone', 'mean_length_m', 'rsd'),
    'CalibrationBoard': ('squares_x', 'squares_y', 'square_length_mm', 'marker_length_mm', 'aruco_dictionary', 'measured_square_length_mm'),
    'CameraAblation': ('removed_role', 'mean_shift_m', 'mean_rsd_change'),
    'CameraAlignment': ('role', 'offset_ns', 'drift_ppm', 'frames_in', 'frames_out'),
    'CameraConfig': ('role', 'source', 'width', 'height', 'fps', 'notes'),
    'CameraControls': (),
    'CameraFileReady': ('take_id', 'role', 'kind', 'path', 'size_bytes', 'sha256', 'frames', 'first_ts_ns', 'last_ts_ns'),
    'CameraQuality': ('role', 'detection_rate_body', 'detection_rate_left_hand', 'detection_rate_right_hand'),
    'CameraTakeReport': ('role', 'frames', 'fps_measured', 'fps_cv', 'first_ts_ns', 'last_ts_ns'),
    'Casting': ('actor_id', 'character_id'),
    'Character': ('id', 'name'),
    'ControlCapability': ('backend', 'key', 'value_type', 'read_only', 'unit'),
    'ControlMenuOption': ('value', 'name'),
    'ControlResult': ('key', 'requested', 'status', 'note'),
    'ControlSetting': ('key', 'value'),
    'ControlValue': (),
    'Crop': ('x', 'y', 'width', 'height'),
    'ExtractIndex': ('take_id', 'calibration_take_id', 'calibration_path', 'fps', 'frames', 't0_ns', 'length_unit', 'up_axis'),
    'FrameGap': ('after_frame', 'duration_ns'),
    'PointSet': ('name', 'role', 'path', 'frames'),
    'PreprocessSpec': ('output_width', 'output_height'),
    'QualityReport': ('take_id',),
    'Session': ('id', 'date'),
    'SyncEvent': ('kind', 'host_ts_ns', 'source'),
    'SyncedVideo': ('role', 'path'),
    'Take': ('id', 'session_id', 'type', 'start'),
    'TakeCamera': ('config',),
    'TakeClosed': ('take_id', 'start', 'end'),
    'TakeReport': ('take_id', 'ok'),
}

__all__ = [
    "Actor",
    "BodyLength",
    "BoneStability",
    "CalibrationBoard",
    "CameraAblation",
    "CameraAlignment",
    "CameraConfig",
    "CameraControls",
    "CameraFileReady",
    "CameraQuality",
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
    "ExtractIndex",
    "FileKind",
    "Flag",
    "FrameGap",
    "LengthUnit",
    "PointSet",
    "PreprocessSpec",
    "QualityReport",
    "Session",
    "SyncEvent",
    "SyncKind",
    "SyncSource",
    "SyncedVideo",
    "Take",
    "TakeCamera",
    "TakeClosed",
    "TakeReport",
    "TakeType",
    "UpAxis",
]
