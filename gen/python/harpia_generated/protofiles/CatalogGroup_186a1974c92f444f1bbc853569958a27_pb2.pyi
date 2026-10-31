from harpia_generated.protofiles import Flag_186a1974c92f444f1bbc853569958a27_pb2 as _Flag_186a1974c92f444f1bbc853569958a27_pb2
from harpia_generated.protofiles import CatalogField_186a1974c92f444f1bbc853569958a27_pb2 as _CatalogField_186a1974c92f444f1bbc853569958a27_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogGroup(_message.Message):
    __slots__ = ["ERROR_186a1974c92f444f1bbc853569958a27", "ID_186a1974c92f444f1bbc853569958a27", "ORIGINATOR", "STATUS_186a1974c92f444f1bbc853569958a27", "department", "fields", "key", "label", "per_scene"]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ERROR_186a1974c92f444f1bbc853569958a27: str
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    ID_186a1974c92f444f1bbc853569958a27: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PER_SCENE_FIELD_NUMBER: _ClassVar[int]
    STATUS_186A1974C92F444F1BBC853569958A27_FIELD_NUMBER: _ClassVar[int]
    STATUS_186a1974c92f444f1bbc853569958a27: str
    department: str
    fields: _containers.RepeatedCompositeFieldContainer[_CatalogField_186a1974c92f444f1bbc853569958a27_pb2.CatalogField]
    key: str
    label: str
    per_scene: _Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag
    def __init__(self, ID_186a1974c92f444f1bbc853569958a27: _Optional[int] = ..., key: _Optional[str] = ..., label: _Optional[str] = ..., per_scene: _Optional[_Union[_Flag_186a1974c92f444f1bbc853569958a27_pb2.Flag, str]] = ..., department: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[_CatalogField_186a1974c92f444f1bbc853569958a27_pb2.CatalogField, _Mapping]]] = ..., STATUS_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ERROR_186a1974c92f444f1bbc853569958a27: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
