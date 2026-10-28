from harpia_generated.protofiles import Flag_ae090d6fa4827e92540c3f916b30649f_pb2 as _Flag_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import CameraTakeReport_ae090d6fa4827e92540c3f916b30649f_pb2 as _CameraTakeReport_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "ok", "problems", "reports", "take_id"]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_ae090d6fa4827e92540c3f916b30649f_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_ae090d6fa4827e92540c3f916b30649f_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_ae090d6fa4827e92540c3f916b30649f_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_ae090d6fa4827e92540c3f916b30649f_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
