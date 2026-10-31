from harpia_generated.protofiles import Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapFrame(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "body_missing", "body_xyz", "emotion", "face_blendshapes", "frame_id", "gaze", "left_foot_contact", "left_hand_missing", "left_hand_xyz", "right_foot_contact", "right_hand_missing", "right_hand_xyz", "timestamp_ns"]
    BODY_MISSING_FIELD_NUMBER: _ClassVar[int]
    BODY_XYZ_FIELD_NUMBER: _ClassVar[int]
    EMOTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FACE_BLENDSHAPES_FIELD_NUMBER: _ClassVar[int]
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    GAZE_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    LEFT_FOOT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    LEFT_HAND_MISSING_FIELD_NUMBER: _ClassVar[int]
    LEFT_HAND_XYZ_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FOOT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_HAND_MISSING_FIELD_NUMBER: _ClassVar[int]
    RIGHT_HAND_XYZ_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    TIMESTAMP_NS_FIELD_NUMBER: _ClassVar[int]
    body_missing: _containers.RepeatedScalarFieldContainer[int]
    body_xyz: _containers.RepeatedScalarFieldContainer[float]
    emotion: str
    face_blendshapes: _containers.RepeatedScalarFieldContainer[float]
    frame_id: int
    gaze: _containers.RepeatedScalarFieldContainer[float]
    left_foot_contact: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    left_hand_missing: _containers.RepeatedScalarFieldContainer[int]
    left_hand_xyz: _containers.RepeatedScalarFieldContainer[float]
    right_foot_contact: _Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag
    right_hand_missing: _containers.RepeatedScalarFieldContainer[int]
    right_hand_xyz: _containers.RepeatedScalarFieldContainer[float]
    timestamp_ns: int
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., frame_id: _Optional[int] = ..., timestamp_ns: _Optional[int] = ..., body_xyz: _Optional[_Iterable[float]] = ..., left_hand_xyz: _Optional[_Iterable[float]] = ..., right_hand_xyz: _Optional[_Iterable[float]] = ..., body_missing: _Optional[_Iterable[int]] = ..., left_hand_missing: _Optional[_Iterable[int]] = ..., right_hand_missing: _Optional[_Iterable[int]] = ..., face_blendshapes: _Optional[_Iterable[float]] = ..., gaze: _Optional[_Iterable[float]] = ..., emotion: _Optional[str] = ..., left_foot_contact: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., right_foot_contact: _Optional[_Union[_Flag_e51d6d03132b4baa0ced72cde01af9d0_pb2.Flag, str]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
