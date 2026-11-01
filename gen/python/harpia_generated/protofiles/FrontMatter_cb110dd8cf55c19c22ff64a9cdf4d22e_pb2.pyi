from harpia_generated.protofiles import TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrontMatter(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "argument", "overview", "pitch", "title"]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    TITLE_FIELD_NUMBER: _ClassVar[int]
    argument: _Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Argument
    overview: _Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Overview
    pitch: _Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Pitch
    title: _TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitlePage
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., title: _Optional[_Union[_TitlePage_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitlePage, _Mapping]] = ..., overview: _Optional[_Union[_Overview_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Overview, _Mapping]] = ..., pitch: _Optional[_Union[_Pitch_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Pitch, _Mapping]] = ..., argument: _Optional[_Union[_Argument_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Argument, _Mapping]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
