from harpia_generated.protofiles import Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapFrame(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "body_missing", "body_xyz", "emotion", "face_blendshapes", "frame_id", "gaze", "left_foot_contact", "left_hand_missing", "left_hand_xyz", "right_foot_contact", "right_hand_missing", "right_hand_xyz", "timestamp_ns"]
    BODY_MISSING_FIELD_NUMBER: _ClassVar[int]
    BODY_XYZ_FIELD_NUMBER: _ClassVar[int]
    EMOTION_FIELD_NUMBER: _ClassVar[int]
    FACE_BLENDSHAPES_FIELD_NUMBER: _ClassVar[int]
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    GAZE_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    LEFT_FOOT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    LEFT_HAND_MISSING_FIELD_NUMBER: _ClassVar[int]
    LEFT_HAND_XYZ_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FOOT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_HAND_MISSING_FIELD_NUMBER: _ClassVar[int]
    RIGHT_HAND_XYZ_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_NS_FIELD_NUMBER: _ClassVar[int]
    body_missing: _containers.RepeatedScalarFieldContainer[int]
    body_xyz: _containers.RepeatedScalarFieldContainer[float]
    emotion: str
    face_blendshapes: _containers.RepeatedScalarFieldContainer[float]
    frame_id: int
    gaze: _containers.RepeatedScalarFieldContainer[float]
    left_foot_contact: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    left_hand_missing: _containers.RepeatedScalarFieldContainer[int]
    left_hand_xyz: _containers.RepeatedScalarFieldContainer[float]
    right_foot_contact: _Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag
    right_hand_missing: _containers.RepeatedScalarFieldContainer[int]
    right_hand_xyz: _containers.RepeatedScalarFieldContainer[float]
    timestamp_ns: int
    def __init__(self, HARPIA_ID: _Optional[int] = ..., frame_id: _Optional[int] = ..., timestamp_ns: _Optional[int] = ..., body_xyz: _Optional[_Iterable[float]] = ..., left_hand_xyz: _Optional[_Iterable[float]] = ..., right_hand_xyz: _Optional[_Iterable[float]] = ..., body_missing: _Optional[_Iterable[int]] = ..., left_hand_missing: _Optional[_Iterable[int]] = ..., right_hand_missing: _Optional[_Iterable[int]] = ..., face_blendshapes: _Optional[_Iterable[float]] = ..., gaze: _Optional[_Iterable[float]] = ..., emotion: _Optional[str] = ..., left_foot_contact: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., right_foot_contact: _Optional[_Union[_Flag_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Flag, str]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
