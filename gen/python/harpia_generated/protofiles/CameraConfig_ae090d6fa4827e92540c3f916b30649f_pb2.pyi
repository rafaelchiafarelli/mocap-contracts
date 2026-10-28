from harpia_generated.protofiles import CameraSource_ae090d6fa4827e92540c3f916b30649f_pb2 as _CameraSource_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2 as _PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2 as _ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraConfig(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "control_port", "controls", "device_hint", "fps", "height", "notes", "preprocess", "role", "source", "stats_port", "stream_host", "sync_port", "video_port", "width"]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HINT_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    FPS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATS_PORT_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    STREAM_HOST_FIELD_NUMBER: _ClassVar[int]
    SYNC_PORT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PORT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    control_port: int
    controls: _containers.RepeatedCompositeFieldContainer[_ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2.ControlSetting]
    device_hint: str
    fps: float
    height: int
    notes: str
    preprocess: _PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2.PreprocessSpec
    role: str
    source: _CameraSource_ae090d6fa4827e92540c3f916b30649f_pb2.CameraSource
    stats_port: int
    stream_host: str
    sync_port: int
    video_port: int
    width: int
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., role: _Optional[str] = ..., source: _Optional[_Union[_CameraSource_ae090d6fa4827e92540c3f916b30649f_pb2.CameraSource, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., fps: _Optional[float] = ..., notes: _Optional[str] = ..., preprocess: _Optional[_Union[_PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2.PreprocessSpec, _Mapping]] = ..., controls: _Optional[_Iterable[_Union[_ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2.ControlSetting, _Mapping]]] = ..., device_hint: _Optional[str] = ..., stream_host: _Optional[str] = ..., video_port: _Optional[int] = ..., sync_port: _Optional[int] = ..., control_port: _Optional[int] = ..., stats_port: _Optional[int] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
