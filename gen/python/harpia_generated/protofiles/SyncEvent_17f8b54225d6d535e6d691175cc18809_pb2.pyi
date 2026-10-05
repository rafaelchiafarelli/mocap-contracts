from harpia_generated.protofiles import SyncKind_17f8b54225d6d535e6d691175cc18809_pb2 as _SyncKind_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import SyncSource_17f8b54225d6d535e6d691175cc18809_pb2 as _SyncSource_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "host_ts_ns", "kind", "source"]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    host_ts_ns: int
    kind: _SyncKind_17f8b54225d6d535e6d691175cc18809_pb2.SyncKind
    source: _SyncSource_17f8b54225d6d535e6d691175cc18809_pb2.SyncSource
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_17f8b54225d6d535e6d691175cc18809_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_17f8b54225d6d535e6d691175cc18809_pb2.SyncSource, str]] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
