from harpia_generated.protofiles import SceneChange_186a1974c92f444f1bbc853569958a27_pb2 as _SceneChange_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeSet(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "changes", "from_hash", "time", "to_hash"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FROM_HASH_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_HASH_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[_SceneChange_186a1974c92f444f1bbc853569958a27_pb2.SceneChange]
    from_hash: str
    time: str
    to_hash: str
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., time: _Optional[str] = ..., from_hash: _Optional[str] = ..., to_hash: _Optional[str] = ..., changes: _Optional[_Iterable[_Union[_SceneChange_186a1974c92f444f1bbc853569958a27_pb2.SceneChange, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
