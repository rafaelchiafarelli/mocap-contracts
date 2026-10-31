from harpia_generated.protofiles import CameraSource_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _CameraSource_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraConfig(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "control_port", "controls", "device_hint", "fps", "height", "notes", "preprocess", "role", "source", "stats_port", "stream_host", "sync_port", "video_port", "width"]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HINT_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FPS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATS_PORT_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    STREAM_HOST_FIELD_NUMBER: _ClassVar[int]
    SYNC_PORT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PORT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    control_port: int
    controls: _containers.RepeatedCompositeFieldContainer[_ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlSetting]
    device_hint: str
    fps: float
    height: int
    notes: str
    preprocess: _PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2.PreprocessSpec
    role: str
    source: _CameraSource_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraSource
    stats_port: int
    stream_host: str
    sync_port: int
    video_port: int
    width: int
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., role: _Optional[str] = ..., source: _Optional[_Union[_CameraSource_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraSource, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., fps: _Optional[float] = ..., notes: _Optional[str] = ..., preprocess: _Optional[_Union[_PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2.PreprocessSpec, _Mapping]] = ..., controls: _Optional[_Iterable[_Union[_ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlSetting, _Mapping]]] = ..., device_hint: _Optional[str] = ..., stream_host: _Optional[str] = ..., video_port: _Optional[int] = ..., sync_port: _Optional[int] = ..., control_port: _Optional[int] = ..., stats_port: _Optional[int] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
