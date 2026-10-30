from harpia_generated.protofiles import Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageSettings(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "font_size_pt", "margin_bottom_mm", "margin_left_mm", "margin_right_mm", "margin_top_mm", "page_break_action_lines", "page_break_dialogue_lines", "paper_height_mm", "paper_width_mm", "scene_continued_indent_chars", "scene_continueds"]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    FONT_SIZE_PT_FIELD_NUMBER: _ClassVar[int]
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
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
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
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
    scene_continueds: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., paper_width_mm: _Optional[float] = ..., paper_height_mm: _Optional[float] = ..., margin_top_mm: _Optional[float] = ..., margin_bottom_mm: _Optional[float] = ..., margin_left_mm: _Optional[float] = ..., margin_right_mm: _Optional[float] = ..., font_size_pt: _Optional[int] = ..., page_break_action_lines: _Optional[int] = ..., page_break_dialogue_lines: _Optional[int] = ..., scene_continueds: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., scene_continued_indent_chars: _Optional[int] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
