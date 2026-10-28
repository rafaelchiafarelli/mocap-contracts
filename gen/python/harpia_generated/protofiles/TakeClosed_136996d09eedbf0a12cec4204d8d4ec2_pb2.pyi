from harpia_generated.protofiles import SyncEvent_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _SyncEvent_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeClosed(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "end", "roles", "start", "take_id"]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: str
    ROLES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    end: _SyncEvent_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncEvent
    roles: _containers.RepeatedScalarFieldContainer[str]
    start: _SyncEvent_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncEvent
    take_id: str
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., take_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., start: _Optional[_Union[_SyncEvent_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_136996d09eedbf0a12cec4204d8d4ec2_pb2.SyncEvent, _Mapping]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ...) -> None: ...
