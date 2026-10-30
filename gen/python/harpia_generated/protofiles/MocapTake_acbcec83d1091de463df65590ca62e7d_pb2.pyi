from harpia_generated.protofiles import MocapTakeHeader_acbcec83d1091de463df65590ca62e7d_pb2 as _MocapTakeHeader_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import MocapFrame_acbcec83d1091de463df65590ca62e7d_pb2 as _MocapFrame_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "frames", "header"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_acbcec83d1091de463df65590ca62e7d_pb2.MocapFrame]
    header: _MocapTakeHeader_acbcec83d1091de463df65590ca62e7d_pb2.MocapTakeHeader
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_acbcec83d1091de463df65590ca62e7d_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_acbcec83d1091de463df65590ca62e7d_pb2.MocapFrame, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
