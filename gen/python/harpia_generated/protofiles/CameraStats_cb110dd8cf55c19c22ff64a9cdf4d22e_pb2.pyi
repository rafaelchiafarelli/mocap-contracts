from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraStats(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "battery_temp_c", "camera_fps", "cpu_percent", "dropped_frames", "encoder_fps", "sensor_ns", "serial", "thermal_status"]
    BATTERY_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FPS_FIELD_NUMBER: _ClassVar[int]
    CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DROPPED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    ENCODER_FPS_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    SENSOR_NS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    THERMAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    battery_temp_c: float
    camera_fps: float
    cpu_percent: float
    dropped_frames: int
    encoder_fps: float
    sensor_ns: int
    serial: str
    thermal_status: int
    def __init__(self, HARPIA_ID: _Optional[int] = ..., serial: _Optional[str] = ..., sensor_ns: _Optional[int] = ..., camera_fps: _Optional[float] = ..., encoder_fps: _Optional[float] = ..., dropped_frames: _Optional[int] = ..., cpu_percent: _Optional[float] = ..., battery_temp_c: _Optional[float] = ..., thermal_status: _Optional[int] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
