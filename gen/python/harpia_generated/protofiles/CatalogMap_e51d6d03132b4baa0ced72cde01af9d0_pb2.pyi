from harpia_generated.protofiles import BibleMap_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _BibleMap_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import CatalogGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _CatalogGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogMap(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "bible_map", "groups"]
    BIBLE_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    bible_map: _BibleMap_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleMap
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2.CatalogGroup]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., bible_map: _Optional[_Union[_BibleMap_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleMap, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
