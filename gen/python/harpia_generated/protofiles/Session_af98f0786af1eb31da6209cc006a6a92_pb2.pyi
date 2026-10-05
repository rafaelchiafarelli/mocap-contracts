from harpia_generated.protofiles import Actor_af98f0786af1eb31da6209cc006a6a92_pb2 as _Actor_af98f0786af1eb31da6209cc006a6a92_pb2
from harpia_generated.protofiles import Character_af98f0786af1eb31da6209cc006a6a92_pb2 as _Character_af98f0786af1eb31da6209cc006a6a92_pb2
from harpia_generated.protofiles import Casting_af98f0786af1eb31da6209cc006a6a92_pb2 as _Casting_af98f0786af1eb31da6209cc006a6a92_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_af98f0786af1eb31da6209cc006a6a92", "ID_af98f0786af1eb31da6209cc006a6a92", "ORIGINATOR", "STATUS_af98f0786af1eb31da6209cc006a6a92", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    ERROR_af98f0786af1eb31da6209cc006a6a92: str
    ID_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_af98f0786af1eb31da6209cc006a6a92: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_AF98F0786AF1EB31DA6209CC006A6A92_FIELD_NUMBER: _ClassVar[int]
    STATUS_af98f0786af1eb31da6209cc006a6a92: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_af98f0786af1eb31da6209cc006a6a92_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_af98f0786af1eb31da6209cc006a6a92_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_af98f0786af1eb31da6209cc006a6a92_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_af98f0786af1eb31da6209cc006a6a92: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_af98f0786af1eb31da6209cc006a6a92_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_af98f0786af1eb31da6209cc006a6a92_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_af98f0786af1eb31da6209cc006a6a92_pb2.Casting, _Mapping]]] = ..., STATUS_af98f0786af1eb31da6209cc006a6a92: _Optional[str] = ..., ERROR_af98f0786af1eb31da6209cc006a6a92: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
