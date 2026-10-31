from harpia_generated.protofiles import StreamSettings_186a1974c92f444f1bbc853569958a27_pb2 as _StreamSettings_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import ControlResult_186a1974c92f444f1bbc853569958a27_pb2 as _ControlResult_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import DeviceInfo_186a1974c92f444f1bbc853569958a27_pb2 as _DeviceInfo_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR_186a1974c92f444f1bbc853569958a27", "STATUS_186a1974c92f444f1bbc853569958a27", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_186a1974c92f444f1bbc853569958a27: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_186a1974c92f444f1bbc853569958a27_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_186a1974c92f444f1bbc853569958a27_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_186a1974c92f444f1bbc853569958a27_pb2.StreamSettings
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_186a1974c92f444f1bbc853569958a27_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_186a1974c92f444f1bbc853569958a27_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_186a1974c92f444f1bbc853569958a27_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ...) -> None: ...
