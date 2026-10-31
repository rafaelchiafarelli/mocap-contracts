from harpia_generated.protofiles import AnnotationKind_7656bad163803b596999eb3843b4995c_pb2 as _AnnotationKind_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import AnnotationAnchor_7656bad163803b596999eb3843b4995c_pb2 as _AnnotationAnchor_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import BibleValue_7656bad163803b596999eb3843b4995c_pb2 as _BibleValue_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Annotation(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "anchor", "by", "id", "kind", "shot", "text", "values"]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SHOT_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    anchor: _AnnotationAnchor_7656bad163803b596999eb3843b4995c_pb2.AnnotationAnchor
    by: str
    id: str
    kind: _AnnotationKind_7656bad163803b596999eb3843b4995c_pb2.AnnotationKind
    shot: int
    text: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_7656bad163803b596999eb3843b4995c_pb2.BibleValue]
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., id: _Optional[str] = ..., kind: _Optional[_Union[_AnnotationKind_7656bad163803b596999eb3843b4995c_pb2.AnnotationKind, str]] = ..., anchor: _Optional[_Union[_AnnotationAnchor_7656bad163803b596999eb3843b4995c_pb2.AnnotationAnchor, _Mapping]] = ..., text: _Optional[str] = ..., by: _Optional[str] = ..., shot: _Optional[int] = ..., values: _Optional[_Iterable[_Union[_BibleValue_7656bad163803b596999eb3843b4995c_pb2.BibleValue, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
