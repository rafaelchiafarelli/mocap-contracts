from harpia_generated.protofiles import Crop_c4b8ea5558d6147d937c128fc2703ba0_pb2 as _Crop_c4b8ea5558d6147d937c128fc2703ba0_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreprocessSpec(_message.Message):
    __slots__ = ["ERROR_c4b8ea5558d6147d937c128fc2703ba0", "ID_c4b8ea5558d6147d937c128fc2703ba0", "ORIGINATOR", "STATUS_c4b8ea5558d6147d937c128fc2703ba0", "crop", "output_height", "output_width"]
    CROP_FIELD_NUMBER: _ClassVar[int]
    ERROR_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ERROR_c4b8ea5558d6147d937c128fc2703ba0: str
    ID_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    ID_c4b8ea5558d6147d937c128fc2703ba0: int
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_C4B8EA5558D6147D937C128FC2703BA0_FIELD_NUMBER: _ClassVar[int]
    STATUS_c4b8ea5558d6147d937c128fc2703ba0: str
    crop: _Crop_c4b8ea5558d6147d937c128fc2703ba0_pb2.Crop
    output_height: int
    output_width: int
    def __init__(self, ID_c4b8ea5558d6147d937c128fc2703ba0: _Optional[int] = ..., crop: _Optional[_Union[_Crop_c4b8ea5558d6147d937c128fc2703ba0_pb2.Crop, _Mapping]] = ..., output_width: _Optional[int] = ..., output_height: _Optional[int] = ..., STATUS_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ERROR_c4b8ea5558d6147d937c128fc2703ba0: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
