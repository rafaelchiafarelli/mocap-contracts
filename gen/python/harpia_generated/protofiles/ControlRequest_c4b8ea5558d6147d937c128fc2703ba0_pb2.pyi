from harpia_generated.protofiles import StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "reply_endpoint", "request_id", "serial", "settings", "stream", "want_device_info"]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0: str
    REPLY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WANT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    reply_endpoint: str
    request_id: str
    serial: str
    settings: _containers.RepeatedCompositeFieldContainer[_ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlSetting]
    stream: _StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2.StreamSettings
    want_device_info: _Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2.Flag
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream: _Optional[_Union[_StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2.StreamSettings, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[_ControlSetting_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlSetting, _Mapping]]] = ..., want_device_info: _Optional[_Union[_Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2.Flag, str]] = ..., reply_endpoint: _Optional[str] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ...) -> None: ...
