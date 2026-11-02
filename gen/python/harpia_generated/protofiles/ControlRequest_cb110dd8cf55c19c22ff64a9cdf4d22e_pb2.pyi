from harpia_generated.protofiles import StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlSetting]
    stream: _StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.StreamSettings
    want_device_info: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    def __init__(self, HARPIA_ID: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
