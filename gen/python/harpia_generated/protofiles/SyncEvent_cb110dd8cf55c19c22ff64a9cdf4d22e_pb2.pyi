from harpia_generated.protofiles import SyncKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SyncKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import SyncSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SyncSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "host_ts_ns", "kind", "source"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    host_ts_ns: int
    kind: _SyncKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncKind
    source: _SyncSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncSource
    def __init__(self, HARPIA_ID: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncSource, str]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
