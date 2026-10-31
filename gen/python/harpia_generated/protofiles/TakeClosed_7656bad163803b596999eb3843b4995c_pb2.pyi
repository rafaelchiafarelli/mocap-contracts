from harpia_generated.protofiles import SyncEvent_7656bad163803b596999eb3843b4995c_pb2 as _SyncEvent_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR_7656bad163803b596999eb3843b4995c", "STATUS_7656bad163803b596999eb3843b4995c", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_7656bad163803b596999eb3843b4995c: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_7656bad163803b596999eb3843b4995c_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_7656bad163803b596999eb3843b4995c_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_7656bad163803b596999eb3843b4995c_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_7656bad163803b596999eb3843b4995c_pb2.SyncEvent, _Mapping]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR_7656bad163803b596999eb3843b4995c: _Optional[str] = ...) -> None: ...
