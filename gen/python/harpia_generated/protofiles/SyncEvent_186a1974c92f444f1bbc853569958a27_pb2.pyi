from harpia_generated.protofiles import SyncKind_186a1974c92f444f1bbc853569958a27_pb2 as _SyncKind_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import SyncSource_186a1974c92f444f1bbc853569958a27_pb2 as _SyncSource_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "host_ts_ns", "kind", "source"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    host_ts_ns: int
    kind: _SyncKind_186a1974c92f444f1bbc853569958a27_pb2.SyncKind
    source: _SyncSource_186a1974c92f444f1bbc853569958a27_pb2.SyncSource
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_186a1974c92f444f1bbc853569958a27_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_186a1974c92f444f1bbc853569958a27_pb2.SyncSource, str]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
