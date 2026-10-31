from harpia_generated.protofiles import StreamSettings_7656bad163803b596999eb3843b4995c_pb2 as _StreamSettings_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlResult_7656bad163803b596999eb3843b4995c_pb2 as _ControlResult_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import DeviceInfo_7656bad163803b596999eb3843b4995c_pb2 as _DeviceInfo_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR_7656bad163803b596999eb3843b4995c", "STATUS_7656bad163803b596999eb3843b4995c", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_7656bad163803b596999eb3843b4995c: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_7656bad163803b596999eb3843b4995c_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_7656bad163803b596999eb3843b4995c_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_7656bad163803b596999eb3843b4995c_pb2.StreamSettings
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_7656bad163803b596999eb3843b4995c_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_7656bad163803b596999eb3843b4995c_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_7656bad163803b596999eb3843b4995c_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR_7656bad163803b596999eb3843b4995c: _Optional[str] = ...) -> None: ...
