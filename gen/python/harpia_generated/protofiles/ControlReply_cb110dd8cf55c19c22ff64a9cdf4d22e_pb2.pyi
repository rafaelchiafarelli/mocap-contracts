from harpia_generated.protofiles import StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import DeviceInfo_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _DeviceInfo_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.StreamSettings
    def __init__(self, HARPIA_ID: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
