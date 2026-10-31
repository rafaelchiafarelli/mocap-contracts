from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptStrings(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "continued_page_end", "continued_page_start", "dialogue_continued", "more"]
    CONTINUED_PAGE_END_FIELD_NUMBER: _ClassVar[int]
    CONTINUED_PAGE_START_FIELD_NUMBER: _ClassVar[int]
    DIALOGUE_CONTINUED_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    MORE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    continued_page_end: str
    continued_page_start: str
    dialogue_continued: str
    more: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., more: _Optional[str] = ..., continued_page_end: _Optional[str] = ..., continued_page_start: _Optional[str] = ..., dialogue_continued: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
