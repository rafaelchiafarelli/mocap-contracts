from harpia_generated.protofiles import Flag_3bddfc80b8962961520359f03ba8cf1e_pb2 as _Flag_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import CameraTakeReport_3bddfc80b8962961520359f03ba8cf1e_pb2 as _CameraTakeReport_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "ok", "problems", "reports", "take_id"]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_3bddfc80b8962961520359f03ba8cf1e_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_3bddfc80b8962961520359f03ba8cf1e_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_3bddfc80b8962961520359f03ba8cf1e_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_3bddfc80b8962961520359f03ba8cf1e_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
