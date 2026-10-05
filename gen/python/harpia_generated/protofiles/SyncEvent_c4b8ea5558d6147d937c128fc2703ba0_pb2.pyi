from harpia_generated.protofiles import SyncKind_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _SyncKind_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import SyncSource_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _SyncSource_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "host_ts_ns", "kind", "source"]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    host_ts_ns: int
    kind: _SyncKind_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncKind
    source: _SyncSource_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncSource
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncSource, str]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
