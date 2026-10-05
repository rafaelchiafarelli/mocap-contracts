from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class contracts_placeholder(_message.Message):
    __slots__ = ["ERROR_fb15c485dc8666ed616f54252a0db38b", "ID_fb15c485dc8666ed616f54252a0db38b", "ORIGINATOR", "STATUS_fb15c485dc8666ed616f54252a0db38b", "note"]
    ERROR_FB15C485DC8666ED616F54252A0DB38B_FIELD_NUMBER: _ClassVar[int]
    ERROR_fb15c485dc8666ed616f54252a0db38b: str
    ID_FB15C485DC8666ED616F54252A0DB38B_FIELD_NUMBER: _ClassVar[int]
    ID_fb15c485dc8666ed616f54252a0db38b: int
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FB15C485DC8666ED616F54252A0DB38B_FIELD_NUMBER: _ClassVar[int]
    STATUS_fb15c485dc8666ed616f54252a0db38b: str
    note: str
    def __init__(self, ID_fb15c485dc8666ed616f54252a0db38b: _Optional[int] = ..., note: _Optional[str] = ..., STATUS_fb15c485dc8666ed616f54252a0db38b: _Optional[str] = ..., ERROR_fb15c485dc8666ed616f54252a0db38b: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
