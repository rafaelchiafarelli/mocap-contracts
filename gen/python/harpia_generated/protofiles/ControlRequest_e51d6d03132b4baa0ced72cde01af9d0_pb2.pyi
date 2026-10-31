from harpia_generated.protofiles import StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlSetting]
    stream: _StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.StreamSettings
    want_device_info: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ...) -> None: ...
