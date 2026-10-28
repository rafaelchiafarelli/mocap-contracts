from harpia_generated.protofiles import ControlValue_ae090d6fa4827e92540c3f916b30649f_pb2 as _ControlValue_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import ControlStatus_ae090d6fa4827e92540c3f916b30649f_pb2 as _ControlStatus_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    applied: _ControlValue_ae090d6fa4827e92540c3f916b30649f_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_ae090d6fa4827e92540c3f916b30649f_pb2.ControlValue
    status: _ControlStatus_ae090d6fa4827e92540c3f916b30649f_pb2.ControlStatus
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_ae090d6fa4827e92540c3f916b30649f_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_ae090d6fa4827e92540c3f916b30649f_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_ae090d6fa4827e92540c3f916b30649f_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
