from harpia_generated.protofiles import FrameGap_acbcec83d1091de463df65590ca62e7d_pb2 as _FrameGap_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraTakeReport(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "first_ts_ns", "fps_cv", "fps_measured", "frames", "gaps", "last_ts_ns", "role"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FPS_CV_FIELD_NUMBER: _ClassVar[int]
    FPS_MEASURED_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    GAPS_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    first_ts_ns: int
    fps_cv: float
    fps_measured: float
    frames: int
    gaps: _containers.RepeatedCompositeFieldContainer[_FrameGap_acbcec83d1091de463df65590ca62e7d_pb2.FrameGap]
    last_ts_ns: int
    role: str
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., role: _Optional[str] = ..., frames: _Optional[int] = ..., fps_measured: _Optional[float] = ..., fps_cv: _Optional[float] = ..., gaps: _Optional[_Iterable[_Union[_FrameGap_acbcec83d1091de463df65590ca62e7d_pb2.FrameGap, _Mapping]]] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
