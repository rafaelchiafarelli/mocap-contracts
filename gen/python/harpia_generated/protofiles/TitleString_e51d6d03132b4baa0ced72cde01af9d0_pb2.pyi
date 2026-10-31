from harpia_generated.protofiles import TextAlign_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _TextAlign_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import TitleFont_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _TitleFont_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitleString(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "align", "bold", "font", "italic", "items", "size_pt", "underlined", "x_mm", "y_mm"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FONT_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_PT_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_MM_FIELD_NUMBER: _ClassVar[int]
    Y_MM_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_e51d6d03132b4baa0ced72cde01af9d0_pb2.TextAlign
    bold: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    font: _TitleFont_e51d6d03132b4baa0ced72cde01af9d0_pb2.TitleFont
    italic: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    items: _containers.RepeatedScalarFieldContainer[str]
    size_pt: int
    underlined: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    x_mm: float
    y_mm: float
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., items: _Optional[_Iterable[str]] = ..., x_mm: _Optional[float] = ..., y_mm: _Optional[float] = ..., size_pt: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_e51d6d03132b4baa0ced72cde01af9d0_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., font: _Optional[_Union[_TitleFont_e51d6d03132b4baa0ced72cde01af9d0_pb2.TitleFont, str]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
