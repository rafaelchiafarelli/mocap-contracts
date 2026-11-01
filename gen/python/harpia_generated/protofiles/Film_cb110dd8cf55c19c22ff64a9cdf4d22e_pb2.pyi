from harpia_generated.protofiles import FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "format_version", "origin", "parts", "spaces"]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    format_version: int
    origin: _FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.IdSpace]
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.IdSpace, _Mapping]]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
