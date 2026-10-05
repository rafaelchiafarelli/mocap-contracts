from harpia_generated.protofiles import CameraSource_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraSource_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraConfig(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "control_port", "controls", "device_hint", "fps", "height", "notes", "preprocess", "role", "source", "stats_port", "stream_host", "sync_port", "video_port", "width"]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HINT_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    FPS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATS_PORT_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    STREAM_HOST_FIELD_NUMBER: _ClassVar[int]
    SYNC_PORT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PORT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    control_port: int
    controls: _containers.RepeatedCompositeFieldContainer[_ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlSetting]
    device_hint: str
    fps: float
    height: int
    notes: str
    preprocess: _PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2.PreprocessSpec
    role: str
    source: _CameraSource_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraSource
    stats_port: int
    stream_host: str
    sync_port: int
    video_port: int
    width: int
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., role: _Optional[str] = ..., source: _Optional[_Union[_CameraSource_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraSource, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., fps: _Optional[float] = ..., notes: _Optional[str] = ..., preprocess: _Optional[_Union[_PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2.PreprocessSpec, _Mapping]] = ..., controls: _Optional[_Iterable[_Union[_ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlSetting, _Mapping]]] = ..., device_hint: _Optional[str] = ..., stream_host: _Optional[str] = ..., video_port: _Optional[int] = ..., sync_port: _Optional[int] = ..., control_port: _Optional[int] = ..., stats_port: _Optional[int] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
