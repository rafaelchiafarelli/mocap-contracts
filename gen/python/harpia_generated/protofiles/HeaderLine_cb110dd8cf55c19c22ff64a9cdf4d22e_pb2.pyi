from harpia_generated.protofiles import TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderLine(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "align", "bold", "italic", "line", "text", "underlined", "x_offset_chars"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_OFFSET_CHARS_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextAlign
    bold: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    italic: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    line: int
    text: str
    underlined: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    x_offset_chars: int
    def __init__(self, HARPIA_ID: _Optional[int] = ..., line: _Optional[int] = ..., x_offset_chars: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., text: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
