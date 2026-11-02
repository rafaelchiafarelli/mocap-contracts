from harpia_generated.protofiles import BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Proposal(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "change_set", "id", "item", "time", "value"]
    CHANGE_SET_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    change_set: str
    id: str
    item: str
    time: str
    value: _BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleValue
    def __init__(self, HARPIA_ID: _Optional[int] = ..., id: _Optional[str] = ..., item: _Optional[str] = ..., value: _Optional[_Union[_BibleValue_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BibleValue, _Mapping]] = ..., time: _Optional[str] = ..., change_set: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
