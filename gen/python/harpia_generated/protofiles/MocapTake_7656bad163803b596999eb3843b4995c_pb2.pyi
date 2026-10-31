from harpia_generated.protofiles import MocapTakeHeader_7656bad163803b596999eb3843b4995c_pb2 as _MocapTakeHeader_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import MocapFrame_7656bad163803b596999eb3843b4995c_pb2 as _MocapFrame_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "frames", "header"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_7656bad163803b596999eb3843b4995c_pb2.MocapFrame]
    header: _MocapTakeHeader_7656bad163803b596999eb3843b4995c_pb2.MocapTakeHeader
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_7656bad163803b596999eb3843b4995c_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_7656bad163803b596999eb3843b4995c_pb2.MocapFrame, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
