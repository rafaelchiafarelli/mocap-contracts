from harpia_generated.protofiles import Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlValue(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "flag_value", "float_value", "float_values", "int_value", "int_values", "text_value"]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    FLAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    INT_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    flag_value: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    float_value: float
    float_values: _containers.RepeatedScalarFieldContainer[float]
    int_value: int
    int_values: _containers.RepeatedScalarFieldContainer[int]
    text_value: str
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., flag_value: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., text_value: _Optional[str] = ..., int_values: _Optional[_Iterable[int]] = ..., float_values: _Optional[_Iterable[float]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
