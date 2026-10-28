from harpia_generated.protofiles import Actor_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Actor_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import Character_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Character_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import Casting_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Casting_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_136996d09eedbf0a12cec4204d8d4ec2_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_136996d09eedbf0a12cec4204d8d4ec2_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_136996d09eedbf0a12cec4204d8d4ec2_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_136996d09eedbf0a12cec4204d8d4ec2_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_136996d09eedbf0a12cec4204d8d4ec2_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_136996d09eedbf0a12cec4204d8d4ec2_pb2.Casting, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
