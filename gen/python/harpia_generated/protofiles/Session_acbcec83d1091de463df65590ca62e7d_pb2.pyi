from harpia_generated.protofiles import Actor_acbcec83d1091de463df65590ca62e7d_pb2 as _Actor_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Character_acbcec83d1091de463df65590ca62e7d_pb2 as _Character_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Casting_acbcec83d1091de463df65590ca62e7d_pb2 as _Casting_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_acbcec83d1091de463df65590ca62e7d_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_acbcec83d1091de463df65590ca62e7d_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_acbcec83d1091de463df65590ca62e7d_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_acbcec83d1091de463df65590ca62e7d_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_acbcec83d1091de463df65590ca62e7d_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_acbcec83d1091de463df65590ca62e7d_pb2.Casting, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
