from harpia_generated.protofiles import BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import BibleLink_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BibleLink_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleItem(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "aliases", "id", "links", "name", "parent", "values"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    id: str
    links: _containers.RepeatedCompositeFieldContainer[_BibleLink_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleLink]
    name: str
    parent: str
    values: _containers.RepeatedCompositeFieldContainer[_BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleValue]
    def __init__(self, HARPIA_ID: _Optional[int] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., parent: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleValue, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[_BibleLink_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleLink, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
