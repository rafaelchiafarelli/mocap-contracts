from harpia_generated.protofiles import Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Argument(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "include", "text"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    include: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    text: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., include: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., text: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
