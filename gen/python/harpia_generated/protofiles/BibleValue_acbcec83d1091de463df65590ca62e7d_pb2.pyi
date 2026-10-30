from harpia_generated.protofiles import ValueState_acbcec83d1091de463df65590ca62e7d_pb2 as _ValueState_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BibleValue(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "by", "department", "field", "note", "number", "revisit", "scene", "source", "state", "text", "unit"]
    BY_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    FIELD_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REVISIT_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
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
    state: _ValueState_acbcec83d1091de463df65590ca62e7d_pb2.ValueState
    text: str
    unit: str
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., field: _Optional[str] = ..., scene: _Optional[str] = ..., text: _Optional[str] = ..., number: _Optional[str] = ..., unit: _Optional[str] = ..., note: _Optional[str] = ..., state: _Optional[_Union[_ValueState_acbcec83d1091de463df65590ca62e7d_pb2.ValueState, str]] = ..., source: _Optional[str] = ..., department: _Optional[str] = ..., by: _Optional[str] = ..., revisit: _Optional[str] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
