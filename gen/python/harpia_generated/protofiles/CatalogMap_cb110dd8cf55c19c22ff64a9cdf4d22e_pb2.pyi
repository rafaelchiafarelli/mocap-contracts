from harpia_generated.protofiles import BibleMap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BibleMap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogMap(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "bible_map", "groups"]
    BIBLE_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    bible_map: _BibleMap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleMap
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CatalogGroup]
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., bible_map: _Optional[_Union[_BibleMap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleMap, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
