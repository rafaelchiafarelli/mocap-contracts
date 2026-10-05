from harpia_generated.protofiles import Flag_5f4d7690e05d3b2a18b01aae2e150601_pb2 as _Flag_5f4d7690e05d3b2a18b01aae2e150601_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlValue(_message.Message):
    __slots__ = ["ERROR_5f4d7690e05d3b2a18b01aae2e150601", "ID_5f4d7690e05d3b2a18b01aae2e150601", "ORIGINATOR", "STATUS_5f4d7690e05d3b2a18b01aae2e150601", "flag_value", "float_value", "float_values", "int_value", "int_values", "text_value"]
    ERROR_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    ERROR_5f4d7690e05d3b2a18b01aae2e150601: str
    FLAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ID_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    ID_5f4d7690e05d3b2a18b01aae2e150601: int
    INT_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_5F4D7690E05D3B2A18B01AAE2E150601_FIELD_NUMBER: _ClassVar[int]
    STATUS_5f4d7690e05d3b2a18b01aae2e150601: str
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    flag_value: _Flag_5f4d7690e05d3b2a18b01aae2e150601_pb2.Flag
    float_value: float
    float_values: _containers.RepeatedScalarFieldContainer[float]
    int_value: int
    int_values: _containers.RepeatedScalarFieldContainer[int]
    text_value: str
    def __init__(self, ID_5f4d7690e05d3b2a18b01aae2e150601: _Optional[int] = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., flag_value: _Optional[_Union[_Flag_5f4d7690e05d3b2a18b01aae2e150601_pb2.Flag, str]] = ..., text_value: _Optional[str] = ..., int_values: _Optional[_Iterable[int]] = ..., float_values: _Optional[_Iterable[float]] = ..., STATUS_5f4d7690e05d3b2a18b01aae2e150601: _Optional[str] = ..., ERROR_5f4d7690e05d3b2a18b01aae2e150601: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
