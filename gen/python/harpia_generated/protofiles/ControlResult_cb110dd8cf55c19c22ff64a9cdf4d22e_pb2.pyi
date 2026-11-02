from harpia_generated.protofiles import ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue
    status: _ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlStatus
    def __init__(self, HARPIA_ID: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
