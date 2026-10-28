from harpia_generated.protofiles import FilmOrigin_ae090d6fa4827e92540c3f916b30649f_pb2 as _FilmOrigin_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import FilmPart_ae090d6fa4827e92540c3f916b30649f_pb2 as _FilmPart_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import IdSpace_ae090d6fa4827e92540c3f916b30649f_pb2 as _IdSpace_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "format_version", "origin", "parts", "spaces"]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    format_version: int
    origin: _FilmOrigin_ae090d6fa4827e92540c3f916b30649f_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_ae090d6fa4827e92540c3f916b30649f_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_ae090d6fa4827e92540c3f916b30649f_pb2.IdSpace]
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_ae090d6fa4827e92540c3f916b30649f_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_ae090d6fa4827e92540c3f916b30649f_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_ae090d6fa4827e92540c3f916b30649f_pb2.IdSpace, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
