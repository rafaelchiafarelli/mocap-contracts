from harpia_generated.protofiles import Crop_7656bad163803b596999eb3843b4995c_pb2 as _Crop_7656bad163803b596999eb3843b4995c_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreprocessSpec(_message.Message):
    __slots__ = ["ERROR_7656bad163803b596999eb3843b4995c", "ID_7656bad163803b596999eb3843b4995c", "ORIGINATOR", "STATUS_7656bad163803b596999eb3843b4995c", "crop", "output_height", "output_width"]
    CROP_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ERROR_7656bad163803b596999eb3843b4995c: str
    ID_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    ID_7656bad163803b596999eb3843b4995c: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656BAD163803B596999EB3843B4995C_FIELD_NUMBER: _ClassVar[int]
    STATUS_7656bad163803b596999eb3843b4995c: str
    crop: _Crop_7656bad163803b596999eb3843b4995c_pb2.Crop
    output_height: int
    output_width: int
    def __init__(self, ID_7656bad163803b596999eb3843b4995c: _Optional[int] = ..., crop: _Optional[_Union[_Crop_7656bad163803b596999eb3843b4995c_pb2.Crop, _Mapping]] = ..., output_width: _Optional[int] = ..., output_height: _Optional[int] = ..., STATUS_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ERROR_7656bad163803b596999eb3843b4995c: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
