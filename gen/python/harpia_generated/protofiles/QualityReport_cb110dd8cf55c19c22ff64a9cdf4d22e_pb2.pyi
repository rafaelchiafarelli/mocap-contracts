from harpia_generated.protofiles import CameraQuality_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraQuality_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import BoneStability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _BoneStability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import CameraAblation_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _CameraAblation_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QualityReport(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "ablation", "bones", "calibration_reproj_err_px", "cameras", "take_id"]
    ABLATION_FIELD_NUMBER: _ClassVar[int]
    BONES_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ablation: _containers.RepeatedCompositeFieldContainer[_CameraAblation_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraAblation]
    bones: _containers.RepeatedCompositeFieldContainer[_BoneStability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BoneStability]
    calibration_reproj_err_px: float
    cameras: _containers.RepeatedCompositeFieldContainer[_CameraQuality_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraQuality]
    take_id: str
    def __init__(self, HARPIA_ID: _Optional[int] = ..., take_id: _Optional[str] = ..., calibration_reproj_err_px: _Optional[float] = ..., cameras: _Optional[_Iterable[_Union[_CameraQuality_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraQuality, _Mapping]]] = ..., bones: _Optional[_Iterable[_Union[_BoneStability_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.BoneStability, _Mapping]]] = ..., ablation: _Optional[_Iterable[_Union[_CameraAblation_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.CameraAblation, _Mapping]]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
