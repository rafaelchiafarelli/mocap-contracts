from harpia_generated.protofiles import CameraFacing_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CameraFacing_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import FrameSize_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _FrameSize_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import FpsRange_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _FpsRange_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlCapability_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlCapability_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraInfo(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "camera_id", "controls", "facing", "focal_lengths_mm", "fps_ranges", "hardware_level", "sensor_orientation_deg", "sizes"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    FACING_FIELD_NUMBER: _ClassVar[int]
    FOCAL_LENGTHS_MM_FIELD_NUMBER: _ClassVar[int]
    FPS_RANGES_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ORIENTATION_DEG_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    camera_id: str
    controls: _containers.RepeatedCompositeFieldContainer[_ControlCapability_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlCapability]
    facing: _CameraFacing_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraFacing
    focal_lengths_mm: _containers.RepeatedScalarFieldContainer[float]
    fps_ranges: _containers.RepeatedCompositeFieldContainer[_FpsRange_136996d09eedbf0a12cec4204d8d4ec2_pb2.FpsRange]
    hardware_level: str
    sensor_orientation_deg: int
    sizes: _containers.RepeatedCompositeFieldContainer[_FrameSize_136996d09eedbf0a12cec4204d8d4ec2_pb2.FrameSize]
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., camera_id: _Optional[str] = ..., facing: _Optional[_Union[_CameraFacing_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraFacing, str]] = ..., hardware_level: _Optional[str] = ..., sensor_orientation_deg: _Optional[int] = ..., focal_lengths_mm: _Optional[_Iterable[float]] = ..., sizes: _Optional[_Iterable[_Union[_FrameSize_136996d09eedbf0a12cec4204d8d4ec2_pb2.FrameSize, _Mapping]]] = ..., fps_ranges: _Optional[_Iterable[_Union[_FpsRange_136996d09eedbf0a12cec4204d8d4ec2_pb2.FpsRange, _Mapping]]] = ..., controls: _Optional[_Iterable[_Union[_ControlCapability_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlCapability, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
