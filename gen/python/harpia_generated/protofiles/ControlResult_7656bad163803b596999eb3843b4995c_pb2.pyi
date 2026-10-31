from harpia_generated.protofiles import ControlValue_7656bad163803b596999eb3843b4995c_pb2 as _ControlValue_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlStatus_7656bad163803b596999eb3843b4995c_pb2 as _ControlStatus_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    status: _ControlStatus_7656bad163803b596999eb3843b4995c_pb2.ControlStatus
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_7656bad163803b596999eb3843b4995c_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
