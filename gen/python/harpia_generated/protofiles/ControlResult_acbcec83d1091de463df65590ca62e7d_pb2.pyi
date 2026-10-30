from harpia_generated.protofiles import ControlValue_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlStatus_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlStatus_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    applied: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    status: _ControlStatus_acbcec83d1091de463df65590ca62e7d_pb2.ControlStatus
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_acbcec83d1091de463df65590ca62e7d_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
