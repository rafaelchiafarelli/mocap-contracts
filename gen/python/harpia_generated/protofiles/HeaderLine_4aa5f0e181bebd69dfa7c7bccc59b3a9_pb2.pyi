from harpia_generated.protofiles import TextAlign_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _TextAlign_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from harpia_generated.protofiles import Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2 as _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderLine(_message.Message):
    __slots__ = ["ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ID_4aa5f0e181bebd69dfa7c7bccc59b3a9", "ORIGINATOR", "STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9", "align", "bold", "italic", "line", "text", "underlined", "x_offset_chars"]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ERROR_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    ID_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: int
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR: str
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_4AA5F0E181BEBD69DFA7C7BCCC59B3A9_FIELD_NUMBER: _ClassVar[int]
    STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: str
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UNDERLINED_FIELD_NUMBER: _ClassVar[int]
    X_OFFSET_CHARS_FIELD_NUMBER: _ClassVar[int]
    align: _TextAlign_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.TextAlign
    bold: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    italic: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    line: int
    text: str
    underlined: _Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag
    x_offset_chars: int
    def __init__(self, ID_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[int] = ..., line: _Optional[int] = ..., x_offset_chars: _Optional[int] = ..., align: _Optional[_Union[_TextAlign_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.TextAlign, str]] = ..., bold: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., italic: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., underlined: _Optional[_Union[_Flag_4aa5f0e181bebd69dfa7c7bccc59b3a9_pb2.Flag, str]] = ..., text: _Optional[str] = ..., STATUS_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ERROR_4aa5f0e181bebd69dfa7c7bccc59b3a9: _Optional[str] = ..., ORIGINATOR: _Optional[str] = ...) -> None: ...
