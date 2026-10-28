from harpia_generated.protofiles import TakeType_3bddfc80b8962961520359f03ba8cf1e_pb2 as _TakeType_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2 as _SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import Casting_3bddfc80b8962961520359f03ba8cf1e_pb2 as _Casting_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import CalibrationBoard_3bddfc80b8962961520359f03ba8cf1e_pb2 as _CalibrationBoard_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import TakeCamera_3bddfc80b8962961520359f03ba8cf1e_pb2 as _TakeCamera_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Take(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "board", "cameras", "casting", "end", "id", "session_id", "start", "type"]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    CASTING_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    board: _CalibrationBoard_3bddfc80b8962961520359f03ba8cf1e_pb2.CalibrationBoard
    cameras: _containers.RepeatedCompositeFieldContainer[_TakeCamera_3bddfc80b8962961520359f03ba8cf1e_pb2.TakeCamera]
    casting: _containers.RepeatedCompositeFieldContainer[_Casting_3bddfc80b8962961520359f03ba8cf1e_pb2.Casting]
    end: _SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent
    id: str
    session_id: str
    start: _SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent
    type: _TakeType_3bddfc80b8962961520359f03ba8cf1e_pb2.TakeType
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_TakeType_3bddfc80b8962961520359f03ba8cf1e_pb2.TakeType, str]] = ..., start: _Optional[_Union[_SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent, _Mapping]] = ..., end: _Optional[_Union[_SyncEvent_3bddfc80b8962961520359f03ba8cf1e_pb2.SyncEvent, _Mapping]] = ..., casting: _Optional[_Iterable[_Union[_Casting_3bddfc80b8962961520359f03ba8cf1e_pb2.Casting, _Mapping]]] = ..., board: _Optional[_Union[_CalibrationBoard_3bddfc80b8962961520359f03ba8cf1e_pb2.CalibrationBoard, _Mapping]] = ..., cameras: _Optional[_Iterable[_Union[_TakeCamera_3bddfc80b8962961520359f03ba8cf1e_pb2.TakeCamera, _Mapping]]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
