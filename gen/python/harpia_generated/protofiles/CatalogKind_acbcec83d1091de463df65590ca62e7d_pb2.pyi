from harpia_generated.protofiles import AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2 as _AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import CatalogGroup_acbcec83d1091de463df65590ca62e7d_pb2 as _CatalogGroup_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogKind(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "groups", "kind"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_acbcec83d1091de463df65590ca62e7d_pb2.CatalogGroup]
    kind: _AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2.AnnotationKind
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., kind: _Optional[_Union[_AnnotationKind_acbcec83d1091de463df65590ca62e7d_pb2.AnnotationKind, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_acbcec83d1091de463df65590ca62e7d_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
