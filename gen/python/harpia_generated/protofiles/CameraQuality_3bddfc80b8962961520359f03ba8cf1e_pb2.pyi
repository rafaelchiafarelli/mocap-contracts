from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraQuality(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "detection_rate_body", "detection_rate_left_hand", "detection_rate_right_hand", "jitter_px", "reproj_err_px", "role"]
    DETECTION_RATE_BODY_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RATE_LEFT_HAND_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RATE_RIGHT_HAND_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    JITTER_PX_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    detection_rate_body: float
    detection_rate_left_hand: float
    detection_rate_right_hand: float
    jitter_px: float
    reproj_err_px: float
    role: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., role: _Optional[str] = ..., detection_rate_body: _Optional[float] = ..., detection_rate_left_hand: _Optional[float] = ..., detection_rate_right_hand: _Optional[float] = ..., jitter_px: _Optional[float] = ..., reproj_err_px: _Optional[float] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
