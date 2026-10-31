from harpia_generated.protofiles import StreamSettings_7656bad163803b596999eb3843b4995c_pb2 as _StreamSettings_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlSetting_7656bad163803b596999eb3843b4995c_pb2 as _ControlSetting_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import Flag_7656bad163803b596999eb3843b4995c_pb2 as _Flag_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR_7656bad163803b596999eb3843b4995c", "STATUS_7656bad163803b596999eb3843b4995c", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_7656bad163803b596999eb3843b4995c: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_7656bad163803b596999eb3843b4995c_pb2.ControlSetting]
    stream: _StreamSettings_7656bad163803b596999eb3843b4995c_pb2.StreamSettings
    want_device_info: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_7656bad163803b596999eb3843b4995c_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_7656bad163803b596999eb3843b4995c_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR_7656bad163803b596999eb3843b4995c: _Optional[str] = ...) -> None: ...
