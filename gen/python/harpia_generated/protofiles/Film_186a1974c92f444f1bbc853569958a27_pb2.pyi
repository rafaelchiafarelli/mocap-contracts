from harpia_generated.protofiles import FilmOrigin_186a1974c92f444f1bbc853569958a27_pb2 as _FilmOrigin_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import FilmPart_186a1974c92f444f1bbc853569958a27_pb2 as _FilmPart_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import IdSpace_186a1974c92f444f1bbc853569958a27_pb2 as _IdSpace_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "format_version", "origin", "parts", "spaces"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    format_version: int
    origin: _FilmOrigin_186a1974c92f444f1bbc853569958a27_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_186a1974c92f444f1bbc853569958a27_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_186a1974c92f444f1bbc853569958a27_pb2.IdSpace]
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_186a1974c92f444f1bbc853569958a27_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_186a1974c92f444f1bbc853569958a27_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_186a1974c92f444f1bbc853569958a27_pb2.IdSpace, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
