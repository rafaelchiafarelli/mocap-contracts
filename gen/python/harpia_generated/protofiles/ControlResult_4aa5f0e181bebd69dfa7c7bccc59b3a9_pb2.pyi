from harpia_generated.protofiles import ControlValue_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _ControlValue_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import ControlStatus_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _ControlStatus_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlValue
    status: _ControlStatus_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlStatus
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
