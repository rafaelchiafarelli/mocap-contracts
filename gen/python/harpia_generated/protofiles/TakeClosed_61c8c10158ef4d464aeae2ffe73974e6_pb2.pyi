from harpia_generated.protofiles import SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR_61c8c10158ef4d464aeae2ffe73974e6", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    ORIGINATOR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_61c8c10158ef4d464aeae2ffe73974e6: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent, _Mapping]] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ...) -> None: ...
