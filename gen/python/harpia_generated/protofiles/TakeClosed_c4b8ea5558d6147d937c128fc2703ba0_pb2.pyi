from harpia_generated.protofiles import SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent, _Mapping]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ...) -> None: ...
