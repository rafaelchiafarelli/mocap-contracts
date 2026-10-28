from harpia_generated.protofiles import SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2 as _SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ORIGINATOR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent, _Mapping]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ...) -> None: ...
