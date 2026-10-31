from harpia_generated.protofiles import PageSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _PageSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ElementStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ElementStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import PdfSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _PdfSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import ScriptStrings_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _ScriptStrings_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import HeaderSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _HeaderSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import AutoCompletionList_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _AutoCompletionList_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import LocationGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _LocationGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2
from harpia_generated.protofiles import TitlePages_e51d6d03132b4baa0ced72cde01af9d0_pb2 as _TitlePages_e51d6d03132b4baa0ced72cde01af9d0_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptSettings(_message.Message):
    __slots__ = ["ERROR_e51d6d03132b4baa0ced72cde01af9d0", "ID_e51d6d03132b4baa0ced72cde01af9d0", "ORIGINATOR", "STATUS_e51d6d03132b4baa0ced72cde01af9d0", "auto_completion", "elements", "headers", "locations", "page", "pdf", "spelling_words", "strings", "title_page"]
    AUTO_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ERROR_e51d6d03132b4baa0ced72cde01af9d0: str
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ID_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    ID_e51d6d03132b4baa0ced72cde01af9d0: int
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PDF_FIELD_NUMBER: _ClassVar[int]
    SPELLING_WORDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_E51D6D03132B4BAA0CED72CDE01AF9D0_FIELD_NUMBER: _ClassVar[int]
    STATUS_e51d6d03132b4baa0ced72cde01af9d0: str
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_PAGE_FIELD_NUMBER: _ClassVar[int]
    auto_completion: _containers.RepeatedCompositeFieldContainer[_AutoCompletionList_e51d6d03132b4baa0ced72cde01af9d0_pb2.AutoCompletionList]
    elements: _containers.RepeatedCompositeFieldContainer[_ElementStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2.ElementStyle]
    headers: _HeaderSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.HeaderSettings
    locations: _containers.RepeatedCompositeFieldContainer[_LocationGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2.LocationGroup]
    page: _PageSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.PageSettings
    pdf: _PdfSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.PdfSettings
    spelling_words: _containers.RepeatedScalarFieldContainer[str]
    strings: _ScriptStrings_e51d6d03132b4baa0ced72cde01af9d0_pb2.ScriptStrings
    title_page: _TitlePages_e51d6d03132b4baa0ced72cde01af9d0_pb2.TitlePages
    def __init__(self, ID_e51d6d03132b4baa0ced72cde01af9d0: _Optional[int] = ..., page: _Optional[_Union[_PageSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.PageSettings, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[_ElementStyle_e51d6d03132b4baa0ced72cde01af9d0_pb2.ElementStyle, _Mapping]]] = ..., pdf: _Optional[_Union[_PdfSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.PdfSettings, _Mapping]] = ..., strings: _Optional[_Union[_ScriptStrings_e51d6d03132b4baa0ced72cde01af9d0_pb2.ScriptStrings, _Mapping]] = ..., headers: _Optional[_Union[_HeaderSettings_e51d6d03132b4baa0ced72cde01af9d0_pb2.HeaderSettings, _Mapping]] = ..., auto_completion: _Optional[_Iterable[_Union[_AutoCompletionList_e51d6d03132b4baa0ced72cde01af9d0_pb2.AutoCompletionList, _Mapping]]] = ..., locations: _Optional[_Iterable[_Union[_LocationGroup_e51d6d03132b4baa0ced72cde01af9d0_pb2.LocationGroup, _Mapping]]] = ..., spelling_words: _Optional[_Iterable[str]] = ..., title_page: _Optional[_Union[_TitlePages_e51d6d03132b4baa0ced72cde01af9d0_pb2.TitlePages, _Mapping]] = ..., STATUS_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ERROR_e51d6d03132b4baa0ced72cde01af9d0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
