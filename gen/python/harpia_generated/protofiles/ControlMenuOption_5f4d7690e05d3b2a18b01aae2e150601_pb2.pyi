from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ControlMenuOption(_message.Message):
    __slots__ = ["ERROR_5f4d7690e05d3b2a18b01aae2e150601", "ID_5f4d7690e05d3b2a18b01aae2e150601", "ORIGINATOR", "STATUS_5f4d7690e05d3b2a18b01aae2e150601", "name", "value"]
    ERROR_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    ERROR_5f4d7690e05d3b2a18b01aae2e150601: str
    ID_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    ID_5f4d7690e05d3b2a18b01aae2e150601: int
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    STATUS_5f4d7690e05d3b2a18b01aae2e150601: str
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    def __init__(self, ID_5f4d7690e05d3b2a18b01aae2e150601: _Optional[int] = ..., value: _Optional[int] = ..., name: _Optional[str] = ..., STATUS_5f4d7690e05d3b2a18b01aae2e150601: _Optional[str] = ..., ERROR_5f4d7690e05d3b2a18b01aae2e150601: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
