from harpia_generated.protofiles import StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2 as _StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2 as _ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import DeviceInfo_ae090d6fa4827e92540c3f916b30649f_pb2 as _DeviceInfo_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR_ae090d6fa4827e92540c3f916b30649f", "STATUS_ae090d6fa4827e92540c3f916b30649f", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_ae090d6fa4827e92540c3f916b30649f: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_ae090d6fa4827e92540c3f916b30649f_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2.StreamSettings
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_ae090d6fa4827e92540c3f916b30649f_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ...) -> None: ...
