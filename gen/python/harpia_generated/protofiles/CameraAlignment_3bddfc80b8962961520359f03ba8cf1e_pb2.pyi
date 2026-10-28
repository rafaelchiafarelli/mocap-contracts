from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraAlignment(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "drift_ppm", "frames_in", "frames_out", "offset_ns", "role"]
    DRIFT_PPM_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    FRAMES_IN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_OUT_FIELD_NUMBER: _ClassVar[int]
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    OFFSET_NS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    drift_ppm: float
    frames_in: int
    frames_out: int
    offset_ns: int
    role: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., role: _Optional[str] = ..., offset_ns: _Optional[int] = ..., drift_ppm: _Optional[float] = ..., frames_in: _Optional[int] = ..., frames_out: _Optional[int] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
