from harpia_generated.protofiles import Crop_ae090d6fa4827e92540c3f916b30649f_pb2 as _Crop_ae090d6fa4827e92540c3f916b30649f_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreprocessSpec(_message.Message):
    __slots__ = ["ERROR_ae090d6fa4827e92540c3f916b30649f", "ID_ae090d6fa4827e92540c3f916b30649f", "ORIGINATOR", "STATUS_ae090d6fa4827e92540c3f916b30649f", "crop", "output_height", "output_width"]
    CROP_FIELD_NUMBER: _ClassVar[int]
    ERROR_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ERROR_ae090d6fa4827e92540c3f916b30649f: str
    ID_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    ID_ae090d6fa4827e92540c3f916b30649f: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_AE090D6FA4827E92540C3F916B30649F_FIELD_NUMBER: _ClassVar[int]
    STATUS_ae090d6fa4827e92540c3f916b30649f: str
    crop: _Crop_ae090d6fa4827e92540c3f916b30649f_pb2.Crop
    output_height: int
    output_width: int
    def __init__(self, ID_ae090d6fa4827e92540c3f916b30649f: _Optional[int] = ..., crop: _Optional[_Union[_Crop_ae090d6fa4827e92540c3f916b30649f_pb2.Crop, _Mapping]] = ..., output_width: _Optional[int] = ..., output_height: _Optional[int] = ..., STATUS_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ERROR_ae090d6fa4827e92540c3f916b30649f: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
