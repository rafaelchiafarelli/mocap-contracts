from harpia_generated.protofiles import SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneChange(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "new_value", "old_value", "scene", "type"]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    new_value: str
    old_value: str
    scene: str
    type: _SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneChangeType
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., type: _Optional[_Union[_SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneChangeType, str]] = ..., scene: _Optional[str] = ..., old_value: _Optional[str] = ..., new_value: _Optional[str] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
