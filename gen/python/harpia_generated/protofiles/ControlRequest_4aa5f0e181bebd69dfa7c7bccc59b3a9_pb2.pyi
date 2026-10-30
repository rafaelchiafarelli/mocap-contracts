from harpia_generated.protofiles import StreamSettings_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _StreamSettings_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import ControlSetting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _ControlSetting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ORIGINATOR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlSetting]
    stream: _StreamSettings_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.StreamSettings
    want_device_info: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ...) -> None: ...
