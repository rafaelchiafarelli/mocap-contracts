from harpia_generated.protofiles import SyncKind_7656bad163803b596999eb3843b4995c_pb2 as _SyncKind_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import SyncSource_7656bad163803b596999eb3843b4995c_pb2 as _SyncSource_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "host_ts_ns", "kind", "source"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    host_ts_ns: int
    kind: _SyncKind_7656bad163803b596999eb3843b4995c_pb2.SyncKind
    source: _SyncSource_7656bad163803b596999eb3843b4995c_pb2.SyncSource
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_7656bad163803b596999eb3843b4995c_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_7656bad163803b596999eb3843b4995c_pb2.SyncSource, str]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
