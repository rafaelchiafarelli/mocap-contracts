from harpia_generated.protofiles import SyncKind_3bddfc80b8962961520359f03ba8cf1e_pb2 as _SyncKind_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import SyncSource_3bddfc80b8962961520359f03ba8cf1e_pb2 as _SyncSource_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "host_ts_ns", "kind", "source"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    host_ts_ns: int
    kind: _SyncKind_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncKind
    source: _SyncSource_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncSource
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncSource, str]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
