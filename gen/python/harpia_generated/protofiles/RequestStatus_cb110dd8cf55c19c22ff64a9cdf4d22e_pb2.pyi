from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
REQUEST_STATUS_DECLINED: RequestStatus
REQUEST_STATUS_DONE: RequestStatus
REQUEST_STATUS_OPEN: RequestStatus
REQUEST_STATUS_UNSET: RequestStatus

class RequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
