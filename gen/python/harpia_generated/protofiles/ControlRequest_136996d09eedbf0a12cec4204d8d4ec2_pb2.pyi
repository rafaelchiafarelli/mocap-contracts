from harpia_generated.protofiles import StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlSetting_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlSetting_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlSetting]
    stream: _StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2.StreamSettings
    want_device_info: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ...) -> None: ...
