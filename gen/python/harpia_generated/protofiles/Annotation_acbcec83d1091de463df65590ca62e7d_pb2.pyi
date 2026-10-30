from harpia_generated.protofiles import AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2 as _AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import AnnotationAnchor_acbcec83d1091de463df65590ca62e7d_pb2 as _AnnotationAnchor_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import BibleValue_acbcec83d1091de463df65590ca62e7d_pb2 as _BibleValue_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Annotation(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "anchor", "by", "id", "kind", "shot", "text", "values"]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SHOT_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    anchor: _AnnotationAnchor_acbcec83d1091de463df65590ca62e7d_pb2.AnnotationAnchor
    by: str
    id: str
    kind: _AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2.AnnotationKind
    shot: int
    text: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_acbcec83d1091de463df65590ca62e7d_pb2.BibleValue]
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., id: _Optional[str] = ..., kind: _Optional[_Union[_AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2.AnnotationKind, str]] = ..., anchor: _Optional[_Union[_AnnotationAnchor_acbcec83d1091de463df65590ca62e7d_pb2.AnnotationAnchor, _Mapping]] = ..., text: _Optional[str] = ..., by: _Optional[str] = ..., shot: _Optional[int] = ..., values: _Optional[_Iterable[_Union[_BibleValue_acbcec83d1091de463df65590ca62e7d_pb2.BibleValue, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
