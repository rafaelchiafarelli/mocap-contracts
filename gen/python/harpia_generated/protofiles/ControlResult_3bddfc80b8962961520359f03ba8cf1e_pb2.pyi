from harpia_generated.protofiles import ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2 as _ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import ControlStatus_3bddfc80b8962961520359f03ba8cf1e_pb2 as _ControlStatus_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlValue
    status: _ControlStatus_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlStatus
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
