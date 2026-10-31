from harpia_generated.protofiles import ControlBackend_7656bad163803b596999eb3843b4995c_pb2 as _ControlBackend_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlValueType_7656bad163803b596999eb3843b4995c_pb2 as _ControlValueType_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlValue_7656bad163803b596999eb3843b4995c_pb2 as _ControlValue_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlMenuOption_7656bad163803b596999eb3843b4995c_pb2 as _ControlMenuOption_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import Flag_7656bad163803b596999eb3843b4995c_pb2 as _Flag_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlCapability(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "backend", "current_value", "default_value", "key", "max_value", "min_value", "options", "read_only", "step", "unit", "value_type"]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    STEP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    backend: _ControlBackend_7656bad163803b596999eb3843b4995c_pb2.ControlBackend
    current_value: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    default_value: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    key: str
    max_value: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    min_value: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    options: _containers.RepeatedCompositeFieldContainer[_ControlMenuOption_7656bad163803b596999eb3843b4995c_pb2.ControlMenuOption]
    read_only: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    step: _ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue
    unit: str
    value_type: _ControlValueType_7656bad163803b596999eb3843b4995c_pb2.ControlValueType
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., backend: _Optional[_Union[_ControlBackend_7656bad163803b596999eb3843b4995c_pb2.ControlBackend, str]] = ..., key: _Optional[str] = ..., value_type: _Optional[_Union[_ControlValueType_7656bad163803b596999eb3843b4995c_pb2.ControlValueType, str]] = ..., min_value: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., max_value: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., step: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., options: _Optional[_Iterable[_Union[_ControlMenuOption_7656bad163803b596999eb3843b4995c_pb2.ControlMenuOption, _Mapping]]] = ..., default_value: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., current_value: _Optional[_Union[_ControlValue_7656bad163803b596999eb3843b4995c_pb2.ControlValue, _Mapping]] = ..., read_only: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., unit: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
