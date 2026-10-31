from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraStats(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR_186a1974c92f444f1bbc853569958a27", "STATUS_186a1974c92f444f1bbc853569958a27", "battery_temp_c", "camera_fps", "cpu_percent", "dropped_frames", "encoder_fps", "sensor_ns", "serial", "thermal_status"]
    BATTERY_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FPS_FIELD_NUMBER: _ClassVar[int]
    CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DROPPED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    ENCODER_FPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_186a1974c92f444f1bbc853569958a27: str
    SENSOR_NS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    THERMAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    battery_temp_c: float
    camera_fps: float
    cpu_percent: float
    dropped_frames: int
    encoder_fps: float
    sensor_ns: int
    serial: str
    thermal_status: int
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., serial: _Optional[str] = ..., sensor_ns: _Optional[int] = ..., camera_fps: _Optional[float] = ..., encoder_fps: _Optional[float] = ..., dropped_frames: _Optional[int] = ..., cpu_percent: _Optional[float] = ..., battery_temp_c: _Optional[float] = ..., thermal_status: _Optional[int] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ...) -> None: ...
