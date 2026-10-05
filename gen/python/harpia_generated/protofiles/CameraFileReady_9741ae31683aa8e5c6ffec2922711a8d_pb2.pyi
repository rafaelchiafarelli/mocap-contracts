from harpia_generated.protofiles import FileKind_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _FileKind_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraFileReady(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "first_ts_ns", "frames", "kind", "last_ts_ns", "path", "role", "sha256", "size_bytes", "take_id"]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    first_ts_ns: int
    frames: int
    kind: _FileKind_9741ae31683aa8e5c6ffec2922711a8d_pb2.FileKind
    last_ts_ns: int
    path: str
    role: str
    sha256: str
    size_bytes: int
    take_id: str
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., take_id: _Optional[str] = ..., role: _Optional[str] = ..., kind: _Optional[_Union[_FileKind_9741ae31683aa8e5c6ffec2922711a8d_pb2.FileKind, str]] = ..., path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ..., frames: _Optional[int] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
