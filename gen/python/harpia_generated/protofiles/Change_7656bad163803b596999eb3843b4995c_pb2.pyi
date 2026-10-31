from harpia_generated.protofiles import ChangeOp_7656bad163803b596999eb3843b4995c_pb2 as _ChangeOp_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Change(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "after", "before", "by", "op", "path", "record", "time"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    OP_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TIME_FIELD_NUMBER: _ClassVar[int]
    after: str
    before: str
    by: str
    op: _ChangeOp_7656bad163803b596999eb3843b4995c_pb2.ChangeOp
    path: str
    record: str
    time: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., time: _Optional[str] = ..., by: _Optional[str] = ..., path: _Optional[str] = ..., record: _Optional[str] = ..., op: _Optional[_Union[_ChangeOp_7656bad163803b596999eb3843b4995c_pb2.ChangeOp, str]] = ..., before: _Optional[str] = ..., after: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
