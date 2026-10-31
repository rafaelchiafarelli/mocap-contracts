from harpia_generated.protofiles import FilmOrigin_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _FilmOrigin_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import FilmPart_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _FilmPart_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import IdSpace_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _IdSpace_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "format_version", "origin", "parts", "spaces"]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    format_version: int
    origin: _FilmOrigin_e51d6d03132b4baa0ced72cde01af9d0_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_e51d6d03132b4baa0ced72cde01af9d0_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_e51d6d03132b4baa0ced72cde01af9d0_pb2.IdSpace]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_e51d6d03132b4baa0ced72cde01af9d0_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_e51d6d03132b4baa0ced72cde01af9d0_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_e51d6d03132b4baa0ced72cde01af9d0_pb2.IdSpace, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
