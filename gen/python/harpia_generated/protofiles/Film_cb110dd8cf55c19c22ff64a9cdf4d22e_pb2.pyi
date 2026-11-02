from harpia_generated.protofiles import FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "format_version", "origin", "parts", "spaces"]
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    format_version: int
    origin: _FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.IdSpace]
    def __init__(self, HARPIA_ID: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.IdSpace, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
