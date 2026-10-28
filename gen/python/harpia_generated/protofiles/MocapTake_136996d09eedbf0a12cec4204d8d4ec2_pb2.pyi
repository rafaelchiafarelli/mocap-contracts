from harpia_generated.protofiles import MocapTakeHeader_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _MocapTakeHeader_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import MocapFrame_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _MocapFrame_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTake(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "frames", "header"]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    frames: _containers.RepeatedCompositeFieldContainer[_MocapFrame_136996d09eedbf0a12cec4204d8d4ec2_pb2.MocapFrame]
    header: _MocapTakeHeader_136996d09eedbf0a12cec4204d8d4ec2_pb2.MocapTakeHeader
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., header: _Optional[_Union[_MocapTakeHeader_136996d09eedbf0a12cec4204d8d4ec2_pb2.MocapTakeHeader, _Mapping]] = ..., frames: _Optional[_Iterable[_Union[_MocapFrame_136996d09eedbf0a12cec4204d8d4ec2_pb2.MocapFrame, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
