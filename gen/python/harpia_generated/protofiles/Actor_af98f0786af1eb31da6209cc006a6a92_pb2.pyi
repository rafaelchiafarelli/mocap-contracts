from harpia_generated.protofiles import BodyLength_af98f0786af1eb31da6209cc006a6a92_pb2 as _BodyLength_af98f0786af1eb31da6209cc006a6a92_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ["ERROR_af98f0786af1eb31da6209cc006a6a92", "ID_af98f0786af1eb31da6209cc006a6a92", "ORIGINATOR", "STATUS_af98f0786af1eb31da6209cc006a6a92", "height_m", "id", "lengths", "name"]
    ERROR_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    ERROR_af98f0786af1eb31da6209cc006a6a92: str
    HEIGHT_M_FIELD_NUMBER: _ClassVar[int]
    ID_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_af98f0786af1eb31da6209cc006a6a92: int
    LENGTHS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    STATUS_af98f0786af1eb31da6209cc006a6a92: str
    height_m: float
    id: str
    lengths: _containers.RepeatedCompositeFieldContainer[_BodyLength_af98f0786af1eb31da6209cc006a6a92_pb2.BodyLength]
    name: str
    def __init__(self, ID_af98f0786af1eb31da6209cc006a6a92: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., height_m: _Optional[float] = ..., lengths: _Optional[_Iterable[_Union[_BodyLength_af98f0786af1eb31da6209cc006a6a92_pb2.BodyLength, _Mapping]]] = ..., STATUS_af98f0786af1eb31da6209cc006a6a92: _Optional[str] = ..., ERROR_af98f0786af1eb31da6209cc006a6a92: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
