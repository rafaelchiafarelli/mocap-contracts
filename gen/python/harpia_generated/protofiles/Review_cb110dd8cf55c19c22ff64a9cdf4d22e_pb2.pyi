from harpia_generated.protofiles import ReviewOutcome_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ReviewOutcome_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Review(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "by", "note", "outcome", "proposal", "text", "time"]
    BY_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    by: str
    note: str
    outcome: _ReviewOutcome_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ReviewOutcome
    proposal: str
    text: str
    time: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., proposal: _Optional[str] = ..., outcome: _Optional[_Union[_ReviewOutcome_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ReviewOutcome, str]] = ..., by: _Optional[str] = ..., time: _Optional[str] = ..., note: _Optional[str] = ..., text: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
