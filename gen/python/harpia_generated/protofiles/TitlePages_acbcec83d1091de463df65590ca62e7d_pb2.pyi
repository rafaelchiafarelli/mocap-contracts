from harpia_generated.protofiles import TitlePageLayout_acbcec83d1091de463df65590ca62e7d_pb2 as _TitlePageLayout_acbcec83d1091de463df65590ca62e7d_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitlePages(_message.Message):
    __slots__ = ["ERROR_acbcec83d1091de463df65590ca62e7d", "ID_acbcec83d1091de463df65590ca62e7d", "ORIGINATOR", "STATUS_acbcec83d1091de463df65590ca62e7d", "fountain_title", "pages"]
    ERROR_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ERROR_acbcec83d1091de463df65590ca62e7d: str
    FOUNTAIN_TITLE_FIELD_NUMBER: _ClassVar[int]
    ID_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    ID_acbcec83d1091de463df65590ca62e7d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    STATUS_ACBCEC83D1091DE463DF65590CA62E7D_FIELD_NUMBER: _ClassVar[int]
    STATUS_acbcec83d1091de463df65590ca62e7d: str
    fountain_title: str
    pages: _containers.RepeatedCompositeFieldContainer[_TitlePageLayout_acbcec83d1091de463df65590ca62e7d_pb2.TitlePageLayout]
    def __init__(self, ID_acbcec83d1091de463df65590ca62e7d: _Optional[int] = ..., pages: _Optional[_Iterable[_Union[_TitlePageLayout_acbcec83d1091de463df65590ca62e7d_pb2.TitlePageLayout, _Mapping]]] = ..., fountain_title: _Optional[str] = ..., STATUS_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ERROR_acbcec83d1091de463df65590ca62e7d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
