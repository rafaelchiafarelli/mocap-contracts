from harpia_generated.protofiles import CameraFacing_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraFacing_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import FrameSize_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _FrameSize_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import FpsRange_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _FpsRange_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import ControlCapability_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlCapability_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraInfo(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "camera_id", "controls", "facing", "focal_lengths_mm", "fps_ranges", "hardware_level", "sensor_orientation_deg", "sizes"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    FACING_FIELD_NUMBER: _ClassVar[int]
    FOCAL_LENGTHS_MM_FIELD_NUMBER: _ClassVar[int]
    FPS_RANGES_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ORIENTATION_DEG_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    camera_id: str
    controls: _containers.RepeatedCompositeFieldContainer[_ControlCapability_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlCapability]
    facing: _CameraFacing_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraFacing
    focal_lengths_mm: _containers.RepeatedScalarFieldContainer[float]
    fps_ranges: _containers.RepeatedCompositeFieldContainer[_FpsRange_c4b8ea5558d6147d937c128fc2703ba0_pb2.FpsRange]
    hardware_level: str
    sensor_orientation_deg: int
    sizes: _containers.RepeatedCompositeFieldContainer[_FrameSize_c4b8ea5558d6147d937c128fc2703ba0_pb2.FrameSize]
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., camera_id: _Optional[str] = ..., facing: _Optional[_Union[_CameraFacing_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraFacing, str]] = ..., hardware_level: _Optional[str] = ..., sensor_orientation_deg: _Optional[int] = ..., focal_lengths_mm: _Optional[_Iterable[float]] = ..., sizes: _Optional[_Iterable[_Union[_FrameSize_c4b8ea5558d6147d937c128fc2703ba0_pb2.FrameSize, _Mapping]]] = ..., fps_ranges: _Optional[_Iterable[_Union[_FpsRange_c4b8ea5558d6147d937c128fc2703ba0_pb2.FpsRange, _Mapping]]] = ..., controls: _Optional[_Iterable[_Union[_ControlCapability_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlCapability, _Mapping]]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
