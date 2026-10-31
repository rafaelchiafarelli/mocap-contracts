from harpia_generated.protofiles import FileKind_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _FileKind_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraFileReady(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "first_ts_ns", "frames", "kind", "last_ts_ns", "path", "role", "sha256", "size_bytes", "take_id"]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0: str
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    first_ts_ns: int
    frames: int
    kind: _FileKind_e51d6d03132b4baa0ced72cde01af9d0_pb2.FileKind
    last_ts_ns: int
    path: str
    role: str
    sha256: str
    size_bytes: int
    take_id: str
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., take_id: _Optional[str] = ..., role: _Optional[str] = ..., kind: _Optional[_Union[_FileKind_e51d6d03132b4baa0ced72cde01af9d0_pb2.FileKind, str]] = ..., path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ..., frames: _Optional[int] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ...) -> None: ...
