from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
VALUE_STATE_CREATOR_APPROVED: ValueState
VALUE_STATE_PROPOSAL: ValueState
VALUE_STATE_SCRIPT_STATED: ValueState
VALUE_STATE_TBD: ValueState
VALUE_STATE_UNSET: ValueState

class ValueState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
