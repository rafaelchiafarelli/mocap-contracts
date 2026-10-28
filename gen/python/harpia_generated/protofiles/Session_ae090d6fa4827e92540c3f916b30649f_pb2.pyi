from harpia_generated.protofiles import Actor_ae090d6fa4827e92540c3f916b30649f_pb2 as _Actor_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import Character_ae090d6fa4827e92540c3f916b30649f_pb2 as _Character_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import Casting_ae090d6fa4827e92540c3f916b30649f_pb2 as _Casting_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_ae090d6fa4827e92540c3f916b30649f_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_ae090d6fa4827e92540c3f916b30649f_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_ae090d6fa4827e92540c3f916b30649f_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_ae090d6fa4827e92540c3f916b30649f_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_ae090d6fa4827e92540c3f916b30649f_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_ae090d6fa4827e92540c3f916b30649f_pb2.Casting, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
