from harpia_generated.protofiles import CameraQuality_7656bad163803b596999eb3843b4995c_pb2 as _CameraQuality_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import BoneStability_7656bad163803b596999eb3843b4995c_pb2 as _BoneStability_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import CameraAblation_7656bad163803b596999eb3843b4995c_pb2 as _CameraAblation_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QualityReport(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "ablation", "bones", "calibration_reproj_err_px", "cameras", "take_id"]
    ABLATION_FIELD_NUMBER: _ClassVar[int]
    BONES_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ablation: _containers.RepeatedCompositeFieldContainer[_CameraAblation_7656bad163803b596999eb3843b4995c_pb2.CameraAblation]
    bones: _containers.RepeatedCompositeFieldContainer[_BoneStability_7656bad163803b596999eb3843b4995c_pb2.BoneStability]
    calibration_reproj_err_px: float
    cameras: _containers.RepeatedCompositeFieldContainer[_CameraQuality_7656bad163803b596999eb3843b4995c_pb2.CameraQuality]
    take_id: str
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., take_id: _Optional[str] = ..., calibration_reproj_err_px: _Optional[float] = ..., cameras: _Optional[_Iterable[_Union[_CameraQuality_7656bad163803b596999eb3843b4995c_pb2.CameraQuality, _Mapping]]] = ..., bones: _Optional[_Iterable[_Union[_BoneStability_7656bad163803b596999eb3843b4995c_pb2.BoneStability, _Mapping]]] = ..., ablation: _Optional[_Iterable[_Union[_CameraAblation_7656bad163803b596999eb3843b4995c_pb2.CameraAblation, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
