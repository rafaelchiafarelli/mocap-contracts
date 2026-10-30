from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraQuality(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "detection_rate_body", "detection_rate_left_hand", "detection_rate_right_hand", "jitter_px", "reproj_err_px", "role"]
    DETECTION_RATE_BODY_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RATE_LEFT_HAND_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RATE_RIGHT_HAND_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    JITTER_PX_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    detection_rate_body: float
    detection_rate_left_hand: float
    detection_rate_right_hand: float
    jitter_px: float
    reproj_err_px: float
    role: str
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., role: _Optional[str] = ..., detection_rate_body: _Optional[float] = ..., detection_rate_left_hand: _Optional[float] = ..., detection_rate_right_hand: _Optional[float] = ..., jitter_px: _Optional[float] = ..., reproj_err_px: _Optional[float] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
