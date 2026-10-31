from harpia_generated.protofiles import AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2 as _AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import AnnotationAnchor_186a1974c92f444f1bbc853569958a27_pb2 as _AnnotationAnchor_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import BibleValue_186a1974c92f444f1bbc853569958a27_pb2 as _BibleValue_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Annotation(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "anchor", "by", "id", "kind", "shot", "text", "values"]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SHOT_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    anchor: _AnnotationAnchor_186a1974c92f444f1bbc853569958a27_pb2.AnnotationAnchor
    by: str
    id: str
    kind: _AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2.AnnotationKind
    shot: int
    text: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_186a1974c92f444f1bbc853569958a27_pb2.BibleValue]
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., id: _Optional[str] = ..., kind: _Optional[_Union[_AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2.AnnotationKind, str]] = ..., anchor: _Optional[_Union[_AnnotationAnchor_186a1974c92f444f1bbc853569958a27_pb2.AnnotationAnchor, _Mapping]] = ..., text: _Optional[str] = ..., by: _Optional[str] = ..., shot: _Optional[int] = ..., values: _Optional[_Iterable[_Union[_BibleValue_186a1974c92f444f1bbc853569958a27_pb2.BibleValue, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
