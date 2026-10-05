from harpia_generated.protofiles import ControlValue_17f8b54225d6d535e6d691175cc18809_pb2 as _ControlValue_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlSetting(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "key", "value"]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _ControlValue_17f8b54225d6d535e6d691175cc18809_pb2.ControlValue
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_ControlValue_17f8b54225d6d535e6d691175cc18809_pb2.ControlValue, _Mapping]] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
