from harpia_generated.protofiles import StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2 as _StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2 as _ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import DeviceInfo_3bddfc80b8962961520359f03ba8cf1e_pb2 as _DeviceInfo_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ORIGINATOR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_3bddfc80b8962961520359f03ba8cf1e_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2.StreamSettings
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_3bddfc80b8962961520359f03ba8cf1e_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_3bddfc80b8962961520359f03ba8cf1e_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ...) -> None: ...
