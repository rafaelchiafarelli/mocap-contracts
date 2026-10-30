from harpia_generated.protofiles import ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2 as _ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import TextStyle_acbcec83d1091de463df65590ca62e7d_pb2 as _TextStyle_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementStyle(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "before_spacing_tenths", "element", "export", "indent_chars", "intra_spacing_tenths", "screen", "width_chars"]
    BEFORE_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    INDENT_CHARS_FIELD_NUMBER: _ClassVar[int]
    INTRA_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    WIDTH_CHARS_FIELD_NUMBER: _ClassVar[int]
    before_spacing_tenths: int
    element: _ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2.ScriptElement
    export: _TextStyle_acbcec83d1091de463df65590ca62e7d_pb2.TextStyle
    indent_chars: int
    intra_spacing_tenths: int
    screen: _TextStyle_acbcec83d1091de463df65590ca62e7d_pb2.TextStyle
    width_chars: int
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_acbcec83d1091de463df65590ca62e7d_pb2.ScriptElement, str]] = ..., before_spacing_tenths: _Optional[int] = ..., intra_spacing_tenths: _Optional[int] = ..., indent_chars: _Optional[int] = ..., width_chars: _Optional[int] = ..., screen: _Optional[_Union[_TextStyle_acbcec83d1091de463df65590ca62e7d_pb2.TextStyle, _Mapping]] = ..., export: _Optional[_Union[_TextStyle_acbcec83d1091de463df65590ca62e7d_pb2.TextStyle, _Mapping]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
