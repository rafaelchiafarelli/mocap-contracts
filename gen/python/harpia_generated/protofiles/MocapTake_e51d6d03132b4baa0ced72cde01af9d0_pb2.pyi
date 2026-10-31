from harpia_generated.protofiles import MocapTakeHeader_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _MocapTakeHeader_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import MocapFrame_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _MocapFrame_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "frames", "header"]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_e51d6d03132b4baa0ced72cde01af9d0_pb2.MocapFrame]
    header: _MocapTakeHeader_e51d6d03132b4baa0ced72cde01af9d0_pb2.MocapTakeHeader
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_e51d6d03132b4baa0ced72cde01af9d0_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_e51d6d03132b4baa0ced72cde01af9d0_pb2.MocapFrame, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
