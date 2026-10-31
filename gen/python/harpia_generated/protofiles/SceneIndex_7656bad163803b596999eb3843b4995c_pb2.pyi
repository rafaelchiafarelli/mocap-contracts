from harpia_generated.protofiles import SceneEntry_7656bad163803b596999eb3843b4995c_pb2 as _SceneEntry_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneIndex(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "scenes", "script_hash"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCENES_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_HASH_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    scenes: _containers.RepeatedCompositeFieldContainer[_SceneEntry_7656bad163803b596999eb3843b4995c_pb2.SceneEntry]
    script_hash: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., script_hash: _Optional[str] = ..., scenes: _Optional[_Iterable[_Union[_SceneEntry_7656bad163803b596999eb3843b4995c_pb2.SceneEntry, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
