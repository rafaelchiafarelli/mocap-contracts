from harpia_generated.protofiles import SyncEvent_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _SyncEvent_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ORIGINATOR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.SyncEvent, _Mapping]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ...) -> None: ...
