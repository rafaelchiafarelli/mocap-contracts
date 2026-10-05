from harpia_generated.protofiles import BodyLength_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _BodyLength_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "height_m", "id", "lengths", "name"]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    HEIGHT_M_FIELD_NUMBER: _ClassVar[int]
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    ID_FIELD_NUMBER: _ClassVar[int]
    LENGTHS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    height_m: float
    id: str
    lengths: _containers.RepeatedCompositeFieldContainer[_BodyLength_9741ae31683aa8e5c6ffec2922711a8d_pb2.BodyLength]
    name: str
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., height_m: _Optional[float] = ..., lengths: _Optional[_Iterable[_Union[_BodyLength_9741ae31683aa8e5c6ffec2922711a8d_pb2.BodyLength, _Mapping]]] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
