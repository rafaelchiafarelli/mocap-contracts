from harpia_generated.protofiles import FilmOrigin_3bddfc80b8962961520359f03ba8cf1e_pb2 as _FilmOrigin_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import FilmPart_3bddfc80b8962961520359f03ba8cf1e_pb2 as _FilmPart_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import IdSpace_3bddfc80b8962961520359f03ba8cf1e_pb2 as _IdSpace_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "format_version", "origin", "parts", "spaces"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    format_version: int
    origin: _FilmOrigin_3bddfc80b8962961520359f03ba8cf1e_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_3bddfc80b8962961520359f03ba8cf1e_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_3bddfc80b8962961520359f03ba8cf1e_pb2.IdSpace]
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_3bddfc80b8962961520359f03ba8cf1e_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_3bddfc80b8962961520359f03ba8cf1e_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_3bddfc80b8962961520359f03ba8cf1e_pb2.IdSpace, _Mapping]]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
