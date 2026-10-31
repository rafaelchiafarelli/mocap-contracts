from harpia_generated.protofiles import LengthUnit_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _LengthUnit_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import UpAxis_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _UpAxis_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MocapTakeHeader(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "actor_id", "body_joints", "character_id", "face_blendshape_names", "fps", "frame_count", "left_hand_joints", "length_unit", "right_hand_joints", "session_id", "t0_ns", "take_id", "up_axis"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    BODY_JOINTS_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    FACE_BLENDSHAPE_NAMES_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    LEFT_HAND_JOINTS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_UNIT_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    RIGHT_HAND_JOINTS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    T0_NS_FIELD_NUMBER: _ClassVar[int]
    TAKE_ID_FIELD_NUMBER: _ClassVar[int]
    UP_AXIS_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    body_joints: _containers.RepeatedScalarFieldContainer[str]
    character_id: str
    face_blendshape_names: _containers.RepeatedScalarFieldContainer[str]
    fps: float
    frame_count: int
    left_hand_joints: _containers.RepeatedScalarFieldContainer[str]
    length_unit: _LengthUnit_e51d6d03132b4baa0ced72cde01af9d0_pb2.LengthUnit
    right_hand_joints: _containers.RepeatedScalarFieldContainer[str]
    session_id: str
    t0_ns: int
    take_id: str
    up_axis: _UpAxis_e51d6d03132b4baa0ced72cde01af9d0_pb2.UpAxis
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., take_id: _Optional[str] = ..., session_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., character_id: _Optional[str] = ..., fps: _Optional[float] = ..., frame_count: _Optional[int] = ..., t0_ns: _Optional[int] = ..., length_unit: _Optional[_Union[_LengthUnit_e51d6d03132b4baa0ced72cde01af9d0_pb2.LengthUnit, str]] = ..., up_axis: _Optional[_Union[_UpAxis_e51d6d03132b4baa0ced72cde01af9d0_pb2.UpAxis, str]] = ..., body_joints: _Optional[_Iterable[str]] = ..., left_hand_joints: _Optional[_Iterable[str]] = ..., right_hand_joints: _Optional[_Iterable[str]] = ..., face_blendshape_names: _Optional[_Iterable[str]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
