from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraAlignment(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "drift_ppm", "frames_in", "frames_out", "offset_ns", "role"]
    DRIFT_PPM_FIELD_NUMBER: _ClassVar[int]
    FRAMES_IN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_OUT_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_NS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    drift_ppm: float
    frames_in: int
    frames_out: int
    offset_ns: int
    role: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., role: _Optional[str] = ..., offset_ns: _Optional[int] = ..., drift_ppm: _Optional[float] = ..., frames_in: _Optional[int] = ..., frames_out: _Optional[int] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
