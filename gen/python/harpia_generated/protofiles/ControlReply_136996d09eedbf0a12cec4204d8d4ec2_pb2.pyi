from harpia_generated.protofiles import StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import DeviceInfo_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _DeviceInfo_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_136996d09eedbf0a12cec4204d8d4ec2_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2.StreamSettings
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_136996d09eedbf0a12cec4204d8d4ec2_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_136996d09eedbf0a12cec4204d8d4ec2_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ...) -> None: ...
