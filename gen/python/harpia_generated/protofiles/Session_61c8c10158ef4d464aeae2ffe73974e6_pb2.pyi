from harpia_generated.protofiles import Actor_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _Actor_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import Character_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _Character_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_61c8c10158ef4d464aeae2ffe73974e6_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_61c8c10158ef4d464aeae2ffe73974e6_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_61c8c10158ef4d464aeae2ffe73974e6_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_61c8c10158ef4d464aeae2ffe73974e6_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2.Casting, _Mapping]]] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
