from harpia_generated.protofiles import Flag_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _Flag_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import CameraTakeReport_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _CameraTakeReport_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "ok", "problems", "reports", "take_id"]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_61c8c10158ef4d464aeae2ffe73974e6_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_61c8c10158ef4d464aeae2ffe73974e6_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_61c8c10158ef4d464aeae2ffe73974e6_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_61c8c10158ef4d464aeae2ffe73974e6_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
