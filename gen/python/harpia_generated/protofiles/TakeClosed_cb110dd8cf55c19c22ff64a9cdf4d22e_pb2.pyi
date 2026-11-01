from harpia_generated.protofiles import SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR_cb110dd8cf55c19c22ff64a9cdf4d22e", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent, _Mapping]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ...) -> None: ...
