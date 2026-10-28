from harpia_generated.protofiles import CatalogMap_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CatalogMap_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleCatalog(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "maps", "version"]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    MAPS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    VERSION_FIELD_NUMBER: _ClassVar[int]
    maps: _containers.RepeatedCompositeFieldContainer[_CatalogMap_136996d09eedbf0a12cec4204d8d4ec2_pb2.CatalogMap]
    version: int
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., version: _Optional[int] = ..., maps: _Optional[_Iterable[_Union[_CatalogMap_136996d09eedbf0a12cec4204d8d4ec2_pb2.CatalogMap, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
