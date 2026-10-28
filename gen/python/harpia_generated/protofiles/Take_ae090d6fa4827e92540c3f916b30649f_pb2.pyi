from harpia_generated.protofiles import TakeType_ae090d6fa4827e92540c3f916b30649f_pb2 as _TakeType_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2 as _SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import Casting_ae090d6fa4827e92540c3f916b30649f_pb2 as _Casting_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import CalibrationBoard_ae090d6fa4827e92540c3f916b30649f_pb2 as _CalibrationBoard_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import TakeCamera_ae090d6fa4827e92540c3f916b30649f_pb2 as _TakeCamera_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_ae090d6fa4827e92540c3f916b30649f_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_ae090d6fa4827e92540c3f916b30649f_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_ae090d6fa4827e92540c3f916b30649f_pb2.Casting]
    end: _SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent
    type: _TakeType_ae090d6fa4827e92540c3f916b30649f_pb2.TakeType
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_ae090d6fa4827e92540c3f916b30649f_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_ae090d6fa4827e92540c3f916b30649f_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_ae090d6fa4827e92540c3f916b30649f_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_ae090d6fa4827e92540c3f916b30649f_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_ae090d6fa4827e92540c3f916b30649f_pb2.TakeCamera, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
