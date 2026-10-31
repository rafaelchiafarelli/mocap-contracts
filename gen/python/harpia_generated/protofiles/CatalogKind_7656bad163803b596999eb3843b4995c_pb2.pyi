from harpia_generated.protofiles import AnnotationKind_7656bad163803b596999eb3843b4995c_pb2 as _AnnotationKind_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import CatalogGroup_7656bad163803b596999eb3843b4995c_pb2 as _CatalogGroup_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogKind(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "groups", "kind"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_7656bad163803b596999eb3843b4995c_pb2.CatalogGroup]
    kind: _AnnotationKind_7656bad163803b596999eb3843b4995c_pb2.AnnotationKind
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., kind: _Optional[_Union[_AnnotationKind_7656bad163803b596999eb3843b4995c_pb2.AnnotationKind, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_7656bad163803b596999eb3843b4995c_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
