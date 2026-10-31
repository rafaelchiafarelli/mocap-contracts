from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalibrationBoard(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "aruco_dictionary", "marker_length_mm", "measured_square_length_mm", "square_length_mm", "squares_x", "squares_y"]
    ARUCO_DICTIONARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    MARKER_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SQUARES_X_FIELD_NUMBER: _ClassVar[int]
    SQUARES_Y_FIELD_NUMBER: _ClassVar[int]
    SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    aruco_dictionary: str
    marker_length_mm: float
    measured_square_length_mm: float
    square_length_mm: float
    squares_x: int
    squares_y: int
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., squares_x: _Optional[int] = ..., squares_y: _Optional[int] = ..., square_length_mm: _Optional[float] = ..., marker_length_mm: _Optional[float] = ..., aruco_dictionary: _Optional[str] = ..., measured_square_length_mm: _Optional[float] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
