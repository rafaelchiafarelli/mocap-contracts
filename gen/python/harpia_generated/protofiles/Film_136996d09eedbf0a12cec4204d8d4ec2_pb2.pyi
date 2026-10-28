from harpia_generated.protofiles import FilmOrigin_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _FilmOrigin_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import FilmPart_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _FilmPart_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import IdSpace_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _IdSpace_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Film(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "format_version", "origin", "parts", "spaces"]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    format_version: int
    origin: _FilmOrigin_136996d09eedbf0a12cec4204d8d4ec2_pb2.FilmOrigin
    parts: _containers.RepeatedCompositeFieldContainer[_FilmPart_136996d09eedbf0a12cec4204d8d4ec2_pb2.FilmPart]
    spaces: _containers.RepeatedCompositeFieldContainer[_IdSpace_136996d09eedbf0a12cec4204d8d4ec2_pb2.IdSpace]
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., format_version: _Optional[int] = ..., origin: _Optional[_Union[_FilmOrigin_136996d09eedbf0a12cec4204d8d4ec2_pb2.FilmOrigin, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[_FilmPart_136996d09eedbf0a12cec4204d8d4ec2_pb2.FilmPart, _Mapping]]] = ..., spaces: _Optional[_Iterable[_Union[_IdSpace_136996d09eedbf0a12cec4204d8d4ec2_pb2.IdSpace, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
