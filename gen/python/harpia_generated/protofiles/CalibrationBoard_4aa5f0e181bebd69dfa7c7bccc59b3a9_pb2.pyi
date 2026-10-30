from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalibrationBoard(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "aruco_dictionary", "marker_length_mm", "measured_square_length_mm", "square_length_mm", "squares_x", "squares_y"]
    ARUCO_DICTIONARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    MARKER_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SQUARES_X_FIELD_NUMBER: _ClassVar[int]
    SQUARES_Y_FIELD_NUMBER: _ClassVar[int]
    SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    aruco_dictionary: str
    marker_length_mm: float
    measured_square_length_mm: float
    square_length_mm: float
    squares_x: int
    squares_y: int
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., squares_x: _Optional[int] = ..., squares_y: _Optional[int] = ..., square_length_mm: _Optional[float] = ..., marker_length_mm: _Optional[float] = ..., aruco_dictionary: _Optional[str] = ..., measured_square_length_mm: _Optional[float] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
