from harpia_generated.protofiles import ValueState_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ValueState_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleValue(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "by", "department", "field", "note", "number", "revisit", "scene", "source", "state", "text", "unit"]
    BY_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVISIT_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    by: str
    department: str
    field: str
    note: str
    number: str
    revisit: str
    scene: str
    source: str
    state: _ValueState_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ValueState
    text: str
    unit: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., field: _Optional[str] = ..., scene: _Optional[str] = ..., text: _Optional[str] = ..., number: _Optional[str] = ..., unit: _Optional[str] = ..., note: _Optional[str] = ..., state: _Optional[_Union[_ValueState_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ValueState, str]] = ..., source: _Optional[str] = ..., department: _Optional[str] = ..., by: _Optional[str] = ..., revisit: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
