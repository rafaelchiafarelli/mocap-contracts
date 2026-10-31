from harpia_generated.protofiles import StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import DeviceInfo_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _DeviceInfo_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_e51d6d03132b4baa0ced72cde01af9d0_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.StreamSettings
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_e51d6d03132b4baa0ced72cde01af9d0_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ...) -> None: ...
