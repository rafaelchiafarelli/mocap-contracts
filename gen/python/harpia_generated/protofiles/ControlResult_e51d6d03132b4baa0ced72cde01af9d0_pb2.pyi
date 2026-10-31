from harpia_generated.protofiles import ControlValue_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlValue_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ControlStatus_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlStatus_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    applied: _ControlValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlValue
    status: _ControlStatus_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlStatus
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
