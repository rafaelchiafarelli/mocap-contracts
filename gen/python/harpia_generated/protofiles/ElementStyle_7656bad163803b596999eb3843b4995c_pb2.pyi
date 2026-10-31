from harpia_generated.protofiles import ScriptElement_7656bad163803b596999eb3843b4995c_pb2 as _ScriptElement_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import TextStyle_7656bad163803b596999eb3843b4995c_pb2 as _TextStyle_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementStyle(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "before_spacing_tenths", "element", "export", "indent_chars", "intra_spacing_tenths", "screen", "width_chars"]
    BEFORE_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    INDENT_CHARS_FIELD_NUMBER: _ClassVar[int]
    INTRA_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    WIDTH_CHARS_FIELD_NUMBER: _ClassVar[int]
    before_spacing_tenths: int
    element: _ScriptElement_7656bad163803b596999eb3843b4995c_pb2.ScriptElement
    export: _TextStyle_7656bad163803b596999eb3843b4995c_pb2.TextStyle
    indent_chars: int
    intra_spacing_tenths: int
    screen: _TextStyle_7656bad163803b596999eb3843b4995c_pb2.TextStyle
    width_chars: int
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_7656bad163803b596999eb3843b4995c_pb2.ScriptElement, str]] = ..., before_spacing_tenths: _Optional[int] = ..., intra_spacing_tenths: _Optional[int] = ..., indent_chars: _Optional[int] = ..., width_chars: _Optional[int] = ..., screen: _Optional[_Union[_TextStyle_7656bad163803b596999eb3843b4995c_pb2.TextStyle, _Mapping]] = ..., export: _Optional[_Union[_TextStyle_7656bad163803b596999eb3843b4995c_pb2.TextStyle, _Mapping]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
