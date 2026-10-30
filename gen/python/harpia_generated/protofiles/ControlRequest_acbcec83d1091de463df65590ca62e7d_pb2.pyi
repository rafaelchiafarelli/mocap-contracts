from harpia_generated.protofiles import StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2 as _StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlSetting_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlSetting_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Flag_acbcec83d1091de463df65590ca62e7d_pb2 as _Flag_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR_acbcec83d1091de463df65590ca62e7d", "STATUS_acbcec83d1091de463df65590ca62e7d", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_acbcec83d1091de463df65590ca62e7d: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_acbcec83d1091de463df65590ca62e7d_pb2.ControlSetting]
    stream: _StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2.StreamSettings
    want_device_info: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_acbcec83d1091de463df65590ca62e7d_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ...) -> None: ...
