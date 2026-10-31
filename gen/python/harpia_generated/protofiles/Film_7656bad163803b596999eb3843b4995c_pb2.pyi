from harpia_generated.protofiles import FilmOrigin_7656bad163803b596999eb3843b4995c_pb2 as _FilmOrigin_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import FilmPart_7656bad163803b596999eb3843b4995c_pb2 as _FilmPart_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import IdSpace_7656bad163803b596999eb3843b4995c_pb2 as _IdSpace_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "format_version", "origin", "parts", "spaces"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    format_version: int
    origin: _FilmOrigin_7656bad163803b596999eb3843b4995c_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_7656bad163803b596999eb3843b4995c_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_7656bad163803b596999eb3843b4995c_pb2.IdSpace]
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_7656bad163803b596999eb3843b4995c_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_7656bad163803b596999eb3843b4995c_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_7656bad163803b596999eb3843b4995c_pb2.IdSpace, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
