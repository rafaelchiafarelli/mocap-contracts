from harpia_generated.protofiles import BibleMap_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _BibleMap_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import CatalogGroup_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _CatalogGroup_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogMap(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "bible_map", "groups"]
    BIBLE_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    bible_map: _BibleMap_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.BibleMap
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.CatalogGroup]
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., bible_map: _Optional[_Union[_BibleMap_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.BibleMap, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
