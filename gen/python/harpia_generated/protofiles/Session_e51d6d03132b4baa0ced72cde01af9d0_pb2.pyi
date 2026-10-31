from harpia_generated.protofiles import Actor_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Actor_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import Character_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Character_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_e51d6d03132b4baa0ced72cde01af9d0_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_e51d6d03132b4baa0ced72cde01af9d0_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_e51d6d03132b4baa0ced72cde01af9d0_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_e51d6d03132b4baa0ced72cde01af9d0_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2.Casting, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
