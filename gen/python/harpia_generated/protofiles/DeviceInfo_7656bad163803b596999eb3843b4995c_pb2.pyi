from harpia_generated.protofiles import CameraInfo_7656bad163803b596999eb3843b4995c_pb2 as _CameraInfo_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceInfo(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "android_version", "app_version", "cameras", "h264_encoders", "model", "serial"]
    ANDROID_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    H264_ENCODERS_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    android_version: str
    app_version: str
    cameras: _containers.RepeatedCompositeFieldContainer[_CameraInfo_7656bad163803b596999eb3843b4995c_pb2.CameraInfo]
    h264_encoders: _containers.RepeatedScalarFieldContainer[str]
    model: str
    serial: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., model: _Optional[str] = ..., serial: _Optional[str] = ..., android_version: _Optional[str] = ..., app_version: _Optional[str] = ..., h264_encoders: _Optional[_Iterable[str]] = ..., cameras: _Optional[_Iterable[_Union[_CameraInfo_7656bad163803b596999eb3843b4995c_pb2.CameraInfo, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
