from harpia_generated.protofiles import SyncKind_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _SyncKind_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import SyncSource_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _SyncSource_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "host_ts_ns", "kind", "source"]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    host_ts_ns: int
    kind: _SyncKind_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncKind
    source: _SyncSource_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncSource
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncSource, str]] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
