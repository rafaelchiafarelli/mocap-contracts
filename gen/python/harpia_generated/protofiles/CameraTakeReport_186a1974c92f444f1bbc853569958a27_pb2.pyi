from harpia_generated.protofiles import FrameGap_186a1974c92f444f1bbc853569958a27_pb2 as _FrameGap_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraTakeReport(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "first_ts_ns", "fps_cv", "fps_measured", "frames", "gaps", "last_ts_ns", "role"]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FPS_CV_FIELD_NUMBER: _ClassVar[int]
    FPS_MEASURED_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    GAPS_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    first_ts_ns: int
    fps_cv: float
    fps_measured: float
    frames: int
    gaps: _containers.RepeatedCompositeFieldContainer[_FrameGap_186a1974c92f444f1bbc853569958a27_pb2.FrameGap]
    last_ts_ns: int
    role: str
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., role: _Optional[str] = ..., frames: _Optional[int] = ..., fps_measured: _Optional[float] = ..., fps_cv: _Optional[float] = ..., gaps: _Optional[_Iterable[_Union[_FrameGap_186a1974c92f444f1bbc853569958a27_pb2.FrameGap, _Mapping]]] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
