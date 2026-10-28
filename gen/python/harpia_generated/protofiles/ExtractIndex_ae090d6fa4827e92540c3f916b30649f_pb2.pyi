from harpia_generated.protofiles import LengthUnit_ae090d6fa4827e92540c3f916b30649f_pb2 as _LengthUnit_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import UpAxis_ae090d6fa4827e92540c3f916b30649f_pb2 as _UpAxis_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import SyncedVideo_ae090d6fa4827e92540c3f916b30649f_pb2 as _SyncedVideo_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import CameraAlignment_ae090d6fa4827e92540c3f916b30649f_pb2 as _CameraAlignment_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import PointSet_ae090d6fa4827e92540c3f916b30649f_pb2 as _PointSet_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractIndex(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "alignment", "calibration_path", "calibration_take_id", "fps", "frames", "length_unit", "points_2d", "points_3d", "synced_videos", "t0_ns", "take_id", "up_axis"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_PATH_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    FPS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    LENGTH_UNIT_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    POINTS_2D_FIELD_NUMBER: _ClassVar[int]
    POINTS_3D_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    SYNCED_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    T0_NS_FIELD_NUMBER: _ClassVar[int]
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    UP_AXIS_FIELD_NUMBER: _ClassVar[int]
    alignment: _containers.RepeatedCompositeFieldContainer[_CameraAlignment_ae090d6fa4827e92540c3f916b30649f_pb2.CameraAlignment]
    calibration_path: str
    calibration_take_id: str
    fps: float
    frames: int
    length_unit: _LengthUnit_ae090d6fa4827e92540c3f916b30649f_pb2.LengthUnit
    points_2d: _containers.RepeatedCompositeFieldContainer[_PointSet_ae090d6fa4827e92540c3f916b30649f_pb2.PointSet]
    points_3d: _containers.RepeatedCompositeFieldContainer[_PointSet_ae090d6fa4827e92540c3f916b30649f_pb2.PointSet]
    synced_videos: _containers.RepeatedCompositeFieldContainer[_SyncedVideo_ae090d6fa4827e92540c3f916b30649f_pb2.SyncedVideo]
    t0_ns: int
    take_id: str
    up_axis: _UpAxis_ae090d6fa4827e92540c3f916b30649f_pb2.UpAxis
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., take_id: _Optional[str] = ..., calibration_take_id: _Optional[str] = ..., calibration_path: _Optional[str] = ..., fps: _Optional[float] = ..., frames: _Optional[int] = ..., t0_ns: _Optional[int] = ..., length_unit: _Optional[_Union[_LengthUnit_ae090d6fa4827e92540c3f916b30649f_pb2.LengthUnit, str]] = ..., up_axis: _Optional[_Union[_UpAxis_ae090d6fa4827e92540c3f916b30649f_pb2.UpAxis, str]] = ..., synced_videos: _Optional[_Iterable[_Union[_SyncedVideo_ae090d6fa4827e92540c3f916b30649f_pb2.SyncedVideo, _Mapping]]] = ..., alignment: _Optional[_Iterable[_Union[_CameraAlignment_ae090d6fa4827e92540c3f916b30649f_pb2.CameraAlignment, _Mapping]]] = ..., points_3d: _Optional[_Iterable[_Union[_PointSet_ae090d6fa4827e92540c3f916b30649f_pb2.PointSet, _Mapping]]] = ..., points_2d: _Optional[_Iterable[_Union[_PointSet_ae090d6fa4827e92540c3f916b30649f_pb2.PointSet, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
