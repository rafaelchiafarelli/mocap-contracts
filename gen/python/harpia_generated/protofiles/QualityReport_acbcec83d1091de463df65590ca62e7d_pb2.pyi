from harpia_generated.protofiles import CameraQuality_acbcec83d1091de463df65590ca62e7d_pb2 as _CameraQuality_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import BoneStability_acbcec83d1091de463df65590ca62e7d_pb2 as _BoneStability_acbcec83d1091de463df65590ca62e7d_pb2
from harpia_generated.protofiles import CameraAblation_acbcec83d1091de463df65590ca62e7d_pb2 as _CameraAblation_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QualityReport(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "ablation", "bones", "calibration_reproj_err_px", "cameras", "take_id"]
    ABLATION_FIELD_NUMBER: _ClassVar[int]
    BONES_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ablation: _containers.RepeatedCompositeFieldContainer[_CameraAblation_acbcec83d1091de463df65590ca62e7d_pb2.CameraAblation]
    bones: _containers.RepeatedCompositeFieldContainer[_BoneStability_acbcec83d1091de463df65590ca62e7d_pb2.BoneStability]
    calibration_reproj_err_px: float
    cameras: _containers.RepeatedCompositeFieldContainer[_CameraQuality_acbcec83d1091de463df65590ca62e7d_pb2.CameraQuality]
    take_id: str
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., take_id: _Optional[str] = ..., calibration_reproj_err_px: _Optional[float] = ..., cameras: _Optional[_Iterable[_Union[_CameraQuality_acbcec83d1091de463df65590ca62e7d_pb2.CameraQuality, _Mapping]]] = ..., bones: _Optional[_Iterable[_Union[_BoneStability_acbcec83d1091de463df65590ca62e7d_pb2.BoneStability, _Mapping]]] = ..., ablation: _Optional[_Iterable[_Union[_CameraAblation_acbcec83d1091de463df65590ca62e7d_pb2.CameraAblation, _Mapping]]] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
