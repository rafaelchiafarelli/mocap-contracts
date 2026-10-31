from harpia_generated.protofiles import TakeType_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _TakeType_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import SyncEvent_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _SyncEvent_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import CalibrationBoard_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _CalibrationBoard_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import TakeCamera_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _TakeCamera_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_e51d6d03132b4baa0ced72cde01af9d0_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_e51d6d03132b4baa0ced72cde01af9d0_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2.Casting]
    end: _SyncEvent_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncEvent
    type: _TakeType_e51d6d03132b4baa0ced72cde01af9d0_pb2.TakeType
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_e51d6d03132b4baa0ced72cde01af9d0_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_e51d6d03132b4baa0ced72cde01af9d0_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_e51d6d03132b4baa0ced72cde01af9d0_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_e51d6d03132b4baa0ced72cde01af9d0_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_e51d6d03132b4baa0ced72cde01af9d0_pb2.TakeCamera, _Mapping]]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
