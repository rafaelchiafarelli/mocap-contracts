from harpia_generated.protofiles import errorCode_pb2 as _errorCode_pb2
from harpia_generated.protofiles import heartBeat_pb2 as _heartBeat_pb2
from harpia_generated.protofiles import TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeType_HeartBeat(_message.Message):
    __slots__ = ["hb"]
    HB_FIELD_NUMBER: _ClassVar[int]
    hb: _heartBeat_pb2.heartBeat
    def __init__(self, hb: _Optional[_Union[_heartBeat_pb2.heartBeat, _Mapping]] = ...) -> None: ...

class TakeType_ID(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class TakeType_Message(_message.Message):
    __slots__ = ["msg"]
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: _TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2.TakeType
    def __init__(self, msg: _Optional[_Union[_TakeType_9741ae31683aa8e5c6ffec2922711a8d_pb2.TakeType, str]] = ...) -> None: ...

class TakeType_Stream(_message.Message):
    __slots__ = ["id", "limit", "name", "offset"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    id: int
    limit: int
    name: str
    offset: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...
