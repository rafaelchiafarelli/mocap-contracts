from harpia_generated.protofiles import Flag_7656bad163803b596999eb3843b4995c_pb2 as _Flag_7656bad163803b596999eb3843b4995c_pb2
from harpia_generated.protofiles import CatalogField_7656bad163803b596999eb3843b4995c_pb2 as _CatalogField_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogGroup(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "department", "fields", "key", "label", "per_scene"]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PER_SCENE_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    department: str
    fields: _containers.RepeatedCompositeFieldContainer[_CatalogField_7656bad163803b596999eb3843b4995c_pb2.CatalogField]
    key: str
    label: str
    per_scene: _Flag_7656bad163803b596999eb3843b4995c_pb2.Flag
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., key: _Optional[str] = ..., label: _Optional[str] = ..., per_scene: _Optional[_Union[_Flag_7656bad163803b596999eb3843b4995c_pb2.Flag, str]] = ..., department: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[_CatalogField_7656bad163803b596999eb3843b4995c_pb2.CatalogField, _Mapping]]] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
