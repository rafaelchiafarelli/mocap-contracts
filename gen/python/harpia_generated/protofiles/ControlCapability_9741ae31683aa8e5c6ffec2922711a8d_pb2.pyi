from harpia_generated.protofiles import ControlBackend_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlBackend_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import ControlValueType_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlValueType_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import ControlMenuOption_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlMenuOption_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import Flag_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _Flag_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlCapability(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "backend", "current_value", "default_value", "key", "max_value", "min_value", "options", "read_only", "step", "unit", "value_type"]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    STEP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    backend: _ControlBackend_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlBackend
    current_value: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    default_value: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    key: str
    max_value: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    min_value: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    options: _containers.RepeatedCompositeFieldContainer[_ControlMenuOption_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlMenuOption]
    read_only: _Flag_9741ae31683aa8e5c6ffec2922711a8d_pb2.Flag
    step: _ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue
    unit: str
    value_type: _ControlValueType_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValueType
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., backend: _Optional[_Union[_ControlBackend_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlBackend, str]] = ..., key: _Optional[str] = ..., value_type: _Optional[_Union[_ControlValueType_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValueType, str]] = ..., min_value: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., max_value: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., step: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., options: _Optional[_Iterable[_Union[_ControlMenuOption_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlMenuOption, _Mapping]]] = ..., default_value: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., current_value: _Optional[_Union[_ControlValue_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlValue, _Mapping]] = ..., read_only: _Optional[_Union[_Flag_9741ae31683aa8e5c6ffec2922711a8d_pb2.Flag, str]] = ..., unit: _Optional[str] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
