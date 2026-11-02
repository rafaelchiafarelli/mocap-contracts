from harpia_generated.protofiles import AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogKind(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "groups", "kind"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CatalogGroup]
    kind: _AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AnnotationKind
    def __init__(self, HARPIA_ID: _Optional[int] = ..., kind: _Optional[_Union[_AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AnnotationKind, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CatalogGroup, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
