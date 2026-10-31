from harpia_generated.protofiles import Flag_7656bad163803b596999eb3843b4995c_pb2 as _Flag_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlValue(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "flag_value", "float_value", "float_values", "int_value", "int_values", "text_value"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    FLAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    INT_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    flag_value: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    float_value: float
    float_values: _containers.RepeatedScalarFieldContainer[float]
    int_value: int
    int_values: _containers.RepeatedScalarFieldContainer[int]
    text_value: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., flag_value: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., text_value: _Optional[str] = ..., int_values: _Optional[_Iterable[int]] = ..., float_values: _Optional[_Iterable[float]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
