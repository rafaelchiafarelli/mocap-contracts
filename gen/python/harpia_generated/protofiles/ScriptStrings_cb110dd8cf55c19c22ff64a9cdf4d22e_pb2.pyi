from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptStrings(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "continued_page_end", "continued_page_start", "dialogue_continued", "more"]
    CONTINUED_PAGE_END_FIELD_NUMBER: _ClassVar[int]
    CONTINUED_PAGE_START_FIELD_NUMBER: _ClassVar[int]
    DIALOGUE_CONTINUED_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    MORE_FIELD_NUMBER: _ClassVar[int]
    continued_page_end: str
    continued_page_start: str
    dialogue_continued: str
    more: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., more: _Optional[str] = ..., continued_page_end: _Optional[str] = ..., continued_page_start: _Optional[str] = ..., dialogue_continued: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
