from harpia_generated.protofiles import FilmOrigin_acbcec83d1091de463df65590ca62e7d_pb2 as _FilmOrigin_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import FilmPart_acbcec83d1091de463df65590ca62e7d_pb2 as _FilmPart_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import IdSpace_acbcec83d1091de463df65590ca62e7d_pb2 as _IdSpace_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "format_version", "origin", "parts", "spaces"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    format_version: int
    origin: _FilmOrigin_acbcec83d1091de463df65590ca62e7d_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_acbcec83d1091de463df65590ca62e7d_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_acbcec83d1091de463df65590ca62e7d_pb2.IdSpace]
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_acbcec83d1091de463df65590ca62e7d_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_acbcec83d1091de463df65590ca62e7d_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_acbcec83d1091de463df65590ca62e7d_pb2.IdSpace, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
