from harpia_generated.protofiles import CameraConfig_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraConfig_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import CameraControls_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraControls_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    applied_controls: _CameraControls_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PreprocessSpec
    config: _CameraConfig_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlResult]
    def __init__(self, HARPIA_ID: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PreprocessSpec, _Mapping]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
