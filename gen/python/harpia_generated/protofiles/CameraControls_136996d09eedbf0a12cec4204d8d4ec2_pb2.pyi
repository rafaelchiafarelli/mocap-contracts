from harpia_generated.protofiles import Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraControls(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "auto_exposure", "auto_focus", "auto_white_balance", "exposure_ns", "focus_diopters", "focus_raw", "gain_raw", "iso", "power_line_hz", "white_balance_k"]
    AUTO_EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    AUTO_FOCUS_FIELD_NUMBER: _ClassVar[int]
    AUTO_WHITE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    EXPOSURE_NS_FIELD_NUMBER: _ClassVar[int]
    FOCUS_DIOPTERS_FIELD_NUMBER: _ClassVar[int]
    FOCUS_RAW_FIELD_NUMBER: _ClassVar[int]
    GAIN_RAW_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ISO_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    POWER_LINE_HZ_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    WHITE_BALANCE_K_FIELD_NUMBER: _ClassVar[int]
    auto_exposure: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    auto_focus: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    auto_white_balance: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    exposure_ns: int
    focus_diopters: float
    focus_raw: float
    gain_raw: float
    iso: int
    power_line_hz: int
    white_balance_k: int
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., exposure_ns: _Optional[int] = ..., iso: _Optional[int] = ..., gain_raw: _Optional[float] = ..., focus_diopters: _Optional[float] = ..., focus_raw: _Optional[float] = ..., white_balance_k: _Optional[int] = ..., power_line_hz: _Optional[int] = ..., auto_exposure: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., auto_focus: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., auto_white_balance: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
