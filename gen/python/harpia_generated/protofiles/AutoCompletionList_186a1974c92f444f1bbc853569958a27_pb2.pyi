from harpia_generated.protofiles import ScriptElement_186a1974c92f444f1bbc853569958a27_pb2 as _ScriptElement_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutoCompletionList(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "element", "enabled", "items"]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    element: _ScriptElement_186a1974c92f444f1bbc853569958a27_pb2.ScriptElement
    enabled: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., element: _Optional[_Union[_ScriptElement_186a1974c92f444f1bbc853569958a27_pb2.ScriptElement, str]] = ..., enabled: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., items: _Optional[_Iterable[str]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
