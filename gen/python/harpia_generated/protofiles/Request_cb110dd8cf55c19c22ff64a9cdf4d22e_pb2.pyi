from harpia_generated.protofiles import RequestStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _RequestStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e", "ID_cb110dd8cf55c19c22ff64a9cdf4d22e", "ORIGINATOR", "STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e", "answer", "answered_by", "id", "items", "scenes", "source", "status", "time", "to", "what"]
    ANSWERED_BY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ERROR_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_cb110dd8cf55c19c22ff64a9cdf4d22e: int
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    SCENES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CB110DD8CF55C19C22FF64A9CDF4D22E_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: str
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    WHAT_FIELD_NUMBER: _ClassVar[int]
    answer: str
    answered_by: str
    id: str
    items: _containers.RepeatedScalarFieldContainer[str]
    scenes: _containers.RepeatedScalarFieldContainer[str]
    source: str
    status: _RequestStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.RequestStatus
    time: str
    to: str
    what: str
    def __init__(self, ID_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[int] = ..., id: _Optional[str] = ..., to: _Optional[str] = ..., items: _Optional[_Iterable[str]] = ..., scenes: _Optional[_Iterable[str]] = ..., what: _Optional[str] = ..., source: _Optional[str] = ..., time: _Optional[str] = ..., status: _Optional[_Union[_RequestStatus_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.RequestStatus, str]] = ..., answer: _Optional[str] = ..., answered_by: _Optional[str] = ..., STATUS_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ERROR_cb110dd8cf55c19c22ff64a9cdf4d22e: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ..., **kwargs) -> None: ...
