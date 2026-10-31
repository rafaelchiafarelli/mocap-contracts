from harpia_generated.protofiles import ScriptElement_186a1974c92f444f1bbc853569958a27_pb2 as _ScriptElement_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import TextStyle_186a1974c92f444f1bbc853569958a27_pb2 as _TextStyle_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementStyle(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "before_spacing_tenths", "element", "export", "indent_chars", "intra_spacing_tenths", "screen", "width_chars"]
    BEFORE_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    INDENT_CHARS_FIELD_NUMBER: _ClassVar[int]
    INTRA_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    WIDTH_CHARS_FIELD_NUMBER: _ClassVar[int]
    before_spacing_tenths: int
    element: _ScriptElement_186a1974c92f444f1bbc853569958a27_pb2.ScriptElement
    export: _TextStyle_186a1974c92f444f1bbc853569958a27_pb2.TextStyle
    indent_chars: int
    intra_spacing_tenths: int
    screen: _TextStyle_186a1974c92f444f1bbc853569958a27_pb2.TextStyle
    width_chars: int
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_186a1974c92f444f1bbc853569958a27_pb2.ScriptElement, str]] = ..., before_spacing_tenths: _Optional[int] = ..., intra_spacing_tenths: _Optional[int] = ..., indent_chars: _Optional[int] = ..., width_chars: _Optional[int] = ..., screen: _Optional[_Union[_TextStyle_186a1974c92f444f1bbc853569958a27_pb2.TextStyle, _Mapping]] = ..., export: _Optional[_Union[_TextStyle_186a1974c92f444f1bbc853569958a27_pb2.TextStyle, _Mapping]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
