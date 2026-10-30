from harpia_generated.protofiles import ControlBackend_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlBackend_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlValueType_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlValueType_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlValue_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlMenuOption_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlMenuOption_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Flag_acbcec83d1091de463df65590ca62e7d_pb2 as _Flag_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlCapability(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "backend", "current_value", "default_value", "key", "max_value", "min_value", "options", "read_only", "step", "unit", "value_type"]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    STEP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    backend: _ControlBackend_acbcec83d1091de463df65590ca62e7d_pb2.ControlBackend
    current_value: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    default_value: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    key: str
    max_value: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    min_value: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    options: _containers.RepeatedCompositeFieldContainer[_ControlMenuOption_acbcec83d1091de463df65590ca62e7d_pb2.ControlMenuOption]
    read_only: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    step: _ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue
    unit: str
    value_type: _ControlValueType_acbcec83d1091de463df65590ca62e7d_pb2.ControlValueType
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., backend: _Optional[_Union[_ControlBackend_acbcec83d1091de463df65590ca62e7d_pb2.ControlBackend, str]] = ..., key: _Optional[str] = ..., value_type: _Optional[_Union[_ControlValueType_acbcec83d1091de463df65590ca62e7d_pb2.ControlValueType, str]] = ..., min_value: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., max_value: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., step: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., options: _Optional[_Iterable[_Union[_ControlMenuOption_acbcec83d1091de463df65590ca62e7d_pb2.ControlMenuOption, _Mapping]]] = ..., default_value: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., current_value: _Optional[_Union[_ControlValue_acbcec83d1091de463df65590ca62e7d_pb2.ControlValue, _Mapping]] = ..., read_only: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., unit: _Optional[str] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
