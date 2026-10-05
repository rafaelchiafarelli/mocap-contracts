from harpia_generated.protofiles import CameraConfig_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraConfig_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import CameraControls_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraControls_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    applied_controls: _CameraControls_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2.PreprocessSpec
    config: _CameraConfig_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlResult]
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_c4b8ea5558d6147d937c128fc2703ba0_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_c4b8ea5558d6147d937c128fc2703ba0_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
