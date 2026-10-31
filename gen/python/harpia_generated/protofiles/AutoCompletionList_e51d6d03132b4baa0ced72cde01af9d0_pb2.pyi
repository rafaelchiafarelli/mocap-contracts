from harpia_generated.protofiles import ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutoCompletionList(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "element", "enabled", "items"]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    element: _ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2.ScriptElement
    enabled: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2.ScriptElement, str]] = ..., enabled: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., items: _Optional[_Iterable[str]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
