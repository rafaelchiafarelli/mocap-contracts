from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
REVIEW_OUTCOME_APPROVED: ReviewOutcome
REVIEW_OUTCOME_EDITED: ReviewOutcome
REVIEW_OUTCOME_REJECTED: ReviewOutcome
REVIEW_OUTCOME_UNSET: ReviewOutcome

class ReviewOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
