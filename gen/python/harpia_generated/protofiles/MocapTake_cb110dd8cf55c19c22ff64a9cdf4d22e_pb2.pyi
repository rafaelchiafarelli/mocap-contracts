from harpia_generated.protofiles import MocapTakeHeader_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _MocapTakeHeader_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import MocapFrame_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _MocapFrame_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "frames", "header"]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.MocapFrame]
    header: _MocapTakeHeader_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.MocapTakeHeader
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.MocapFrame, _Mapping]]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
