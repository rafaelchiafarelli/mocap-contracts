from harpia_generated.protofiles import Crop_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2 as _Crop_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreprocessSpec(_message.Message):
    __slots__ = ["HARPIA_ERROR", "HARPIA_ID", "HARPIA_ORIGINATOR", "HARPIA_STATUS", "crop", "output_height", "output_width"]
    CROP_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ERROR: str
    HARPIA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ID: int
    HARPIA_ID_FIELD_NUMBER: _ClassVar[int]
    HARPIA_ORIGINATOR: str
    HARPIA_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    HARPIA_STATUS: str
    HARPIA_STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    crop: _Crop_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Crop
    output_height: int
    output_width: int
    def __init__(self, HARPIA_ID: _Optional[int] = ..., crop: _Optional[_Union[_Crop_cb110dd8cf55c19c22ff64a9cdf4d22e_pb2.Crop, _Mapping]] = ..., output_width: _Optional[int] = ..., output_height: _Optional[int] = ..., HARPIA_STATUS: _Optional[str] = ..., HARPIA_ERROR: _Optional[str] = ..., HARPIA_ORIGINATOR: _Optional[str] = ...) -> None: ...
