from harpia_generated.protofiles import TakeType_acbcec83d1091de463df65590ca62e7d_pb2 as _TakeType_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2 as _SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import Casting_acbcec83d1091de463df65590ca62e7d_pb2 as _Casting_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import CalibrationBoard_acbcec83d1091de463df65590ca62e7d_pb2 as _CalibrationBoard_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import TakeCamera_acbcec83d1091de463df65590ca62e7d_pb2 as _TakeCamera_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_acbcec83d1091de463df65590ca62e7d_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_acbcec83d1091de463df65590ca62e7d_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_acbcec83d1091de463df65590ca62e7d_pb2.Casting]
    end: _SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent
    type: _TakeType_acbcec83d1091de463df65590ca62e7d_pb2.TakeType
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_acbcec83d1091de463df65590ca62e7d_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_acbcec83d1091de463df65590ca62e7d_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_acbcec83d1091de463df65590ca62e7d_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_acbcec83d1091de463df65590ca62e7d_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_acbcec83d1091de463df65590ca62e7d_pb2.TakeCamera, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
