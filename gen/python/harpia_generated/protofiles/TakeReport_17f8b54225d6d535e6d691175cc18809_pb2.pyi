from harpia_generated.protofiles import Flag_17f8b54225d6d535e6d691175cc18809_pb2 as _Flag_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import CameraTakeReport_17f8b54225d6d535e6d691175cc18809_pb2 as _CameraTakeReport_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "ok", "problems", "reports", "take_id"]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_17f8b54225d6d535e6d691175cc18809_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_17f8b54225d6d535e6d691175cc18809_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_17f8b54225d6d535e6d691175cc18809_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_17f8b54225d6d535e6d691175cc18809_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
