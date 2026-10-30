from harpia_generated.protofiles import ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2 as _ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Flag_acbcec83d1091de463df65590ca62e7d_pb2 as _Flag_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutoCompletionList(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "element", "enabled", "items"]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    element: _ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2.ScriptElement
    enabled: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2.ScriptElement, str]] = ..., enabled: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., items: _Optional[_Iterable[str]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
