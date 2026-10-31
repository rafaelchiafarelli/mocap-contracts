from harpia_generated.protofiles import SceneChangeType_186a1974c92f444f1bbc853569958a27_pb2 as _SceneChangeType_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneChange(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "new_value", "old_value", "scene", "type"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    new_value: str
    old_value: str
    scene: str
    type: _SceneChangeType_186a1974c92f444f1bbc853569958a27_pb2.SceneChangeType
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., type: _Optional[_Union[_SceneChangeType_186a1974c92f444f1bbc853569958a27_pb2.SceneChangeType, str]] = ..., scene: _Optional[str] = ..., old_value: _Optional[str] = ..., new_value: _Optional[str] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
