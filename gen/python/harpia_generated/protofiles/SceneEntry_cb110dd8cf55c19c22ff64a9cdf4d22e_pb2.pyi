from harpia_generated.protofiles import SceneCharacter_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SceneCharacter_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import SceneProp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SceneProp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntry(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "characters", "first_line", "first_page", "int_ext", "last_line", "last_page", "location", "order", "props", "scene", "set_id", "text_hash", "time_of_day"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    FIRST_LINE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    INT_EXT_FIELD_NUMBER: _ClassVar[int]
    LAST_LINE_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_HASH_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[_SceneCharacter_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneCharacter]
    first_line: int
    first_page: int
    int_ext: str
    last_line: int
    last_page: int
    location: str
    order: int
    props: _containers.RepeatedCompositeFieldContainer[_SceneProp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneProp]
    scene: str
    set_id: str
    text_hash: str
    time_of_day: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., scene: _Optional[str] = ..., order: _Optional[int] = ..., int_ext: _Optional[str] = ..., location: _Optional[str] = ..., time_of_day: _Optional[str] = ..., set_id: _Optional[str] = ..., characters: _Optional[_Iterable[_Union[_SceneCharacter_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneCharacter, _Mapping]]] = ..., props: _Optional[_Iterable[_Union[_SceneProp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneProp, _Mapping]]] = ..., first_page: _Optional[int] = ..., last_page: _Optional[int] = ..., first_line: _Optional[int] = ..., last_line: _Optional[int] = ..., text_hash: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
