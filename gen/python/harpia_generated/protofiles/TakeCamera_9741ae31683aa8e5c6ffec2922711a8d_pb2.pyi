from harpia_generated.protofiles import CameraConfig_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _CameraConfig_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import ControlResult_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _ControlResult_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import CameraControls_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _CameraControls_9741ae31683aa8e5c6ffec2922711a8d_pb2
from harpia_generated.protofiles import PreprocessSpec_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _PreprocessSpec_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    applied_controls: _CameraControls_9741ae31683aa8e5c6ffec2922711a8d_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_9741ae31683aa8e5c6ffec2922711a8d_pb2.PreprocessSpec
    config: _CameraConfig_9741ae31683aa8e5c6ffec2922711a8d_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlResult]
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_9741ae31683aa8e5c6ffec2922711a8d_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_9741ae31683aa8e5c6ffec2922711a8d_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_9741ae31683aa8e5c6ffec2922711a8d_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_9741ae31683aa8e5c6ffec2922711a8d_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
