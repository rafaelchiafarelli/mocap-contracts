from harpia_generated.protofiles import StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2 as _StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlResult_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlResult_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import DeviceInfo_acbcec83d1091de463df65590ca62e7d_pb2 as _DeviceInfo_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR_acbcec83d1091de463df65590ca62e7d", "STATUS_acbcec83d1091de463df65590ca62e7d", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_acbcec83d1091de463df65590ca62e7d: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_acbcec83d1091de463df65590ca62e7d_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_acbcec83d1091de463df65590ca62e7d_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2.StreamSettings
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_acbcec83d1091de463df65590ca62e7d_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_acbcec83d1091de463df65590ca62e7d_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_acbcec83d1091de463df65590ca62e7d_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ...) -> None: ...
