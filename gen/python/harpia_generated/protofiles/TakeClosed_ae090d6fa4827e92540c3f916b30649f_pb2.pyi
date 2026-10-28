from harpia_generated.protofiles import SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2 as _SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR_ae090d6fa4827e92540c3f916b30649f", "STATUS_ae090d6fa4827e92540c3f916b30649f", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_ae090d6fa4827e92540c3f916b30649f: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent, _Mapping]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ...) -> None: ...
