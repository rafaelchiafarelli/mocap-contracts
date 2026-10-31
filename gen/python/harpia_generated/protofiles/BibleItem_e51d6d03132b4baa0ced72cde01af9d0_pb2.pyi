from harpia_generated.protofiles import BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import BibleLink_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _BibleLink_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleItem(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "aliases", "id", "links", "name", "parent", "values"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    VALUES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    id: str
    links: _containers.RepeatedCompositeFieldContainer[_BibleLink_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleLink]
    name: str
    parent: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleValue]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., parent: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_BibleValue_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleValue, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[_BibleLink_e51d6d03132b4baa0ced72cde01af9d0_pb2.BibleLink, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
