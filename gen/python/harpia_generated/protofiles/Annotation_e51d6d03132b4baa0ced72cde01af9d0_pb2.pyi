from harpia_generated.protofiles import AnnotationKind_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _AnnotationKind_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import AnnotationAnchor_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _AnnotationAnchor_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Annotation(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "anchor", "by", "id", "kind", "shot", "text", "values"]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SHOT_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    anchor: _AnnotationAnchor_e51d6d03132b4baa0ced72cde01af9d0_pb2.AnnotationAnchor
    by: str
    id: str
    kind: _AnnotationKind_e51d6d03132b4baa0ced72cde01af9d0_pb2.AnnotationKind
    shot: int
    text: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleValue]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., id: _Optional[str] = ..., kind: _Optional[_Union[_AnnotationKind_e51d6d03132b4baa0ced72cde01af9d0_pb2.AnnotationKind, str]] = ..., anchor: _Optional[_Union[_AnnotationAnchor_e51d6d03132b4baa0ced72cde01af9d0_pb2.AnnotationAnchor, _Mapping]] = ..., text: _Optional[str] = ..., by: _Optional[str] = ..., shot: _Optional[int] = ..., values: _Optional[_Iterable[_Union[_BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleValue, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
