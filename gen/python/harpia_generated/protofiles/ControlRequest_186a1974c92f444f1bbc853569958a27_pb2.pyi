from harpia_generated.protofiles import StreamSettings_186a1974c92f444f1bbc853569958a27_pb2 as _StreamSettings_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import ControlSetting_186a1974c92f444f1bbc853569958a27_pb2 as _ControlSetting_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR_186a1974c92f444f1bbc853569958a27", "STATUS_186a1974c92f444f1bbc853569958a27", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_186a1974c92f444f1bbc853569958a27: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_186a1974c92f444f1bbc853569958a27_pb2.ControlSetting]
    stream: _StreamSettings_186a1974c92f444f1bbc853569958a27_pb2.StreamSettings
    want_device_info: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_186a1974c92f444f1bbc853569958a27_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_186a1974c92f444f1bbc853569958a27_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ...) -> None: ...
