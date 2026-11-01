from harpia_generated.protofiles import TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import TitleFont_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TitleFont_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitleString(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "align", "bold", "font", "italic", "items", "size_pt", "underlined", "x_mm", "y_mm"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    FONT_FIELD_NUMBER: _ClassVar[int]
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_PT_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_MM_FIELD_NUMBER: _ClassVar[int]
    Y_MM_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextAlign
    bold: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    font: _TitleFont_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitleFont
    italic: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    items: _containers.RepeatedScalarFieldContainer[str]
    size_pt: int
    underlined: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    x_mm: float
    y_mm: float
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., items: _Optional[_Iterable[str]] = ..., x_mm: _Optional[float] = ..., y_mm: _Optional[float] = ..., size_pt: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., font: _Optional[_Union[_TitleFont_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitleFont, str]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
