from harpia_generated.protofiles import FrameGap_17f8b54225d6d535e6d691175cc18809_pb2 as _FrameGap_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraTakeReport(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "first_ts_ns", "fps_cv", "fps_measured", "frames", "gaps", "last_ts_ns", "role"]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FPS_CV_FIELD_NUMBER: _ClassVar[int]
    FPS_MEASURED_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    GAPS_FIELD_NUMBER: _ClassVar[int]
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    first_ts_ns: int
    fps_cv: float
    fps_measured: float
    frames: int
    gaps: _containers.RepeatedCompositeFieldContainer[_FrameGap_17f8b54225d6d535e6d691175cc18809_pb2.FrameGap]
    last_ts_ns: int
    role: str
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., role: _Optional[str] = ..., frames: _Optional[int] = ..., fps_measured: _Optional[float] = ..., fps_cv: _Optional[float] = ..., gaps: _Optional[_Iterable[_Union[_FrameGap_17f8b54225d6d535e6d691175cc18809_pb2.FrameGap, _Mapping]]] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
