from harpia_generated.protofiles import ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import TextStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _TextStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementStyle(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "before_spacing_tenths", "element", "export", "indent_chars", "intra_spacing_tenths", "screen", "width_chars"]
    BEFORE_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    INDENT_CHARS_FIELD_NUMBER: _ClassVar[int]
    INTRA_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    WIDTH_CHARS_FIELD_NUMBER: _ClassVar[int]
    before_spacing_tenths: int
    element: _ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2.ScriptElement
    export: _TextStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2.TextStyle
    indent_chars: int
    intra_spacing_tenths: int
    screen: _TextStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2.TextStyle
    width_chars: int
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_e51d6d03132b4baa0ced72cde01af9d0_pb2.ScriptElement, str]] = ..., before_spacing_tenths: _Optional[int] = ..., intra_spacing_tenths: _Optional[int] = ..., indent_chars: _Optional[int] = ..., width_chars: _Optional[int] = ..., screen: _Optional[_Union[_TextStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2.TextStyle, _Mapping]] = ..., export: _Optional[_Union[_TextStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2.TextStyle, _Mapping]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
