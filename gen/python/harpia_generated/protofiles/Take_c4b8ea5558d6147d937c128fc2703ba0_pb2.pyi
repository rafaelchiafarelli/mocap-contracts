from harpia_generated.protofiles import TakeType_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _TakeType_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import CalibrationBoard_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CalibrationBoard_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import TakeCamera_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _TakeCamera_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_c4b8ea5558d6147d937c128fc2703ba0_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_c4b8ea5558d6147d937c128fc2703ba0_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2.Casting]
    end: _SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent
    type: _TakeType_c4b8ea5558d6147d937c128fc2703ba0_pb2.TakeType
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_c4b8ea5558d6147d937c128fc2703ba0_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_c4b8ea5558d6147d937c128fc2703ba0_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_c4b8ea5558d6147d937c128fc2703ba0_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_c4b8ea5558d6147d937c128fc2703ba0_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_c4b8ea5558d6147d937c128fc2703ba0_pb2.TakeCamera, _Mapping]]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
