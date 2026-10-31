from harpia_generated.protofiles import TextAlign_186a1974c92f444f1bbc853569958a27_pb2 as _TextAlign_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderLine(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "align", "bold", "italic", "line", "text", "underlined", "x_offset_chars"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_OFFSET_CHARS_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_186a1974c92f444f1bbc853569958a27_pb2.TextAlign
    bold: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    italic: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    line: int
    text: str
    underlined: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    x_offset_chars: int
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., line: _Optional[int] = ..., x_offset_chars: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_186a1974c92f444f1bbc853569958a27_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., text: _Optional[str] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
