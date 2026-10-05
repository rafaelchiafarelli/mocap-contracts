from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

CONTROL_STATUS_APPLIED: ControlStatus
CONTROL_STATUS_CLAMPED: ControlStatus
CONTROL_STATUS_FAILED: ControlStatus
CONTROL_STATUS_READ_ONLY: ControlStatus
CONTROL_STATUS_UNSET: ControlStatus
CONTROL_STATUS_UNSUPPORTED: ControlStatus
DESCRIPTOR: _descriptor.FileDescriptor

class ControlStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
