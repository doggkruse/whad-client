# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: whad/protocol/generic.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bwhad/protocol/generic.proto\x12\x07generic\"0\n\tCmdResult\x12#\n\x06result\x18\x01 \x01(\x0e\x32\x13.generic.ResultCode\"\x19\n\x08Progress\x12\r\n\x05value\x18\x01 \x01(\r\"\'\n\x08\x44\x65\x62ugMsg\x12\r\n\x05level\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x1a\n\nVerboseMsg\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\xd4\x01\n\x07Message\x12%\n\x06result\x18\x01 \x01(\x0e\x32\x13.generic.ResultCodeH\x00\x12(\n\ncmd_result\x18\x02 \x01(\x0b\x32\x12.generic.CmdResultH\x00\x12%\n\x08progress\x18\x03 \x01(\x0b\x32\x11.generic.ProgressH\x00\x12\"\n\x05\x64\x65\x62ug\x18\x04 \x01(\x0b\x32\x11.generic.DebugMsgH\x00\x12&\n\x07verbose\x18\x05 \x01(\x0b\x32\x13.generic.VerboseMsgH\x00\x42\x05\n\x03msg*}\n\nResultCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x13\n\x0fPARAMETER_ERROR\x10\x02\x12\x10\n\x0c\x44ISCONNECTED\x10\x03\x12\x0e\n\nWRONG_MODE\x10\x04\x12\x16\n\x12UNSUPPORTED_DOMAIN\x10\x05\x12\x08\n\x04\x42USY\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'whad.protocol.generic_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESULTCODE._serialized_start=401
  _RESULTCODE._serialized_end=526
  _CMDRESULT._serialized_start=40
  _CMDRESULT._serialized_end=88
  _PROGRESS._serialized_start=90
  _PROGRESS._serialized_end=115
  _DEBUGMSG._serialized_start=117
  _DEBUGMSG._serialized_end=156
  _VERBOSEMSG._serialized_start=158
  _VERBOSEMSG._serialized_end=184
  _MESSAGE._serialized_start=187
  _MESSAGE._serialized_end=399
# @@protoc_insertion_point(module_scope)
