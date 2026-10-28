from harpia_generated.protofiles import SyncKind_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _SyncKind_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import SyncSource_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _SyncSource_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "host_ts_ns", "kind", "source"]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    host_ts_ns: int
    kind: _SyncKind_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncKind
    source: _SyncSource_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncSource
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncSource, str]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
