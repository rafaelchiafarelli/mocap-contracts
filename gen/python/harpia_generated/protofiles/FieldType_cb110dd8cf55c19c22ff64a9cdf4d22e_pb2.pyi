from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
FIELD_TYPE_CHOICE: FieldType
FIELD_TYPE_FILE: FieldType
FIELD_TYPE_LINK: FieldType
FIELD_TYPE_LIST: FieldType
FIELD_TYPE_NUMBER: FieldType
FIELD_TYPE_TEXT: FieldType
FIELD_TYPE_UNSET: FieldType

class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
