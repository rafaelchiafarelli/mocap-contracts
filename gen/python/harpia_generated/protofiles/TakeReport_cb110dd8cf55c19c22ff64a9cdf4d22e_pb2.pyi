from harpia_generated.protofiles import Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import CameraTakeReport_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraTakeReport_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "ok", "problems", "reports", "take_id"]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
