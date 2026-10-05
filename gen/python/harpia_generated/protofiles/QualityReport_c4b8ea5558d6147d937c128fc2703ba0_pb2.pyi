from harpia_generated.protofiles import CameraQuality_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraQuality_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import BoneStability_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _BoneStability_c4b8ea5558d6147d937c128fc2703ba0_pb2
from harpia_generated.protofiles import CameraAblation_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _CameraAblation_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QualityReport(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "ablation", "bones", "calibration_reproj_err_px", "cameras", "take_id"]
    ABLATION_FIELD_NUMBER: _ClassVar[int]
    BONES_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REPROJ_ERR_PX_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ablation: _containers.RepeatedCompositeFieldContainer[_CameraAblation_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraAblation]
    bones: _containers.RepeatedCompositeFieldContainer[_BoneStability_c4b8ea5558d6147d937c128fc2703ba0_pb2.BoneStability]
    calibration_reproj_err_px: float
    cameras: _containers.RepeatedCompositeFieldContainer[_CameraQuality_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraQuality]
    take_id: str
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., take_id: _Optional[str] = ..., calibration_reproj_err_px: _Optional[float] = ..., cameras: _Optional[_Iterable[_Union[_CameraQuality_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraQuality, _Mapping]]] = ..., bones: _Optional[_Iterable[_Union[_BoneStability_c4b8ea5558d6147d937c128fc2703ba0_pb2.BoneStability, _Mapping]]] = ..., ablation: _Optional[_Iterable[_Union[_CameraAblation_c4b8ea5558d6147d937c128fc2703ba0_pb2.CameraAblation, _Mapping]]] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
