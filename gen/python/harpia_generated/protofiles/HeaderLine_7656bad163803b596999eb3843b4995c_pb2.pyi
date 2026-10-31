from harpia_generated.protofiles import TextAlign_7656bad163803b596999eb3843b4995c_pb2 as _TextAlign_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import Flag_7656bad163803b596999eb3843b4995c_pb2 as _Flag_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderLine(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "align", "bold", "italic", "line", "text", "underlined", "x_offset_chars"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_OFFSET_CHARS_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_7656bad163803b596999eb3843b4995c_pb2.TextAlign
    bold: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    italic: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    line: int
    text: str
    underlined: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    x_offset_chars: int
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., line: _Optional[int] = ..., x_offset_chars: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_7656bad163803b596999eb3843b4995c_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., text: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
