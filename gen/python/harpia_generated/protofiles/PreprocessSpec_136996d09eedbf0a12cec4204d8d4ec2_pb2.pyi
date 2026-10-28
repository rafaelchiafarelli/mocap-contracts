from harpia_generated.protofiles import Crop_136996d09eedbf0a12cec4204d8d4ec2_pb2 as _Crop_136996d09eedbf0a12cec4204d8d4ec2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreprocessSpec(_message.Message):
    __slots__ = ["ERROR_136996d09eedbf0a12cec4204d8d4ec2", "ID_136996d09eedbf0a12cec4204d8d4ec2", "ORIGINATOR", "STATUS_136996d09eedbf0a12cec4204d8d4ec2", "crop", "output_height", "output_width"]
    CROP_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ERROR_136996d09eedbf0a12cec4204d8d4ec2: str
    ID_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    ID_136996d09eedbf0a12cec4204d8d4ec2: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996D09EEDBF0A12CEC4204D8D4EC2_FIELD_NUMBER: _ClassVar[int]
    STATUS_136996d09eedbf0a12cec4204d8d4ec2: str
    crop: _Crop_136996d09eedbf0a12cec4204d8d4ec2_pb2.Crop
    output_height: int
    output_width: int
    def __init__(self, ID_136996d09eedbf0a12cec4204d8d4ec2: _Optional[int] = ..., crop: _Optional[_Union[_Crop_136996d09eedbf0a12cec4204d8d4ec2_pb2.Crop, _Mapping]] = ..., output_width: _Optional[int] = ..., output_height: _Optional[int] = ..., STATUS_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ERROR_136996d09eedbf0a12cec4204d8d4ec2: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
