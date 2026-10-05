from harpia_generated.protofiles import ControlValue_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _ControlValue_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import ControlStatus_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _ControlStatus_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlResult(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "applied", "key", "note", "requested", "status"]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    applied: _ControlValue_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlValue
    key: str
    note: str
    requested: _ControlValue_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlValue
    status: _ControlStatus_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlStatus
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., key: _Optional[str] = ..., requested: _Optional[_Union[_ControlValue_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlValue, _Mapping]] = ..., applied: _Optional[_Union[_ControlValue_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlValue, _Mapping]] = ..., status: _Optional[_Union[_ControlStatus_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlStatus, str]] = ..., note: _Optional[str] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
