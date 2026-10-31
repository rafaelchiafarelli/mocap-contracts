from harpia_generated.protofiles import SceneCharacter_186a1974c92f444f1bbc853569958a27_pb2 as _SceneCharacter_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import SceneProp_186a1974c92f444f1bbc853569958a27_pb2 as _SceneProp_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntry(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "characters", "first_line", "first_page", "int_ext", "last_line", "last_page", "location", "order", "props", "scene", "set_id", "text_hash", "time_of_day"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FIRST_LINE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    INT_EXT_FIELD_NUMBER: _ClassVar[int]
    LAST_LINE_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    SET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TEXT_HASH_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[_SceneCharacter_186a1974c92f444f1bbc853569958a27_pb2.SceneCharacter]
    first_line: int
    first_page: int
    int_ext: str
    last_line: int
    last_page: int
    location: str
    order: int
    props: _containers.RepeatedCompositeFieldContainer[_SceneProp_186a1974c92f444f1bbc853569958a27_pb2.SceneProp]
    scene: str
    set_id: str
    text_hash: str
    time_of_day: str
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., scene: _Optional[str] = ..., order: _Optional[int] = ..., int_ext: _Optional[str] = ..., location: _Optional[str] = ..., time_of_day: _Optional[str] = ..., set_id: _Optional[str] = ..., characters: _Optional[_Iterable[_Union[_SceneCharacter_186a1974c92f444f1bbc853569958a27_pb2.SceneCharacter, _Mapping]]] = ..., props: _Optional[_Iterable[_Union[_SceneProp_186a1974c92f444f1bbc853569958a27_pb2.SceneProp, _Mapping]]] = ..., first_page: _Optional[int] = ..., last_page: _Optional[int] = ..., first_line: _Optional[int] = ..., last_line: _Optional[int] = ..., text_hash: _Optional[str] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
