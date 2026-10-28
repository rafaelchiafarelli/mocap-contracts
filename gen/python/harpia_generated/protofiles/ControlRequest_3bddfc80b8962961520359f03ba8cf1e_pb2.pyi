from harpia_generated.protofiles import StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2 as _StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import ControlSetting_3bddfc80b8962961520359f03ba8cf1e_pb2 as _ControlSetting_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import Flag_3bddfc80b8962961520359f03ba8cf1e_pb2 as _Flag_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ORIGINATOR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlSetting]
    stream: _StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2.StreamSettings
    want_device_info: _Flag_3bddfc80b8962961520359f03ba8cf1e_pb2.Flag
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_3bddfc80b8962961520359f03ba8cf1e_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ...) -> None: ...
