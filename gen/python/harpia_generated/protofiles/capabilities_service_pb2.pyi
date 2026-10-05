from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class capabilities_Request(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class capabilities_Response(_message.Message):
    __slots__ = ["message_types"]
    MESSAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    message_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message_types: _Optional[_Iterable[str]] = ...) -> None: ...
