from harpia_generated.protofiles import TakeType_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _TakeType_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import CalibrationBoard_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _CalibrationBoard_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import TakeCamera_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _TakeCamera_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_61c8c10158ef4d464aeae2ffe73974e6_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_61c8c10158ef4d464aeae2ffe73974e6_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2.Casting]
    end: _SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent
    type: _TakeType_61c8c10158ef4d464aeae2ffe73974e6_pb2.TakeType
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_61c8c10158ef4d464aeae2ffe73974e6_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_61c8c10158ef4d464aeae2ffe73974e6_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_61c8c10158ef4d464aeae2ffe73974e6_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_61c8c10158ef4d464aeae2ffe73974e6_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_61c8c10158ef4d464aeae2ffe73974e6_pb2.TakeCamera, _Mapping]]] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
