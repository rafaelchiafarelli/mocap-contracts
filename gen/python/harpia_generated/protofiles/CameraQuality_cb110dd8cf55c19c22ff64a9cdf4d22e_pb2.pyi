from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraQuality(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "detection_rate_body", "detection_rate_left_hand", "detection_rate_right_hand", "jitter_px", "reproj_err_px", "role"]
    DETECTION_RATE_BODY_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RATE_LEFT_HAND_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RATE_RIGHT_HAND_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    JITTER_PX_FIELD_NUMBER: _ClassVar[int]
    REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    detection_rate_body: float
    detection_rate_left_hand: float
    detection_rate_right_hand: float
    jitter_px: float
    reproj_err_px: float
    role: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., role: _Optional[str] = ..., detection_rate_body: _Optional[float] = ..., detection_rate_left_hand: _Optional[float] = ..., detection_rate_right_hand: _Optional[float] = ..., jitter_px: _Optional[float] = ..., reproj_err_px: _Optional[float] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
