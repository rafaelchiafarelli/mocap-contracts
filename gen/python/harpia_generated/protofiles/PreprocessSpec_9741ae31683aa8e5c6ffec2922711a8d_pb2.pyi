from harpia_generated.protofiles import Crop_9741ae31683aa8e5c6ffec2922711a8d_pb2 as _Crop_9741ae31683aa8e5c6ffec2922711a8d_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreprocessSpec(_message.Message):
    __slots__ = ["ERROR_9741ae31683aa8e5c6ffec2922711a8d", "ID_9741ae31683aa8e5c6ffec2922711a8d", "ORIGINATOR", "STATUS_9741ae31683aa8e5c6ffec2922711a8d", "crop", "output_height", "output_width"]
    CROP_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ERROR_9741ae31683aa8e5c6ffec2922711a8d: str
    ID_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    ID_9741ae31683aa8e5c6ffec2922711a8d: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741AE31683AA8E5C6FFEC2922711A8D_FIELD_NUMBER: _ClassVar[int]
    STATUS_9741ae31683aa8e5c6ffec2922711a8d: str
    crop: _Crop_9741ae31683aa8e5c6ffec2922711a8d_pb2.Crop
    output_height: int
    output_width: int
    def __init__(self, ID_9741ae31683aa8e5c6ffec2922711a8d: _Optional[int] = ..., crop: _Optional[_Union[_Crop_9741ae31683aa8e5c6ffec2922711a8d_pb2.Crop, _Mapping]] = ..., output_width: _Optional[int] = ..., output_height: _Optional[int] = ..., STATUS_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ERROR_9741ae31683aa8e5c6ffec2922711a8d: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
