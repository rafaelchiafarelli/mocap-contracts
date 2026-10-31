from harpia_generated.protofiles import TitlePageLayout_7656bad163803b596999eb3843b4995c_pb2 as _TitlePageLayout_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitlePages(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "fountain_title", "pages"]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    FOUNTAIN_TITLE_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    fountain_title: str
    pages: _containers.RepeatedCompositeFieldContainer[_TitlePageLayout_7656bad163803b596999eb3843b4995c_pb2.TitlePageLayout]
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., pages: _Optional[_Iterable[_Union[_TitlePageLayout_7656bad163803b596999eb3843b4995c_pb2.TitlePageLayout, _Mapping]]] = ..., fountain_title: _Optional[str] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
