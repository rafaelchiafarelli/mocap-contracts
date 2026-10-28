from harpia_generated.protofiles import FieldType_ae090d6fa4827e92540c3f916b30649f_pb2 as _FieldType_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogField(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "key", "label", "link_kind", "options", "type", "unit"]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LINK_KIND_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    link_kind: str
    options: _containers.RepeatedScalarFieldContainer[str]
    type: _FieldType_ae090d6fa4827e92540c3f916b30649f_pb2.FieldType
    unit: str
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., key: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[_Union[_FieldType_ae090d6fa4827e92540c3f916b30649f_pb2.FieldType, str]] = ..., options: _Optional[_Iterable[str]] = ..., unit: _Optional[str] = ..., link_kind: _Optional[str] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
