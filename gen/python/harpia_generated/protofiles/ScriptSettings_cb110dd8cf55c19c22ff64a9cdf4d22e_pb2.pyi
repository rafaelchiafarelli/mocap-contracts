from harpia_generated.protofiles import PageSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _PageSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ElementStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ElementStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import PdfSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _PdfSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import ScriptStrings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _ScriptStrings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import HeaderSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _HeaderSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import AutoCompletionList_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _AutoCompletionList_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import LocationGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _LocationGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from harpia_generated.protofiles import TitlePages_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _TitlePages_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptSettings(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "auto_completion", "elements", "headers", "locations", "page", "pdf", "spelling_words", "strings", "title_page"]
    AUTO_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PDF_FIELD_NUMBER: _ClassVar[int]
    SPELLING_WORDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_PAGE_FIELD_NUMBER: _ClassVar[int]
    auto_completion: _containers.RepeatedCompositeFieldContainer[_AutoCompletionList_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AutoCompletionList]
    elements: _containers.RepeatedCompositeFieldContainer[_ElementStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ElementStyle]
    headers: _HeaderSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.HeaderSettings
    locations: _containers.RepeatedCompositeFieldContainer[_LocationGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.LocationGroup]
    page: _PageSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PageSettings
    pdf: _PdfSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PdfSettings
    spelling_words: _containers.RepeatedScalarFieldContainer[str]
    strings: _ScriptStrings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ScriptStrings
    title_page: _TitlePages_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitlePages
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., page: _Optional[_Union[_PageSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PageSettings, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[_ElementStyle_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ElementStyle, _Mapping]]] = ..., pdf: _Optional[_Union[_PdfSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.PdfSettings, _Mapping]] = ..., strings: _Optional[_Union[_ScriptStrings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.ScriptStrings, _Mapping]] = ..., headers: _Optional[_Union[_HeaderSettings_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.HeaderSettings, _Mapping]] = ..., auto_completion: _Optional[_Iterable[_Union[_AutoCompletionList_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.AutoCompletionList, _Mapping]]] = ..., locations: _Optional[_Iterable[_Union[_LocationGroup_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.LocationGroup, _Mapping]]] = ..., spelling_words: _Optional[_Iterable[str]] = ..., title_page: _Optional[_Union[_TitlePages_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.TitlePages, _Mapping]] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
