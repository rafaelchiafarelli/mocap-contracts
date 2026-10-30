from harpia_generated.protofiles import Flag_acbcec83d1091de463df65590ca62e7d_pb2 as _Flag_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageSettings(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "font_size_pt", "margin_bottom_mm", "margin_left_mm", "margin_right_mm", "margin_top_mm", "page_break_action_lines", "page_break_dialogue_lines", "paper_height_mm", "paper_width_mm", "scene_continued_indent_chars", "scene_continueds"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    FONT_SIZE_PT_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    MARGIN_BOTTOM_MM_FIELD_NUMBER: _ClassVar[int]
    MARGIN_LEFT_MM_FIELD_NUMBER: _ClassVar[int]
    MARGIN_RIGHT_MM_FIELD_NUMBER: _ClassVar[int]
    MARGIN_TOP_MM_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_BREAK_ACTION_LINES_FIELD_NUMBER: _ClassVar[int]
    PAGE_BREAK_DIALOGUE_LINES_FIELD_NUMBER: _ClassVar[int]
    PAPER_HEIGHT_MM_FIELD_NUMBER: _ClassVar[int]
    PAPER_WIDTH_MM_FIELD_NUMBER: _ClassVar[int]
    SCENE_CONTINUEDS_FIELD_NUMBER: _ClassVar[int]
    SCENE_CONTINUED_INDENT_CHARS_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    font_size_pt: int
    margin_bottom_mm: float
    margin_left_mm: float
    margin_right_mm: float
    margin_top_mm: float
    page_break_action_lines: int
    page_break_dialogue_lines: int
    paper_height_mm: float
    paper_width_mm: float
    scene_continued_indent_chars: int
    scene_continueds: _Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., paper_width_mm: _Optional[float] = ..., paper_height_mm: _Optional[float] = ..., margin_top_mm: _Optional[float] = ..., margin_bottom_mm: _Optional[float] = ..., margin_left_mm: _Optional[float] = ..., margin_right_mm: _Optional[float] = ..., font_size_pt: _Optional[int] = ..., page_break_action_lines: _Optional[int] = ..., page_break_dialogue_lines: _Optional[int] = ..., scene_continueds: _Optional[_Union[_Flag_acbcec83d1091de463df65590ca62e7d_pb2.Flag, str]] = ..., scene_continued_indent_chars: _Optional[int] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
