from harpia_generated.protofiles import TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrontMatter(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "argument", "overview", "pitch", "title"]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    argument: _Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Argument
    overview: _Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Overview
    pitch: _Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Pitch
    title: _TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitlePage
    def __init__(self, HARPIA_ID: _Optional[int] = ..., title: _Optional[_Union[_TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitlePage, _Mapping]] = ..., overview: _Optional[_Union[_Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Overview, _Mapping]] = ..., pitch: _Optional[_Union[_Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Pitch, _Mapping]] = ..., argument: _Optional[_Union[_Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Argument, _Mapping]] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
