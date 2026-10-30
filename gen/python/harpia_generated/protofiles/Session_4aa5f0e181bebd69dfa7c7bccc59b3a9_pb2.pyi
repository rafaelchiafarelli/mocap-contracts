from harpia_generated.protofiles import Actor_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Actor_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import Character_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Character_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import Casting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Casting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Casting, _Mapping]]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
