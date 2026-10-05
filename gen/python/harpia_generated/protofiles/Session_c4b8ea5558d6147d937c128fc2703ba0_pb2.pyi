from harpia_generated.protofiles import Actor_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Actor_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import Character_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Character_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_c4b8ea5558d6147d937c128fc2703ba0_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_c4b8ea5558d6147d937c128fc2703ba0_pb2.Character]
    date: str
    id: str
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_c4b8ea5558d6147d937c128fc2703ba0_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_c4b8ea5558d6147d937c128fc2703ba0_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2.Casting, _Mapping]]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
