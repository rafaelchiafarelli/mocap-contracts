from harpia_generated.protofiles import Actor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Actor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Character_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Character_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "actors", "casting", "characters", "date", "id"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[_Actor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Actor]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Casting]
    characters: _containers.RepeatedCompositeFieldContainer[_Character_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Character]
    date: str
    id: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., id: _Optional[str] = ..., date: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[_Actor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Actor, _Mapping]]] = ..., characters: _Optional[_Iterable[_Union[_Character_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Character, _Mapping]]] = ..., casting: _Optional[_Iterable[_Union[_Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Casting, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
