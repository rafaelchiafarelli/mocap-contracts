from harpia_generated.protofiles import SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneChange(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "new_value", "old_value", "scene", "type"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    new_value: str
    old_value: str
    scene: str
    type: _SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneChangeType
    def __init__(self, HARPIA_ID: _Optional[int] = ..., type: _Optional[_Union[_SceneChangeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SceneChangeType, str]] = ..., scene: _Optional[str] = ..., old_value: _Optional[str] = ..., new_value: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
