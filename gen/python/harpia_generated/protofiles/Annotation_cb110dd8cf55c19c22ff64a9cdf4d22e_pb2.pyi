from harpia_generated.protofiles import AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import AnnotationAnchor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _AnnotationAnchor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Annotation(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "anchor", "by", "id", "kind", "shot", "text", "values"]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SHOT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    anchor: _AnnotationAnchor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AnnotationAnchor
    by: str
    id: str
    kind: _AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AnnotationKind
    shot: int
    text: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleValue]
    def __init__(self, HARPIA_ID: _Optional[int] = ..., id: _Optional[str] = ..., kind: _Optional[_Union[_AnnotationKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AnnotationKind, str]] = ..., anchor: _Optional[_Union[_AnnotationAnchor_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AnnotationAnchor, _Mapping]] = ..., text: _Optional[str] = ..., by: _Optional[str] = ..., shot: _Optional[int] = ..., values: _Optional[_Iterable[_Union[_BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleValue, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
