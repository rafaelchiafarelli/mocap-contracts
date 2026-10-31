from harpia_generated.protofiles import BibleValue_186a1974c92f444f1bbc853569958a27_pb2 as _BibleValue_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import BibleLink_186a1974c92f444f1bbc853569958a27_pb2 as _BibleLink_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleItem(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "aliases", "id", "links", "name", "parent", "values"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    VALUES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    id: str
    links: _containers.RepeatedCompositeFieldContainer[_BibleLink_186a1974c92f444f1bbc853569958a27_pb2.BibleLink]
    name: str
    parent: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_186a1974c92f444f1bbc853569958a27_pb2.BibleValue]
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., parent: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_BibleValue_186a1974c92f444f1bbc853569958a27_pb2.BibleValue, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[_BibleLink_186a1974c92f444f1bbc853569958a27_pb2.BibleLink, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
