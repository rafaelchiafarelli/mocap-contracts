from harpia_generated.protofiles import ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    applied: _ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue
    status: _ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlStatus
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
