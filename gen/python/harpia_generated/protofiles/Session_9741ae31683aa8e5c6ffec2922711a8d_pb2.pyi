from harpia_generated.protofiles import Actor_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _Actor_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import Character_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _Character_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_9741ae31683aa8e5c6ffec2922711a8d_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_9741ae31683aa8e5c6ffec2922711a8d_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_9741ae31683aa8e5c6ffec2922711a8d_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_9741ae31683aa8e5c6ffec2922711a8d_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2.Casting, _Mapping]]] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
