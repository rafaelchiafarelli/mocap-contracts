from harpia_generated.protofiles import ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import ControlStatus_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlStatus_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    status: _ControlStatus_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlStatus
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
