from harpia_generated.protofiles import CameraConfig_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CameraConfig_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import CameraControls_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CameraControls_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import PreprocessSpec_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _PreprocessSpec_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    applied_controls: _CameraControls_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_136996d09eedbf0a12cec4204d8d4ec2_pb2.PreprocessSpec
    config: _CameraConfig_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlResult]
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_136996d09eedbf0a12cec4204d8d4ec2_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_136996d09eedbf0a12cec4204d8d4ec2_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
