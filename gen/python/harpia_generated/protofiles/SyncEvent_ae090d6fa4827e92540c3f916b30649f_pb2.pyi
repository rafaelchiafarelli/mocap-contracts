from harpia_generated.protofiles import SyncKind_ae090d6fa4827e92540c3f916b30649f_pb2 as _SyncKind_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import SyncSource_ae090d6fa4827e92540c3f916b30649f_pb2 as _SyncSource_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncEvent(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "host_ts_ns", "kind", "source"]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    HOST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    host_ts_ns: int
    kind: _SyncKind_ae090d6fa4827e92540c3f916b30649f_pb2.SyncKind
    source: _SyncSource_ae090d6fa4827e92540c3f916b30649f_pb2.SyncSource
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., kind: _Optional[_Union[_SyncKind_ae090d6fa4827e92540c3f916b30649f_pb2.SyncKind, str]] = ..., host_ts_ns: _Optional[int] = ..., source: _Optional[_Union[_SyncSource_ae090d6fa4827e92540c3f916b30649f_pb2.SyncSource, str]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
