from harpia_generated.protofiles import SyncKind_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _SyncKind_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import SyncSource_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _SyncSource_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "host_ts_ns", "kind", "source"]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    host_ts_ns: int
    kind: _SyncKind_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncKind
    source: _SyncSource_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncSource
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncSource, str]] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
