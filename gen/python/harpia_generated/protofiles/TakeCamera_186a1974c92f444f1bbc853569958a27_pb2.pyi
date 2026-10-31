from harpia_generated.protofiles import CameraConfig_186a1974c92f444f1bbc853569958a27_pb2 as _CameraConfig_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import ControlResult_186a1974c92f444f1bbc853569958a27_pb2 as _ControlResult_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import CameraControls_186a1974c92f444f1bbc853569958a27_pb2 as _CameraControls_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import PreprocessSpec_186a1974c92f444f1bbc853569958a27_pb2 as _PreprocessSpec_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    applied_controls: _CameraControls_186a1974c92f444f1bbc853569958a27_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_186a1974c92f444f1bbc853569958a27_pb2.PreprocessSpec
    config: _CameraConfig_186a1974c92f444f1bbc853569958a27_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_186a1974c92f444f1bbc853569958a27_pb2.ControlResult]
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_186a1974c92f444f1bbc853569958a27_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_186a1974c92f444f1bbc853569958a27_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_186a1974c92f444f1bbc853569958a27_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_186a1974c92f444f1bbc853569958a27_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
