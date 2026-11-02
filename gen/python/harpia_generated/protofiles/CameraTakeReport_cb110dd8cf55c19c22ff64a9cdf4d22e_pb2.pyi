from harpia_generated.protofiles import FrameGap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _FrameGap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraTakeReport(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "first_ts_ns", "fps_cv", "fps_measured", "frames", "gaps", "last_ts_ns", "role"]
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FPS_CV_FIELD_NUMBER: _ClassVar[int]
    FPS_MEASURED_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    GAPS_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    first_ts_ns: int
    fps_cv: float
    fps_measured: float
    frames: int
    gaps: _containers.RepeatedCompositeFieldContainer[_FrameGap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FrameGap]
    last_ts_ns: int
    role: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., role: _Optional[str] = ..., frames: _Optional[int] = ..., fps_measured: _Optional[float] = ..., fps_cv: _Optional[float] = ..., gaps: _Optional[_Iterable[_Union[_FrameGap_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.FrameGap, _Mapping]]] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
