from harpia_generated.protofiles import TitlePage_186a1974c92f444f1bbc853569958a27_pb2 as _TitlePage_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Overview_186a1974c92f444f1bbc853569958a27_pb2 as _Overview_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Pitch_186a1974c92f444f1bbc853569958a27_pb2 as _Pitch_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Argument_186a1974c92f444f1bbc853569958a27_pb2 as _Argument_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrontMatter(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "argument", "overview", "pitch", "title"]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    TITLE_FIELD_NUMBER: _ClassVar[int]
    argument: _Argument_186a1974c92f444f1bbc853569958a27_pb2.Argument
    overview: _Overview_186a1974c92f444f1bbc853569958a27_pb2.Overview
    pitch: _Pitch_186a1974c92f444f1bbc853569958a27_pb2.Pitch
    title: _TitlePage_186a1974c92f444f1bbc853569958a27_pb2.TitlePage
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., title: _Optional[_Union[_TitlePage_186a1974c92f444f1bbc853569958a27_pb2.TitlePage, _Mapping]] = ..., overview: _Optional[_Union[_Overview_186a1974c92f444f1bbc853569958a27_pb2.Overview, _Mapping]] = ..., pitch: _Optional[_Union[_Pitch_186a1974c92f444f1bbc853569958a27_pb2.Pitch, _Mapping]] = ..., argument: _Optional[_Union[_Argument_186a1974c92f444f1bbc853569958a27_pb2.Argument, _Mapping]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
