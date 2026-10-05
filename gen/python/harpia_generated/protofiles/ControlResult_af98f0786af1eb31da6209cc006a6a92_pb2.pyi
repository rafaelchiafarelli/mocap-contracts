from harpia_generated.protofiles import ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2 as _ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2
from harpia_generated.protofiles import ControlStatus_af98f0786af1eb31da6209cc006a6a92_pb2 as _ControlStatus_af98f0786af1eb31da6209cc006a6a92_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_af98f0786af1eb31da6209cc006a6a92", "ID_af98f0786af1eb31da6209cc006a6a92", "ORIGINATOR", "STATUS_af98f0786af1eb31da6209cc006a6a92", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    ERROR_af98f0786af1eb31da6209cc006a6a92: str
    ID_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    ID_af98f0786af1eb31da6209cc006a6a92: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_af98f0786af1eb31da6209cc006a6a92: str
    applied: _ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2.ControlValue
    status: _ControlStatus_af98f0786af1eb31da6209cc006a6a92_pb2.ControlStatus
    def __init__(self, ID_af98f0786af1eb31da6209cc006a6a92: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_af98f0786af1eb31da6209cc006a6a92_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_af98f0786af1eb31da6209cc006a6a92_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_af98f0786af1eb31da6209cc006a6a92: _Optional[str] = ..., ERROR_af98f0786af1eb31da6209cc006a6a92: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
