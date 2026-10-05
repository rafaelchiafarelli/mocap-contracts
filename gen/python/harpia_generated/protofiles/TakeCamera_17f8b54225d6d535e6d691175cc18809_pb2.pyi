from harpia_generated.protofiles import CameraConfig_17f8b54225d6d535e6d691175cc18809_pb2 as _CameraConfig_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import ControlResult_17f8b54225d6d535e6d691175cc18809_pb2 as _ControlResult_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import CameraControls_17f8b54225d6d535e6d691175cc18809_pb2 as _CameraControls_17f8b54225d6d535e6d691175cc18809_pb2
from harpia_generated.protofiles import PreprocessSpec_17f8b54225d6d535e6d691175cc18809_pb2 as _PreprocessSpec_17f8b54225d6d535e6d691175cc18809_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_17f8b54225d6d535e6d691175cc18809", "ID_17f8b54225d6d535e6d691175cc18809", "ORIGINATOR", "STATUS_17f8b54225d6d535e6d691175cc18809", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ERROR_17f8b54225d6d535e6d691175cc18809: str
    ID_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    ID_17f8b54225d6d535e6d691175cc18809: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_17F8B54225D6D535E6D691175CC18809_FIELD_NUMBER: _ClassVar[int]
    STATUS_17f8b54225d6d535e6d691175cc18809: str
    applied_controls: _CameraControls_17f8b54225d6d535e6d691175cc18809_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_17f8b54225d6d535e6d691175cc18809_pb2.PreprocessSpec
    config: _CameraConfig_17f8b54225d6d535e6d691175cc18809_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_17f8b54225d6d535e6d691175cc18809_pb2.ControlResult]
    def __init__(self, ID_17f8b54225d6d535e6d691175cc18809: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_17f8b54225d6d535e6d691175cc18809_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_17f8b54225d6d535e6d691175cc18809_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_17f8b54225d6d535e6d691175cc18809_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_17f8b54225d6d535e6d691175cc18809_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ERROR_17f8b54225d6d535e6d691175cc18809: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
