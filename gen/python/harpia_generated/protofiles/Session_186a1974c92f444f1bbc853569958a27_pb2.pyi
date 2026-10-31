from harpia_generated.protofiles import Actor_186a1974c92f444f1bbc853569958a27_pb2 as _Actor_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Character_186a1974c92f444f1bbc853569958a27_pb2 as _Character_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Casting_186a1974c92f444f1bbc853569958a27_pb2 as _Casting_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_186a1974c92f444f1bbc853569958a27_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_186a1974c92f444f1bbc853569958a27_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_186a1974c92f444f1bbc853569958a27_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_186a1974c92f444f1bbc853569958a27_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_186a1974c92f444f1bbc853569958a27_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_186a1974c92f444f1bbc853569958a27_pb2.Casting, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
