from harpia_generated.protofiles import Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import CameraTakeReport_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CameraTakeReport_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeReport(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "ok", "problems", "reports", "take_id"]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    OK_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ok: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    problems: _containers.RepeatedScalarFieldContainer[str]
    reports: _containers.RepeatedCompositeFieldContainer[_CameraTakeReport_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraTakeReport]
    take_id: str
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., take_id: _Optional[str] = ..., ok: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., problems: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[_CameraTakeReport_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraTakeReport, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
