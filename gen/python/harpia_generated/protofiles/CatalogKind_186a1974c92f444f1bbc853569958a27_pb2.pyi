from harpia_generated.protofiles import AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2 as _AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import CatalogGroup_186a1974c92f444f1bbc853569958a27_pb2 as _CatalogGroup_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogKind(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "groups", "kind"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_186a1974c92f444f1bbc853569958a27_pb2.CatalogGroup]
    kind: _AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2.AnnotationKind
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., kind: _Optional[_Union[_AnnotationKind_186a1974c92f444f1bbc853569958a27_pb2.AnnotationKind, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_186a1974c92f444f1bbc853569958a27_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
