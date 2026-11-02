from harpia_generated.protofiles import CameraSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraConfig(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "control_port", "controls", "device_hint", "fps", "height", "notes", "preprocess", "role", "source", "stats_port", "stream_host", "sync_port", "video_port", "width"]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HINT_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATS_PORT_FIELD_NUMBER: _ClassVar[int]
    STREAM_HOST_FIELD_NUMBER: _ClassVar[int]
    SYNC_PORT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PORT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    control_port: int
    controls: _containers.RepeatedCompositeFieldContainer[_ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlSetting]
    device_hint: str
    fps: float
    height: int
    notes: str
    preprocess: _PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PreprocessSpec
    role: str
    source: _CameraSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraSource
    stats_port: int
    stream_host: str
    sync_port: int
    video_port: int
    width: int
    def __init__(self, HARPIA_ID: _Optional[int] = ..., role: _Optional[str] = ..., source: _Optional[_Union[_CameraSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraSource, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., fps: _Optional[float] = ..., notes: _Optional[str] = ..., preprocess: _Optional[_Union[_PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PreprocessSpec, _Mapping]] = ..., controls: _Optional[_Iterable[_Union[_ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlSetting, _Mapping]]] = ..., device_hint: _Optional[str] = ..., stream_host: _Optional[str] = ..., video_port: _Optional[int] = ..., sync_port: _Optional[int] = ..., control_port: _Optional[int] = ..., stats_port: _Optional[int] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
