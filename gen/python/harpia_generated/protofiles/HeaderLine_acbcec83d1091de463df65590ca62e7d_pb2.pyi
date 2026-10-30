from harpia_generated.protofiles import TextAlign_acbcec83d1091de463df65590ca62e7d_pb2 as _TextAlign_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Flag_acbcec83d1091de463df65590ca62e7d_pb2 as _Flag_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderLine(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "align", "bold", "italic", "line", "text", "underlined", "x_offset_chars"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_OFFSET_CHARS_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_acbcec83d1091de463df65590ca62e7d_pb2.TextAlign
    bold: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    italic: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    line: int
    text: str
    underlined: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    x_offset_chars: int
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., line: _Optional[int] = ..., x_offset_chars: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_acbcec83d1091de463df65590ca62e7d_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., text: _Optional[str] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
