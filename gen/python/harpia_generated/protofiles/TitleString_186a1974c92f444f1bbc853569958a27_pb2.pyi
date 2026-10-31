from harpia_generated.protofiles import TextAlign_186a1974c92f444f1bbc853569958a27_pb2 as _TextAlign_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import TitleFont_186a1974c92f444f1bbc853569958a27_pb2 as _TitleFont_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitleString(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "align", "bold", "font", "italic", "items", "size_pt", "underlined", "x_mm", "y_mm"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FONT_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_PT_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_MM_FIELD_NUMBER: _ClassVar[int]
    Y_MM_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_186a1974c92f444f1bbc853569958a27_pb2.TextAlign
    bold: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    font: _TitleFont_186a1974c92f444f1bbc853569958a27_pb2.TitleFont
    italic: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    items: _containers.RepeatedScalarFieldContainer[str]
    size_pt: int
    underlined: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    x_mm: float
    y_mm: float
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., items: _Optional[_Iterable[str]] = ..., x_mm: _Optional[float] = ..., y_mm: _Optional[float] = ..., size_pt: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_186a1974c92f444f1bbc853569958a27_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., font: _Optional[_Union[_TitleFont_186a1974c92f444f1bbc853569958a27_pb2.TitleFont, str]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
