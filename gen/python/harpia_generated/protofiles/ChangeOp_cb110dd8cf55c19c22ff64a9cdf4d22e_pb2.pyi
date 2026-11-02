from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

CHANGE_OP_CREATE: ChangeOp
CHANGE_OP_DELETE: ChangeOp
CHANGE_OP_UNSET: ChangeOp
CHANGE_OP_UPDATE: ChangeOp
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
