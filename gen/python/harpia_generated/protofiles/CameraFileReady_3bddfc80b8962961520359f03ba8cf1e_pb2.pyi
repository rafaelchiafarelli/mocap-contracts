from harpia_generated.protofiles import FileKind_3bddfc80b8962961520359f03ba8cf1e_pb2 as _FileKind_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraFileReady(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "first_ts_ns", "frames", "kind", "last_ts_ns", "path", "role", "sha256", "size_bytes", "take_id"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: str
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    first_ts_ns: int
    frames: int
    kind: _FileKind_3bddfc80b8962961520359f03ba8cf1e_pb2.FileKind
    last_ts_ns: int
    path: str
    role: str
    sha256: str
    size_bytes: int
    take_id: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., take_id: _Optional[str] = ..., role: _Optional[str] = ..., kind: _Optional[_Union[_FileKind_3bddfc80b8962961520359f03ba8cf1e_pb2.FileKind, str]] = ..., path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ..., frames: _Optional[int] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ...) -> None: ...
