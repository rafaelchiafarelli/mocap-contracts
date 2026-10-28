from harpia_generated.protofiles import CameraQuality_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CameraQuality_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import BoneStability_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _BoneStability_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import CameraAblation_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CameraAblation_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QualityReport(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "ablation", "bones", "calibration_reproj_err_px", "cameras", "take_id"]
    ABLATION_FIELD_NUMBER: _ClassVar[int]
    BONES_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ablation: _containers.RepeatedCompositeFieldContainer[_CameraAblation_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraAblation]
    bones: _containers.RepeatedCompositeFieldContainer[_BoneStability_136996d09eedbf0a12cec4204d8d4ec2_pb2.BoneStability]
    calibration_reproj_err_px: float
    cameras: _containers.RepeatedCompositeFieldContainer[_CameraQuality_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraQuality]
    take_id: str
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., take_id: _Optional[str] = ..., calibration_reproj_err_px: _Optional[float] = ..., cameras: _Optional[_Iterable[_Union[_CameraQuality_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraQuality, _Mapping]]] = ..., bones: _Optional[_Iterable[_Union[_BoneStability_136996d09eedbf0a12cec4204d8d4ec2_pb2.BoneStability, _Mapping]]] = ..., ablation: _Optional[_Iterable[_Union[_CameraAblation_136996d09eedbf0a12cec4204d8d4ec2_pb2.CameraAblation, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
