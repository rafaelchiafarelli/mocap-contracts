from harpia_generated.protofiles import BibleValue_7656bad163803b596999eb3843b4995c_pb2 as _BibleValue_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import BibleLink_7656bad163803b596999eb3843b4995c_pb2 as _BibleLink_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleItem(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "aliases", "id", "links", "name", "parent", "values"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    VALUES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    id: str
    links: _containers.RepeatedCompositeFieldContainer[_BibleLink_7656bad163803b596999eb3843b4995c_pb2.BibleLink]
    name: str
    parent: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_7656bad163803b596999eb3843b4995c_pb2.BibleValue]
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., parent: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_BibleValue_7656bad163803b596999eb3843b4995c_pb2.BibleValue, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[_BibleLink_7656bad163803b596999eb3843b4995c_pb2.BibleLink, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
