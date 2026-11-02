from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraAblation(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "mean_rsd_change", "mean_shift_m", "removed_role"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    MEAN_RSD_CHANGE_FIELD_NUMBER: _ClassVar[int]
    MEAN_SHIFT_M_FIELD_NUMBER: _ClassVar[int]
    REMOVED_ROLE_FIELD_NUMBER: _ClassVar[int]
    mean_rsd_change: float
    mean_shift_m: float
    removed_role: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., removed_role: _Optional[str] = ..., mean_shift_m: _Optional[float] = ..., mean_rsd_change: _Optional[float] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
