from harpia_generated.protofiles import Actor_17f8b54225d6d535e6d691175cc18809_pb2 as _Actor_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import Character_17f8b54225d6d535e6d691175cc18809_pb2 as _Character_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import Casting_17f8b54225d6d535e6d691175cc18809_pb2 as _Casting_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_17f8b54225d6d535e6d691175cc18809_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_17f8b54225d6d535e6d691175cc18809_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_17f8b54225d6d535e6d691175cc18809_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_17f8b54225d6d535e6d691175cc18809_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_17f8b54225d6d535e6d691175cc18809_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_17f8b54225d6d535e6d691175cc18809_pb2.Casting, _Mapping]]] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
