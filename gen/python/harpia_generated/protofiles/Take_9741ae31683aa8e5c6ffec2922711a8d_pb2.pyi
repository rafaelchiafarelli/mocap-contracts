from harpia_generated.protofiles import TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import CalibrationBoard_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _CalibrationBoard_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import TakeCamera_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _TakeCamera_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_9741ae31683aa8e5c6ffec2922711a8d_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_9741ae31683aa8e5c6ffec2922711a8d_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2.Casting]
    end: _SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncEvent
    type: _TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2.TakeType
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_9741ae31683aa8e5c6ffec2922711a8d_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_9741ae31683aa8e5c6ffec2922711a8d_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_9741ae31683aa8e5c6ffec2922711a8d_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_9741ae31683aa8e5c6ffec2922711a8d_pb2.TakeCamera, _Mapping]]] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
