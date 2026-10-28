from harpia_generated.protofiles import ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlStatus_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlStatus_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    status: _ControlStatus_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlStatus
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
