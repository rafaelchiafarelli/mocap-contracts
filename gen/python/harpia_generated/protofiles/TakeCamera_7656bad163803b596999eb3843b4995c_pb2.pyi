from harpia_generated.protofiles import CameraConfig_7656bad163803b596999eb3843b4995c_pb2 as _CameraConfig_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import ControlResult_7656bad163803b596999eb3843b4995c_pb2 as _ControlResult_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import CameraControls_7656bad163803b596999eb3843b4995c_pb2 as _CameraControls_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import PreprocessSpec_7656bad163803b596999eb3843b4995c_pb2 as _PreprocessSpec_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    applied_controls: _CameraControls_7656bad163803b596999eb3843b4995c_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_7656bad163803b596999eb3843b4995c_pb2.PreprocessSpec
    config: _CameraConfig_7656bad163803b596999eb3843b4995c_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_7656bad163803b596999eb3843b4995c_pb2.ControlResult]
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_7656bad163803b596999eb3843b4995c_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_7656bad163803b596999eb3843b4995c_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_7656bad163803b596999eb3843b4995c_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_7656bad163803b596999eb3843b4995c_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
