from harpia_generated.protofiles import StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2 as _StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2 as _ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import Flag_ae090d6fa4827e92540c3f916b30649f_pb2 as _Flag_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR_ae090d6fa4827e92540c3f916b30649f", "STATUS_ae090d6fa4827e92540c3f916b30649f", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_ae090d6fa4827e92540c3f916b30649f: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2.ControlSetting]
    stream: _StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2.StreamSettings
    want_device_info: _Flag_ae090d6fa4827e92540c3f916b30649f_pb2.Flag
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_ae090d6fa4827e92540c3f916b30649f_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_ae090d6fa4827e92540c3f916b30649f_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_ae090d6fa4827e92540c3f916b30649f_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ...) -> None: ...
