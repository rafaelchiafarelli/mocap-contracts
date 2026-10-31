from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pitch(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "include", "logline", "pitch", "target_audience"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    LOGLINE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TARGET_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    include: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    logline: str
    pitch: str
    target_audience: str
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., include: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., pitch: _Optional[str] = ..., logline: _Optional[str] = ..., target_audience: _Optional[str] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
