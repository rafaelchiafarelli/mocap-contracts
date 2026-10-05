from harpia_generated.protofiles import StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import DeviceInfo_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _DeviceInfo_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlReply(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "device_info", "problems", "request_id", "results", "serial", "stream_applied"]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0: str
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    STREAM_APPLIED_FIELD_NUMBER: _ClassVar[int]
    device_info: _DeviceInfo_c4b8ea5558d6147d937c128fc2703ba0_pb2.DeviceInfo
    problems: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[_ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlResult]
    serial: str
    stream_applied: _StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2.StreamSettings
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., request_id: _Optional[str] = ..., serial: _Optional[str] = ..., stream_applied: _Optional[_Union[_StreamSettings_c4b8ea5558d6147d937c128fc2703ba0_pb2.StreamSettings, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlResult, _Mapping]]] = ..., device_info: _Optional[_Union[_DeviceInfo_c4b8ea5558d6147d937c128fc2703ba0_pb2.DeviceInfo, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ...) -> None: ...
