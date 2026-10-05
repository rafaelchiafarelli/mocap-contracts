from harpia_generated.protofiles import ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2 as _ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2
from harpia_generated.protofiles import ControlStatus_5f4d7690e05d3b2a18b01aae2e150601_pb2 as _ControlStatus_5f4d7690e05d3b2a18b01aae2e150601_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_5f4d7690e05d3b2a18b01aae2e150601", "ID_5f4d7690e05d3b2a18b01aae2e150601", "ORIGINATOR", "STATUS_5f4d7690e05d3b2a18b01aae2e150601", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    ERROR_5f4d7690e05d3b2a18b01aae2e150601: str
    ID_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    ID_5f4d7690e05d3b2a18b01aae2e150601: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    STATUS_5f4d7690e05d3b2a18b01aae2e150601: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2.ControlValue
    status: _ControlStatus_5f4d7690e05d3b2a18b01aae2e150601_pb2.ControlStatus
    def __init__(self, ID_5f4d7690e05d3b2a18b01aae2e150601: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_5f4d7690e05d3b2a18b01aae2e150601_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_5f4d7690e05d3b2a18b01aae2e150601_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_5f4d7690e05d3b2a18b01aae2e150601: _Optional[str] = ..., ERROR_5f4d7690e05d3b2a18b01aae2e150601: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
