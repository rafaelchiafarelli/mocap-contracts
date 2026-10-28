from harpia_generated.protofiles import Flag_ae090d6fa4827e92540c3f916b30649f_pb2 as _Flag_ae090d6fa4827e92540c3f916b30649f_pb2
from harpia_generated.protofiles import CatalogField_ae090d6fa4827e92540c3f916b30649f_pb2 as _CatalogField_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogGroup(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "department", "fields", "key", "label", "per_scene"]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PER_SCENE_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    department: str
    fields: _containers.RepeatedCompositeFieldContainer[_CatalogField_ae090d6fa4827e92540c3f916b30649f_pb2.CatalogField]
    key: str
    label: str
    per_scene: _Flag_ae090d6fa4827e92540c3f916b30649f_pb2.Flag
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., key: _Optional[str] = ..., label: _Optional[str] = ..., per_scene: _Optional[_Union[_Flag_ae090d6fa4827e92540c3f916b30649f_pb2.Flag, str]] = ..., department: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[_CatalogField_ae090d6fa4827e92540c3f916b30649f_pb2.CatalogField, _Mapping]]] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
