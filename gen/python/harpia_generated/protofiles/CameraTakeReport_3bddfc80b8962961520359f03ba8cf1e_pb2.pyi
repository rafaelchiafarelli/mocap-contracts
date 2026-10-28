from harpia_generated.protofiles import FrameGap_3bddfc80b8962961520359f03ba8cf1e_pb2 as _FrameGap_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraTakeReport(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "first_ts_ns", "fps_cv", "fps_measured", "frames", "gaps", "last_ts_ns", "role"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    FIRST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    FPS_CV_FIELD_NUMBER: _ClassVar[int]
    FPS_MEASURED_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    GAPS_FIELD_NUMBER: _ClassVar[int]
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    LAST_TS_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    first_ts_ns: int
    fps_cv: float
    fps_measured: float
    frames: int
    gaps: _containers.RepeatedCompositeFieldContainer[_FrameGap_3bddfc80b8962961520359f03ba8cf1e_pb2.FrameGap]
    last_ts_ns: int
    role: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., role: _Optional[str] = ..., frames: _Optional[int] = ..., fps_measured: _Optional[float] = ..., fps_cv: _Optional[float] = ..., gaps: _Optional[_Iterable[_Union[_FrameGap_3bddfc80b8962961520359f03ba8cf1e_pb2.FrameGap, _Mapping]]] = ..., first_ts_ns: _Optional[int] = ..., last_ts_ns: _Optional[int] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
