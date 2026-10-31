from harpia_generated.protofiles import Actor_7656bad163803b596999eb3843b4995c_pb2 as _Actor_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import Character_7656bad163803b596999eb3843b4995c_pb2 as _Character_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import Casting_7656bad163803b596999eb3843b4995c_pb2 as _Casting_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_7656bad163803b596999eb3843b4995c_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_7656bad163803b596999eb3843b4995c_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_7656bad163803b596999eb3843b4995c_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_7656bad163803b596999eb3843b4995c_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_7656bad163803b596999eb3843b4995c_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_7656bad163803b596999eb3843b4995c_pb2.Casting, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
