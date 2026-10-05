from harpia_generated.protofiles import Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import CameraTakeReport_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraTakeReport_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "ok", "problems", "reports", "take_id"]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_c4b8ea5558d6147d937c128fc2703ba0_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
