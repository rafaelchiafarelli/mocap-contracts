from harpia_generated.protofiles import CameraConfig_ae090d6fa4827e92540c3f916b30649f_pb2 as _CameraConfig_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2 as _ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import CameraControls_ae090d6fa4827e92540c3f916b30649f_pb2 as _CameraControls_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2 as _PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    applied_controls: _CameraControls_ae090d6fa4827e92540c3f916b30649f_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2.PreprocessSpec
    config: _CameraConfig_ae090d6fa4827e92540c3f916b30649f_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2.ControlResult]
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_ae090d6fa4827e92540c3f916b30649f_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_ae090d6fa4827e92540c3f916b30649f_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_ae090d6fa4827e92540c3f916b30649f_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_ae090d6fa4827e92540c3f916b30649f_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
