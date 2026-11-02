from harpia_generated.protofiles import FileKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FileKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraFileReady(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "first_ts_ns", "frames", "kind", "last_ts_ns", "path", "role", "sha256", "size_bytes", "take_id"]
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    first_ts_ns: int
    frames: int
    kind: _FileKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FileKind
    last_ts_ns: int
    path: str
    role: str
    sha256: str
    size_bytes: int
    take_id: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., take_id: _Optional[str] = ..., role: _Optional[str] = ..., kind: _Optional[_Union[_FileKind_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FileKind, str]] = ..., path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ..., frames: _Optional[int] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
