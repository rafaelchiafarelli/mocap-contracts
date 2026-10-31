from harpia_generated.protofiles import SyncKind_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _SyncKind_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import SyncSource_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _SyncSource_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "host_ts_ns", "kind", "source"]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    host_ts_ns: int
    kind: _SyncKind_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncKind
    source: _SyncSource_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncSource
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncSource, str]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
