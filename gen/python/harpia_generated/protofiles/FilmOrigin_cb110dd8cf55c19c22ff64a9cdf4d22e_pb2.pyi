from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FilmOrigin(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "program", "version"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    program: str
    version: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., program: _Optional[str] = ..., version: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
