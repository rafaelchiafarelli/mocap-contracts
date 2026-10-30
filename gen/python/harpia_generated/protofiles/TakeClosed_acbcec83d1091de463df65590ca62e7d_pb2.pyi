from harpia_generated.protofiles import SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2 as _SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR_acbcec83d1091de463df65590ca62e7d", "STATUS_acbcec83d1091de463df65590ca62e7d", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_acbcec83d1091de463df65590ca62e7d: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent, _Mapping]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ...) -> None: ...
