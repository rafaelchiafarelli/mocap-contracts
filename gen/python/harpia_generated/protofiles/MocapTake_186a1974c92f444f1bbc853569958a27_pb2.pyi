from harpia_generated.protofiles import MocapTakeHeader_186a1974c92f444f1bbc853569958a27_pb2 as _MocapTakeHeader_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import MocapFrame_186a1974c92f444f1bbc853569958a27_pb2 as _MocapFrame_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "frames", "header"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_186a1974c92f444f1bbc853569958a27_pb2.MocapFrame]
    header: _MocapTakeHeader_186a1974c92f444f1bbc853569958a27_pb2.MocapTakeHeader
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_186a1974c92f444f1bbc853569958a27_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_186a1974c92f444f1bbc853569958a27_pb2.MocapFrame, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
