from harpia_generated.protofiles import ControlValue_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlValue_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import ControlStatus_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlStatus_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    applied: _ControlValue_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlValue
    status: _ControlStatus_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlStatus
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
