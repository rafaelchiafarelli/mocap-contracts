from harpia_generated.protofiles import BibleMap_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _BibleMap_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import CatalogGroup_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CatalogGroup_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogMap(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "bible_map", "groups"]
    BIBLE_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    bible_map: _BibleMap_136996d09eedbf0a12cec4204d8d4ec2_pb2.BibleMap
    groups: _containers.RepeatedCompositeFieldContainer[_CatalogGroup_136996d09eedbf0a12cec4204d8d4ec2_pb2.CatalogGroup]
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., bible_map: _Optional[_Union[_BibleMap_136996d09eedbf0a12cec4204d8d4ec2_pb2.BibleMap, str]] = ..., groups: _Optional[_Iterable[_Union[_CatalogGroup_136996d09eedbf0a12cec4204d8d4ec2_pb2.CatalogGroup, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
