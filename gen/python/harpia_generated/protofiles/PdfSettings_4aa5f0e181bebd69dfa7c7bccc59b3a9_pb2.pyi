from harpia_generated.protofiles import Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PdfSettings(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "bold", "bold_italic", "include_toc", "italic", "normal", "open_on_current_page", "outline_notes", "remove_notes", "show_line_numbers", "show_margins", "show_scene_numbers", "show_toc"]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    BOLD_ITALIC_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    INCLUDE_TOC_FIELD_NUMBER: _ClassVar[int]
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    OPEN_ON_CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OUTLINE_NOTES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_NOTES_FIELD_NUMBER: _ClassVar[int]
    SHOW_LINE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    SHOW_MARGINS_FIELD_NUMBER: _ClassVar[int]
    SHOW_SCENE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    SHOW_TOC_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    bold: _PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont
    bold_italic: _PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont
    include_toc: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    italic: _PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont
    normal: _PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont
    open_on_current_page: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    outline_notes: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    remove_notes: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    show_line_numbers: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    show_margins: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    show_scene_numbers: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    show_toc: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., show_scene_numbers: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., include_toc: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., show_toc: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., open_on_current_page: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., remove_notes: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., outline_notes: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., show_margins: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., show_line_numbers: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., normal: _Optional[_Union[_PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont, _Mapping]] = ..., bold: _Optional[_Union[_PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont, _Mapping]] = ..., italic: _Optional[_Union[_PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont, _Mapping]] = ..., bold_italic: _Optional[_Union[_PdfFont_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PdfFont, _Mapping]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
