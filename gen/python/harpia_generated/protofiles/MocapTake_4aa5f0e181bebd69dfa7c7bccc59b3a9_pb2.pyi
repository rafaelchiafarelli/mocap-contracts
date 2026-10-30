from harpia_generated.protofiles import MocapTakeHeader_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _MocapTakeHeader_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import MocapFrame_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _MocapFrame_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "frames", "header"]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.MocapFrame]
    header: _MocapTakeHeader_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.MocapTakeHeader
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.MocapFrame, _Mapping]]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
