from harpia_generated.protofiles import Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2
from harpia_generated.protofiles import CatalogField_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _CatalogField_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogGroup(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "department", "fields", "key", "label", "per_scene"]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    PER_SCENE_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    department: str
    fields: _containers.RepeatedCompositeFieldContainer[_CatalogField_136996d09eedbf0a12cec4204d8d4ec2_pb2.CatalogField]
    key: str
    label: str
    per_scene: _Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., key: _Optional[str] = ..., label: _Optional[str] = ..., per_scene: _Optional[_Union[_Flag_136996d09eedbf0a12cec4204d8d4ec2_pb2.Flag, str]] = ..., department: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[_CatalogField_136996d09eedbf0a12cec4204d8d4ec2_pb2.CatalogField, _Mapping]]] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
