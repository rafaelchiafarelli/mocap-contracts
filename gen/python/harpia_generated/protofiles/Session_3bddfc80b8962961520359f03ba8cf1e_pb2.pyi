from harpia_generated.protofiles import Actor_3bddfc80b8962961520359f03ba8cf1e_pb2 as _Actor_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import Character_3bddfc80b8962961520359f03ba8cf1e_pb2 as _Character_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import Casting_3bddfc80b8962961520359f03ba8cf1e_pb2 as _Casting_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_3bddfc80b8962961520359f03ba8cf1e_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_3bddfc80b8962961520359f03ba8cf1e_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_3bddfc80b8962961520359f03ba8cf1e_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_3bddfc80b8962961520359f03ba8cf1e_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_3bddfc80b8962961520359f03ba8cf1e_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_3bddfc80b8962961520359f03ba8cf1e_pb2.Casting, _Mapping]]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
