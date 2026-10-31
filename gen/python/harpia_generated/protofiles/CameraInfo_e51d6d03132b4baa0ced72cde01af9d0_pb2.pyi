from harpia_generated.protofiles import CameraFacing_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _CameraFacing_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import FrameSize_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _FrameSize_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import FpsRange_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _FpsRange_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ControlCapability_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlCapability_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraInfo(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "camera_id", "controls", "facing", "focal_lengths_mm", "fps_ranges", "hardware_level", "sensor_orientation_deg", "sizes"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FACING_FIELD_NUMBER: _ClassVar[int]
    FOCAL_LENGTHS_MM_FIELD_NUMBER: _ClassVar[int]
    FPS_RANGES_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ORIENTATION_DEG_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    camera_id: str
    controls: _containers.RepeatedCompositeFieldContainer[_ControlCapability_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlCapability]
    facing: _CameraFacing_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraFacing
    focal_lengths_mm: _containers.RepeatedScalarFieldContainer[float]
    fps_ranges: _containers.RepeatedCompositeFieldContainer[_FpsRange_e51d6d03132b4baa0ced72cde01af9d0_pb2.FpsRange]
    hardware_level: str
    sensor_orientation_deg: int
    sizes: _containers.RepeatedCompositeFieldContainer[_FrameSize_e51d6d03132b4baa0ced72cde01af9d0_pb2.FrameSize]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., camera_id: _Optional[str] = ..., facing: _Optional[_Union[_CameraFacing_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraFacing, str]] = ..., hardware_level: _Optional[str] = ..., sensor_orientation_deg: _Optional[int] = ..., focal_lengths_mm: _Optional[_Iterable[float]] = ..., sizes: _Optional[_Iterable[_Union[_FrameSize_e51d6d03132b4baa0ced72cde01af9d0_pb2.FrameSize, _Mapping]]] = ..., fps_ranges: _Optional[_Iterable[_Union[_FpsRange_e51d6d03132b4baa0ced72cde01af9d0_pb2.FpsRange, _Mapping]]] = ..., controls: _Optional[_Iterable[_Union[_ControlCapability_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlCapability, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
