from harpia_generated.protofiles import BodyLength_17f8b54225d6d535e6d691175cc18809_pb2 as _BodyLength_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "height_m", "id", "lengths", "name"]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    HEIGHT_M_FIELD_NUMBER: _ClassVar[int]
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    ID_FIELD_NUMBER: _ClassVar[int]
    LENGTHS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    height_m: float
    id: str
    lengths: _containers.RepeatedCompositeFieldContainer[_BodyLength_17f8b54225d6d535e6d691175cc18809_pb2.BodyLength]
    name: str
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., height_m: _Optional[float] = ..., lengths: _Optional[_Iterable[_Union[_BodyLength_17f8b54225d6d535e6d691175cc18809_pb2.BodyLength, _Mapping]]] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
