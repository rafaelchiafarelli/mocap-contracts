from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalibrationBoard(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "aruco_dictionary", "marker_length_mm", "measured_square_length_mm", "square_length_mm", "squares_x", "squares_y"]
    ARUCO_DICTIONARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    MARKER_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SQUARES_X_FIELD_NUMBER: _ClassVar[int]
    SQUARES_Y_FIELD_NUMBER: _ClassVar[int]
    SQUARE_LENGTH_MM_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    aruco_dictionary: str
    marker_length_mm: float
    measured_square_length_mm: float
    square_length_mm: float
    squares_x: int
    squares_y: int
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., squares_x: _Optional[int] = ..., squares_y: _Optional[int] = ..., square_length_mm: _Optional[float] = ..., marker_length_mm: _Optional[float] = ..., aruco_dictionary: _Optional[str] = ..., measured_square_length_mm: _Optional[float] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
