from harpia_generated.protofiles import Flag_7656bad163803b596999eb3843b4995c_pb2 as _Flag_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import CameraTakeReport_7656bad163803b596999eb3843b4995c_pb2 as _CameraTakeReport_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "ok", "problems", "reports", "take_id"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_7656bad163803b596999eb3843b4995c_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_7656bad163803b596999eb3843b4995c_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
