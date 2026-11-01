from harpia_generated.protofiles import TakeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TakeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import CalibrationBoard_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CalibrationBoard_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import TakeCamera_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TakeCamera_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Casting]
    end: _SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent
    type: _TakeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TakeType
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TakeCamera, _Mapping]]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
