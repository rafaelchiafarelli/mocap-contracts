from harpia_generated.protofiles import SyncEvent_186a1974c92f444f1bbc853569958a27_pb2 as _SyncEvent_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR_186a1974c92f444f1bbc853569958a27", "STATUS_186a1974c92f444f1bbc853569958a27", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_186a1974c92f444f1bbc853569958a27: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_186a1974c92f444f1bbc853569958a27_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_186a1974c92f444f1bbc853569958a27_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_186a1974c92f444f1bbc853569958a27_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_186a1974c92f444f1bbc853569958a27_pb2.SyncEvent, _Mapping]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ...) -> None: ...
