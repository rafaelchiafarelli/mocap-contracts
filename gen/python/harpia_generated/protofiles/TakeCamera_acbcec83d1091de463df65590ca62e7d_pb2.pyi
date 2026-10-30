from harpia_generated.protofiles import CameraConfig_acbcec83d1091de463df65590ca62e7d_pb2 as _CameraConfig_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import ControlResult_acbcec83d1091de463df65590ca62e7d_pb2 as _ControlResult_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import CameraControls_acbcec83d1091de463df65590ca62e7d_pb2 as _CameraControls_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import PreprocessSpec_acbcec83d1091de463df65590ca62e7d_pb2 as _PreprocessSpec_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    applied_controls: _CameraControls_acbcec83d1091de463df65590ca62e7d_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_acbcec83d1091de463df65590ca62e7d_pb2.PreprocessSpec
    config: _CameraConfig_acbcec83d1091de463df65590ca62e7d_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_acbcec83d1091de463df65590ca62e7d_pb2.ControlResult]
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_acbcec83d1091de463df65590ca62e7d_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_acbcec83d1091de463df65590ca62e7d_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_acbcec83d1091de463df65590ca62e7d_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_acbcec83d1091de463df65590ca62e7d_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
