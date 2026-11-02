from harpia_generated.protofiles import BodyLength_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BodyLength_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "height_m", "id", "lengths", "name"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_M_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LENGTHS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    height_m: float
    id: str
    lengths: _containers.RepeatedCompositeFieldContainer[_BodyLength_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BodyLength]
    name: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., height_m: _Optional[float] = ..., lengths: _Optional[_Iterable[_Union[_BodyLength_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BodyLength, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
