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
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    applied_controls: _CameraControls_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PreprocessSpec
    config: _CameraConfig_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlResult]
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
