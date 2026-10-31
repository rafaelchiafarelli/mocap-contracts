from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraControls(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "auto_exposure", "auto_focus", "auto_white_balance", "exposure_ns", "focus_diopters", "focus_raw", "gain_raw", "iso", "power_line_hz", "white_balance_k"]
    AUTO_EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    AUTO_FOCUS_FIELD_NUMBER: _ClassVar[int]
    AUTO_WHITE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    EXPOSURE_NS_FIELD_NUMBER: _ClassVar[int]
    FOCUS_DIOPTERS_FIELD_NUMBER: _ClassVar[int]
    FOCUS_RAW_FIELD_NUMBER: _ClassVar[int]
    GAIN_RAW_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ISO_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    POWER_LINE_HZ_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    WHITE_BALANCE_K_FIELD_NUMBER: _ClassVar[int]
    auto_exposure: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    auto_focus: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    auto_white_balance: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    exposure_ns: int
    focus_diopters: float
    focus_raw: float
    gain_raw: float
    iso: int
    power_line_hz: int
    white_balance_k: int
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., exposure_ns: _Optional[int] = ..., iso: _Optional[int] = ..., gain_raw: _Optional[float] = ..., focus_diopters: _Optional[float] = ..., focus_raw: _Optional[float] = ..., white_balance_k: _Optional[int] = ..., power_line_hz: _Optional[int] = ..., auto_exposure: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., auto_focus: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., auto_white_balance: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
