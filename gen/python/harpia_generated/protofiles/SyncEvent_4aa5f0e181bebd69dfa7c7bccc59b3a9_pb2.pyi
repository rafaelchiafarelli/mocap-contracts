from harpia_generated.protofiles import SyncKind_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _SyncKind_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import SyncSource_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _SyncSource_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "host_ts_ns", "kind", "source"]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    host_ts_ns: int
    kind: _SyncKind_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncKind
    source: _SyncSource_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncSource
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncSource, str]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
