from harpia_generated.protofiles import ChangeOp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ChangeOp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Change(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "after", "before", "by", "op", "path", "record", "time"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    after: str
    before: str
    by: str
    op: _ChangeOp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ChangeOp
    path: str
    record: str
    time: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., time: _Optional[str] = ..., by: _Optional[str] = ..., path: _Optional[str] = ..., record: _Optional[str] = ..., op: _Optional[_Union[_ChangeOp_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ChangeOp, str]] = ..., before: _Optional[str] = ..., after: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
