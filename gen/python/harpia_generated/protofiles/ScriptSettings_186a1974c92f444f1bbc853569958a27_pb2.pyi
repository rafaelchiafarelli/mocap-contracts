from harpia_generated.protofiles import PageSettings_186a1974c92f444f1bbc853569958a27_pb2 as _PageSettings_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import ElementStyle_186a1974c92f444f1bbc853569958a27_pb2 as _ElementStyle_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import PdfSettings_186a1974c92f444f1bbc853569958a27_pb2 as _PdfSettings_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import ScriptStrings_186a1974c92f444f1bbc853569958a27_pb2 as _ScriptStrings_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import HeaderSettings_186a1974c92f444f1bbc853569958a27_pb2 as _HeaderSettings_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import AutoCompletionList_186a1974c92f444f1bbc853569958a27_pb2 as _AutoCompletionList_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import LocationGroup_186a1974c92f444f1bbc853569958a27_pb2 as _LocationGroup_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import TitlePages_186a1974c92f444f1bbc853569958a27_pb2 as _TitlePages_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptSettings(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "auto_completion", "elements", "headers", "locations", "page", "pdf", "spelling_words", "strings", "title_page"]
    AUTO_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PDF_FIELD_NUMBER: _ClassVar[int]
    SPELLING_WORDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_PAGE_FIELD_NUMBER: _ClassVar[int]
    auto_completion: _containers.RepeatedCompositeFieldContainer[_AutoCompletionList_186a1974c92f444f1bbc853569958a27_pb2.AutoCompletionList]
    elements: _containers.RepeatedCompositeFieldContainer[_ElementStyle_186a1974c92f444f1bbc853569958a27_pb2.ElementStyle]
    headers: _HeaderSettings_186a1974c92f444f1bbc853569958a27_pb2.HeaderSettings
    locations: _containers.RepeatedCompositeFieldContainer[_LocationGroup_186a1974c92f444f1bbc853569958a27_pb2.LocationGroup]
    page: _PageSettings_186a1974c92f444f1bbc853569958a27_pb2.PageSettings
    pdf: _PdfSettings_186a1974c92f444f1bbc853569958a27_pb2.PdfSettings
    spelling_words: _containers.RepeatedScalarFieldContainer[str]
    strings: _ScriptStrings_186a1974c92f444f1bbc853569958a27_pb2.ScriptStrings
    title_page: _TitlePages_186a1974c92f444f1bbc853569958a27_pb2.TitlePages
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., page: _Optional[_Union[_PageSettings_186a1974c92f444f1bbc853569958a27_pb2.PageSettings, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[_ElementStyle_186a1974c92f444f1bbc853569958a27_pb2.ElementStyle, _Mapping]]] = ..., pdf: _Optional[_Union[_PdfSettings_186a1974c92f444f1bbc853569958a27_pb2.PdfSettings, _Mapping]] = ..., strings: _Optional[_Union[_ScriptStrings_186a1974c92f444f1bbc853569958a27_pb2.ScriptStrings, _Mapping]] = ..., headers: _Optional[_Union[_HeaderSettings_186a1974c92f444f1bbc853569958a27_pb2.HeaderSettings, _Mapping]] = ..., auto_completion: _Optional[_Iterable[_Union[_AutoCompletionList_186a1974c92f444f1bbc853569958a27_pb2.AutoCompletionList, _Mapping]]] = ..., locations: _Optional[_Iterable[_Union[_LocationGroup_186a1974c92f444f1bbc853569958a27_pb2.LocationGroup, _Mapping]]] = ..., spelling_words: _Optional[_Iterable[str]] = ..., title_page: _Optional[_Union[_TitlePages_186a1974c92f444f1bbc853569958a27_pb2.TitlePages, _Mapping]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
