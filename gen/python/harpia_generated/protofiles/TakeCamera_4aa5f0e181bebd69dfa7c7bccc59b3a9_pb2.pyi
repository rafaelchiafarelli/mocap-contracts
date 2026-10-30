from harpia_generated.protofiles import CameraConfig_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _CameraConfig_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import ControlResult_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _ControlResult_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import CameraControls_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _CameraControls_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import PreprocessSpec_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _PreprocessSpec_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    applied_controls: _CameraControls_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PreprocessSpec
    config: _CameraConfig_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlResult]
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
