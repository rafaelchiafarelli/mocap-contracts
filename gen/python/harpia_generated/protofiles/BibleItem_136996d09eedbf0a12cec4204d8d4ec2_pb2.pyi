from harpia_generated.protofiles import BibleValue_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _BibleValue_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import BibleLink_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _BibleLink_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleItem(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "aliases", "id", "links", "name", "parent", "values"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    VALUES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    id: str
    links: _containers.RepeatedCompositeFieldContainer[_BibleLink_136996d09eedbf0a12cec4204d8d4ec2_pb2.BibleLink]
    name: str
    parent: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.BibleValue]
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., parent: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_BibleValue_136996d09eedbf0a12cec4204d8d4ec2_pb2.BibleValue, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[_BibleLink_136996d09eedbf0a12cec4204d8d4ec2_pb2.BibleLink, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
