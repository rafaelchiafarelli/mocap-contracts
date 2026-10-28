from harpia_generated.protofiles import ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2 as _ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlSetting(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "key", "value"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlValue
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_ControlValue_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlValue, _Mapping]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
