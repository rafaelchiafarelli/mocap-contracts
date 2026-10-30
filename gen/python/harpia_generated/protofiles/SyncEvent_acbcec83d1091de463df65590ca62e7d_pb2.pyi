from harpia_generated.protofiles import SyncKind_acbcec83d1091de463df65590ca62e7d_pb2 as _SyncKind_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import SyncSource_acbcec83d1091de463df65590ca62e7d_pb2 as _SyncSource_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "host_ts_ns", "kind", "source"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    host_ts_ns: int
    kind: _SyncKind_acbcec83d1091de463df65590ca62e7d_pb2.SyncKind
    source: _SyncSource_acbcec83d1091de463df65590ca62e7d_pb2.SyncSource
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_acbcec83d1091de463df65590ca62e7d_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_acbcec83d1091de463df65590ca62e7d_pb2.SyncSource, str]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
