from harpia_generated.protofiles import CameraConfig_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _CameraConfig_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import ControlResult_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _ControlResult_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import CameraControls_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _CameraControls_61c8c10158ef4d464aeae2ffe73974e6_pb2
from harpia_generated.protofiles import PreprocessSpec_61c8c10158ef4d464aeae2ffe73974e6_pb2 as _PreprocessSpec_61c8c10158ef4d464aeae2ffe73974e6_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCamera(_message.Message):
    __slots__ = ["ERROR_61c8c10158ef4d464aeae2ffe73974e6", "ID_61c8c10158ef4d464aeae2ffe73974e6", "ORIGINATOR", "STATUS_61c8c10158ef4d464aeae2ffe73974e6", "applied_controls", "applied_preprocess", "config", "control_results"]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ERROR_61c8c10158ef4d464aeae2ffe73974e6: str
    ID_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    ID_61c8c10158ef4d464aeae2ffe73974e6: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_61C8C10158EF4D464AEAE2FFE73974E6_FIELD_NUMBER: _ClassVar[int]
    STATUS_61c8c10158ef4d464aeae2ffe73974e6: str
    applied_controls: _CameraControls_61c8c10158ef4d464aeae2ffe73974e6_pb2.CameraControls
    applied_preprocess: _PreprocessSpec_61c8c10158ef4d464aeae2ffe73974e6_pb2.PreprocessSpec
    config: _CameraConfig_61c8c10158ef4d464aeae2ffe73974e6_pb2.CameraConfig
    control_results: _containers.RepeatedCompositeFieldContainer[_ControlResult_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlResult]
    def __init__(self, ID_61c8c10158ef4d464aeae2ffe73974e6: _Optional[int] = ..., config: _Optional[_Union[_CameraConfig_61c8c10158ef4d464aeae2ffe73974e6_pb2.CameraConfig, _Mapping]] = ..., control_results: _Optional[_Iterable[_Union[_ControlResult_61c8c10158ef4d464aeae2ffe73974e6_pb2.ControlResult, _Mapping]]] = ..., applied_controls: _Optional[_Union[_CameraControls_61c8c10158ef4d464aeae2ffe73974e6_pb2.CameraControls, _Mapping]] = ..., applied_preprocess: _Optional[_Union[_PreprocessSpec_61c8c10158ef4d464aeae2ffe73974e6_pb2.PreprocessSpec, _Mapping]] = ..., STATUS_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ERROR_61c8c10158ef4d464aeae2ffe73974e6: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
