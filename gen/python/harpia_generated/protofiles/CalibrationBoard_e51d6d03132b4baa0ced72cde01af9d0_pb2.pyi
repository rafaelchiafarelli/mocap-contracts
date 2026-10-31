from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalibrationBoard(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "aruco_dictionary", "marker_length_mm", "measured_square_length_mm", "square_length_mm", "squares_x", "squares_y"]
    ARUCO_DICTIONARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    MARKER_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SQUARES_X_FIELD_NUMBER: _ClassVar[int]
    SQUARES_Y_FIELD_NUMBER: _ClassVar[int]
    SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    aruco_dictionary: str
    marker_length_mm: float
    measured_square_length_mm: float
    square_length_mm: float
    squares_x: int
    squares_y: int
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., squares_x: _Optional[int] = ..., squares_y: _Optional[int] = ..., square_length_mm: _Optional[float] = ..., marker_length_mm: _Optional[float] = ..., aruco_dictionary: _Optional[str] = ..., measured_square_length_mm: _Optional[float] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
