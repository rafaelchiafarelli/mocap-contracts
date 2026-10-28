from harpia_generated.protofiles import BibleMap_ae090d6fa4827e92540c3f916b30649f_pb2 as _BibleMap_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import CatalogGroup_ae090d6fa4827e92540c3f916b30649f_pb2 as _CatalogGroup_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogMap(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "bible_map", "groups"]
    BIBLE_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    bible_map: _BibleMap_ae090d6fa4827e92540c3f916b30649f_pb2.BibleMap
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_ae090d6fa4827e92540c3f916b30649f_pb2.CatalogGroup]
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., bible_map: _Optional[_Union[_BibleMap_ae090d6fa4827e92540c3f916b30649f_pb2.BibleMap, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_ae090d6fa4827e92540c3f916b30649f_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
