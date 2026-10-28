from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CameraStats(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "battery_temp_c", "camera_fps", "cpu_percent", "dropped_frames", "encoder_fps", "sensor_ns", "serial", "thermal_status"]
    BATTERY_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FPS_FIELD_NUMBER: _ClassVar[int]
    CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DROPPED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    ENCODER_FPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: str
    SENSOR_NS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    THERMAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    battery_temp_c: float
    camera_fps: float
    cpu_percent: float
    dropped_frames: int
    encoder_fps: float
    sensor_ns: int
    serial: str
    thermal_status: int
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., serial: _Optional[str] = ..., sensor_ns: _Optional[int] = ..., camera_fps: _Optional[float] = ..., encoder_fps: _Optional[float] = ..., dropped_frames: _Optional[int] = ..., cpu_percent: _Optional[float] = ..., battery_temp_c: _Optional[float] = ..., thermal_status: _Optional[int] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ...) -> None: ...
