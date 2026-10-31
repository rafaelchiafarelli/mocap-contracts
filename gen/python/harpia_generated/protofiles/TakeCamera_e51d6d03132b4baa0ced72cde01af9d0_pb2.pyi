from harpia_generated.protofiles import CameraConfig_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _CameraConfig_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import CameraControls_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _CameraControls_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    applied_controls: _CameraControls_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2.PreprocessSpec
    config: _CameraConfig_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlResult]
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_e51d6d03132b4baa0ced72cde01af9d0_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_e51d6d03132b4baa0ced72cde01af9d0_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_e51d6d03132b4baa0ced72cde01af9d0_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
