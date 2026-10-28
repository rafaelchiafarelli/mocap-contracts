from harpia_generated.protofiles import ControlBackend_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlBackend_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlValueType_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlValueType_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlMenuOption_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlMenuOption_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlCapability(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "backend", "current_value", "default_value", "key", "max_value", "min_value", "options", "read_only", "step", "unit", "value_type"]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    STEP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    backend: _ControlBackend_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlBackend
    current_value: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    default_value: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    key: str
    max_value: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    min_value: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    options: _containers.RepeatedCompositeFieldContainer[_ControlMenuOption_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlMenuOption]
    read_only: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    step: _ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue
    unit: str
    value_type: _ControlValueType_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValueType
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., backend: _Optional[_Union[_ControlBackend_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlBackend, str]] = ..., key: _Optional[str] = ..., value_type: _Optional[_Union[_ControlValueType_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValueType, str]] = ..., min_value: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., max_value: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., step: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., options: _Optional[_Iterable[_Union[_ControlMenuOption_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlMenuOption, _Mapping]]] = ..., default_value: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., current_value: _Optional[_Union[_ControlValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlValue, _Mapping]] = ..., read_only: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., unit: _Optional[str] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
