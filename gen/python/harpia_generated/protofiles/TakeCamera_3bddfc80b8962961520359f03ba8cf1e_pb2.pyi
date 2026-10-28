from harpia_generated.protofiles import CameraConfig_3bddfc80b8962961520359f03ba8cf1e_pb2 as _CameraConfig_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2 as _ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import CameraControls_3bddfc80b8962961520359f03ba8cf1e_pb2 as _CameraControls_3bddfc80b8962961520359f03ba8cf1e_pb2
from harpia_generated.protofiles import PreprocessSpec_3bddfc80b8962961520359f03ba8cf1e_pb2 as _PreprocessSpec_3bddfc80b8962961520359f03ba8cf1e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_3bddfc80b8962961520359f03ba8cf1e", "ID_3bddfc80b8962961520359f03ba8cf1e", "ORIGINATOR", "STATUS_3bddfc80b8962961520359f03ba8cf1e", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ERROR_3bddfc80b8962961520359f03ba8cf1e: str
    ID_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    ID_3bddfc80b8962961520359f03ba8cf1e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_3BDDFC80B8962961520359F03BA8CF1E_FIELD_NUMBER: _ClassVar[int]
    STATUS_3bddfc80b8962961520359f03ba8cf1e: str
    applied_controls: _CameraControls_3bddfc80b8962961520359f03ba8cf1e_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_3bddfc80b8962961520359f03ba8cf1e_pb2.PreprocessSpec
    config: _CameraConfig_3bddfc80b8962961520359f03ba8cf1e_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlResult]
    def __init__(self, ID_3bddfc80b8962961520359f03ba8cf1e: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_3bddfc80b8962961520359f03ba8cf1e_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_3bddfc80b8962961520359f03ba8cf1e_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_3bddfc80b8962961520359f03ba8cf1e_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_3bddfc80b8962961520359f03ba8cf1e_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ERROR_3bddfc80b8962961520359f03ba8cf1e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
