from harpia_generated.protofiles import ScriptElement_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ScriptElement_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import TextStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TextStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementStyle(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "before_spacing_tenths", "element", "export", "indent_chars", "intra_spacing_tenths", "screen", "width_chars"]
    BEFORE_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    INDENT_CHARS_FIELD_NUMBER: _ClassVar[int]
    INTRA_SPACING_TENTHS_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    WIDTH_CHARS_FIELD_NUMBER: _ClassVar[int]
    before_spacing_tenths: int
    element: _ScriptElement_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ScriptElement
    export: _TextStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextStyle
    indent_chars: int
    intra_spacing_tenths: int
    screen: _TextStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextStyle
    width_chars: int
    def __init__(self, HARPIA_ID: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ScriptElement, str]] = ..., before_spacing_tenths: _Optional[int] = ..., intra_spacing_tenths: _Optional[int] = ..., indent_chars: _Optional[int] = ..., width_chars: _Optional[int] = ..., screen: _Optional[_Union[_TextStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextStyle, _Mapping]] = ..., export: _Optional[_Union[_TextStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextStyle, _Mapping]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
