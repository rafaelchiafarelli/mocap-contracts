from harpia_generated.protofiles import CameraFacing_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraFacing_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import FrameSize_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FrameSize_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import FpsRange_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FpsRange_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlCapability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlCapability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraInfo(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "camera_id", "controls", "facing", "focal_lengths_mm", "fps_ranges", "hardware_level", "sensor_orientation_deg", "sizes"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    FACING_FIELD_NUMBER: _ClassVar[int]
    FOCAL_LENGTHS_MM_FIELD_NUMBER: _ClassVar[int]
    FPS_RANGES_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ORIENTATION_DEG_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    camera_id: str
    controls: _containers.RepeatedCompositeFieldContainer[_ControlCapability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlCapability]
    facing: _CameraFacing_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraFacing
    focal_lengths_mm: _containers.RepeatedScalarFieldContainer[float]
    fps_ranges: _containers.RepeatedCompositeFieldContainer[_FpsRange_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FpsRange]
    hardware_level: str
    sensor_orientation_deg: int
    sizes: _containers.RepeatedCompositeFieldContainer[_FrameSize_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FrameSize]
    def __init__(self, HARPIA_ID: _Optional[int] = ..., camera_id: _Optional[str] = ..., facing: _Optional[_Union[_CameraFacing_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraFacing, str]] = ..., hardware_level: _Optional[str] = ..., sensor_orientation_deg: _Optional[int] = ..., focal_lengths_mm: _Optional[_Iterable[float]] = ..., sizes: _Optional[_Iterable[_Union[_FrameSize_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FrameSize, _Mapping]]] = ..., fps_ranges: _Optional[_Iterable[_Union[_FpsRange_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FpsRange, _Mapping]]] = ..., controls: _Optional[_Iterable[_Union[_ControlCapability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlCapability, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
