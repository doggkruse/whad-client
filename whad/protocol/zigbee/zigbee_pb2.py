# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/zigbee/zigbee.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol/zigbee/zigbee.proto',
  package='zigbee',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cprotocol/zigbee/zigbee.proto\x12\x06zigbee\"$\n\x11SetNodeAddressCmd\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"\x1b\n\x08SniffCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"\x19\n\x06JamCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"4\n\x07SendCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0b\n\x03pdu\x18\x02 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x03 \x01(\r\"\x0e\n\x0c\x45ndDeviceCmd\"\x0b\n\tRouterCmd\"\x10\n\x0e\x43oordinatorCmd\"\n\n\x08StartCmd\"\t\n\x07StopCmd\"9\n\x11ManInTheMiddleCmd\x12$\n\x04role\x18\x01 \x01(\x0e\x32\x16.zigbee.ZigbeeMitmRole\"\x1b\n\x06Jammed\x12\x11\n\ttimestamp\x18\x01 \x01(\r\"\xa9\x01\n\x0eRawPduReceived\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0c\x66\x63s_validity\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x0b\n\x03pdu\x18\x05 \x01(\x0c\x12\x0b\n\x03\x66\x63s\x18\x06 \x01(\rB\x07\n\x05_rssiB\x0c\n\n_timestampB\x0f\n\r_fcs_validity\"\x99\x01\n\x0bPduReceived\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0c\x66\x63s_validity\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x0b\n\x03pdu\x18\x05 \x01(\x0c\x42\x07\n\x05_rssiB\x0c\n\n_timestampB\x0f\n\r_fcs_validity\"\x87\x04\n\x07Message\x12\x32\n\rset_node_addr\x18\x01 \x01(\x0b\x32\x19.zigbee.SetNodeAddressCmdH\x00\x12!\n\x05sniff\x18\x02 \x01(\x0b\x32\x10.zigbee.SniffCmdH\x00\x12\x1d\n\x03jam\x18\x03 \x01(\x0b\x32\x0e.zigbee.JamCmdH\x00\x12\x1f\n\x04send\x18\x04 \x01(\x0b\x32\x0f.zigbee.SendCmdH\x00\x12*\n\nend_device\x18\x05 \x01(\x0b\x32\x14.zigbee.EndDeviceCmdH\x00\x12#\n\x06router\x18\x06 \x01(\x0b\x32\x11.zigbee.RouterCmdH\x00\x12-\n\x0b\x63oordinator\x18\x07 \x01(\x0b\x32\x16.zigbee.CoordinatorCmdH\x00\x12!\n\x05start\x18\x08 \x01(\x0b\x32\x10.zigbee.StartCmdH\x00\x12\x1f\n\x04stop\x18\t \x01(\x0b\x32\x0f.zigbee.StopCmdH\x00\x12)\n\x04mitm\x18\n \x01(\x0b\x32\x19.zigbee.ManInTheMiddleCmdH\x00\x12 \n\x06jammed\x18\x0b \x01(\x0b\x32\x0e.zigbee.JammedH\x00\x12)\n\x07raw_pdu\x18\x0c \x01(\x0b\x32\x16.zigbee.RawPduReceivedH\x00\x12\"\n\x03pdu\x18\r \x01(\x0b\x32\x13.zigbee.PduReceivedH\x00\x42\x05\n\x03msg*\xa2\x01\n\rZigbeeCommand\x12\x12\n\x0eSetNodeAddress\x10\x00\x12\t\n\x05Sniff\x10\x01\x12\x07\n\x03Jam\x10\x02\x12\x08\n\x04Send\x10\x03\x12\x11\n\rEndDeviceMode\x10\x04\x12\x13\n\x0f\x43oordinatorMode\x10\x05\x12\x0e\n\nRouterMode\x10\x06\x12\t\n\x05Start\x10\x07\x12\x08\n\x04Stop\x10\x08\x12\x12\n\x0eManInTheMiddle\x10\t*4\n\x0eZigbeeMitmRole\x12\x13\n\x0fREACTIVE_JAMMER\x10\x00\x12\r\n\tCORRECTOR\x10\x01\x62\x06proto3'
)

_ZIGBEECOMMAND = _descriptor.EnumDescriptor(
  name='ZigbeeCommand',
  full_name='zigbee.ZigbeeCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SetNodeAddress', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Sniff', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Jam', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Send', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EndDeviceMode', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CoordinatorMode', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RouterMode', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Start', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Stop', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ManInTheMiddle', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1197,
  serialized_end=1359,
)
_sym_db.RegisterEnumDescriptor(_ZIGBEECOMMAND)

ZigbeeCommand = enum_type_wrapper.EnumTypeWrapper(_ZIGBEECOMMAND)
_ZIGBEEMITMROLE = _descriptor.EnumDescriptor(
  name='ZigbeeMitmRole',
  full_name='zigbee.ZigbeeMitmRole',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REACTIVE_JAMMER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CORRECTOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1361,
  serialized_end=1413,
)
_sym_db.RegisterEnumDescriptor(_ZIGBEEMITMROLE)

ZigbeeMitmRole = enum_type_wrapper.EnumTypeWrapper(_ZIGBEEMITMROLE)
SetNodeAddress = 0
Sniff = 1
Jam = 2
Send = 3
EndDeviceMode = 4
CoordinatorMode = 5
RouterMode = 6
Start = 7
Stop = 8
ManInTheMiddle = 9
REACTIVE_JAMMER = 0
CORRECTOR = 1



_SETNODEADDRESSCMD = _descriptor.Descriptor(
  name='SetNodeAddressCmd',
  full_name='zigbee.SetNodeAddressCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='zigbee.SetNodeAddressCmd.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=76,
)


_SNIFFCMD = _descriptor.Descriptor(
  name='SniffCmd',
  full_name='zigbee.SniffCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='zigbee.SniffCmd.channel', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=105,
)


_JAMCMD = _descriptor.Descriptor(
  name='JamCmd',
  full_name='zigbee.JamCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='zigbee.JamCmd.channel', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=132,
)


_SENDCMD = _descriptor.Descriptor(
  name='SendCmd',
  full_name='zigbee.SendCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='zigbee.SendCmd.channel', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pdu', full_name='zigbee.SendCmd.pdu', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='crc', full_name='zigbee.SendCmd.crc', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=186,
)


_ENDDEVICECMD = _descriptor.Descriptor(
  name='EndDeviceCmd',
  full_name='zigbee.EndDeviceCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=202,
)


_ROUTERCMD = _descriptor.Descriptor(
  name='RouterCmd',
  full_name='zigbee.RouterCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=215,
)


_COORDINATORCMD = _descriptor.Descriptor(
  name='CoordinatorCmd',
  full_name='zigbee.CoordinatorCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=233,
)


_STARTCMD = _descriptor.Descriptor(
  name='StartCmd',
  full_name='zigbee.StartCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=245,
)


_STOPCMD = _descriptor.Descriptor(
  name='StopCmd',
  full_name='zigbee.StopCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=256,
)


_MANINTHEMIDDLECMD = _descriptor.Descriptor(
  name='ManInTheMiddleCmd',
  full_name='zigbee.ManInTheMiddleCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='zigbee.ManInTheMiddleCmd.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=315,
)


_JAMMED = _descriptor.Descriptor(
  name='Jammed',
  full_name='zigbee.Jammed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='zigbee.Jammed.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=344,
)


_RAWPDURECEIVED = _descriptor.Descriptor(
  name='RawPduReceived',
  full_name='zigbee.RawPduReceived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='zigbee.RawPduReceived.channel', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='zigbee.RawPduReceived.rssi', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='zigbee.RawPduReceived.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fcs_validity', full_name='zigbee.RawPduReceived.fcs_validity', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pdu', full_name='zigbee.RawPduReceived.pdu', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fcs', full_name='zigbee.RawPduReceived.fcs', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_rssi', full_name='zigbee.RawPduReceived._rssi',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_timestamp', full_name='zigbee.RawPduReceived._timestamp',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_fcs_validity', full_name='zigbee.RawPduReceived._fcs_validity',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=347,
  serialized_end=516,
)


_PDURECEIVED = _descriptor.Descriptor(
  name='PduReceived',
  full_name='zigbee.PduReceived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='zigbee.PduReceived.channel', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='zigbee.PduReceived.rssi', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='zigbee.PduReceived.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fcs_validity', full_name='zigbee.PduReceived.fcs_validity', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pdu', full_name='zigbee.PduReceived.pdu', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_rssi', full_name='zigbee.PduReceived._rssi',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_timestamp', full_name='zigbee.PduReceived._timestamp',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_fcs_validity', full_name='zigbee.PduReceived._fcs_validity',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=519,
  serialized_end=672,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='zigbee.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='set_node_addr', full_name='zigbee.Message.set_node_addr', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sniff', full_name='zigbee.Message.sniff', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jam', full_name='zigbee.Message.jam', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send', full_name='zigbee.Message.send', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_device', full_name='zigbee.Message.end_device', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='router', full_name='zigbee.Message.router', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coordinator', full_name='zigbee.Message.coordinator', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='zigbee.Message.start', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop', full_name='zigbee.Message.stop', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mitm', full_name='zigbee.Message.mitm', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jammed', full_name='zigbee.Message.jammed', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='raw_pdu', full_name='zigbee.Message.raw_pdu', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pdu', full_name='zigbee.Message.pdu', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='zigbee.Message.msg',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=675,
  serialized_end=1194,
)

_MANINTHEMIDDLECMD.fields_by_name['role'].enum_type = _ZIGBEEMITMROLE
_RAWPDURECEIVED.oneofs_by_name['_rssi'].fields.append(
  _RAWPDURECEIVED.fields_by_name['rssi'])
_RAWPDURECEIVED.fields_by_name['rssi'].containing_oneof = _RAWPDURECEIVED.oneofs_by_name['_rssi']
_RAWPDURECEIVED.oneofs_by_name['_timestamp'].fields.append(
  _RAWPDURECEIVED.fields_by_name['timestamp'])
_RAWPDURECEIVED.fields_by_name['timestamp'].containing_oneof = _RAWPDURECEIVED.oneofs_by_name['_timestamp']
_RAWPDURECEIVED.oneofs_by_name['_fcs_validity'].fields.append(
  _RAWPDURECEIVED.fields_by_name['fcs_validity'])
_RAWPDURECEIVED.fields_by_name['fcs_validity'].containing_oneof = _RAWPDURECEIVED.oneofs_by_name['_fcs_validity']
_PDURECEIVED.oneofs_by_name['_rssi'].fields.append(
  _PDURECEIVED.fields_by_name['rssi'])
_PDURECEIVED.fields_by_name['rssi'].containing_oneof = _PDURECEIVED.oneofs_by_name['_rssi']
_PDURECEIVED.oneofs_by_name['_timestamp'].fields.append(
  _PDURECEIVED.fields_by_name['timestamp'])
_PDURECEIVED.fields_by_name['timestamp'].containing_oneof = _PDURECEIVED.oneofs_by_name['_timestamp']
_PDURECEIVED.oneofs_by_name['_fcs_validity'].fields.append(
  _PDURECEIVED.fields_by_name['fcs_validity'])
_PDURECEIVED.fields_by_name['fcs_validity'].containing_oneof = _PDURECEIVED.oneofs_by_name['_fcs_validity']
_MESSAGE.fields_by_name['set_node_addr'].message_type = _SETNODEADDRESSCMD
_MESSAGE.fields_by_name['sniff'].message_type = _SNIFFCMD
_MESSAGE.fields_by_name['jam'].message_type = _JAMCMD
_MESSAGE.fields_by_name['send'].message_type = _SENDCMD
_MESSAGE.fields_by_name['end_device'].message_type = _ENDDEVICECMD
_MESSAGE.fields_by_name['router'].message_type = _ROUTERCMD
_MESSAGE.fields_by_name['coordinator'].message_type = _COORDINATORCMD
_MESSAGE.fields_by_name['start'].message_type = _STARTCMD
_MESSAGE.fields_by_name['stop'].message_type = _STOPCMD
_MESSAGE.fields_by_name['mitm'].message_type = _MANINTHEMIDDLECMD
_MESSAGE.fields_by_name['jammed'].message_type = _JAMMED
_MESSAGE.fields_by_name['raw_pdu'].message_type = _RAWPDURECEIVED
_MESSAGE.fields_by_name['pdu'].message_type = _PDURECEIVED
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['set_node_addr'])
_MESSAGE.fields_by_name['set_node_addr'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['sniff'])
_MESSAGE.fields_by_name['sniff'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['jam'])
_MESSAGE.fields_by_name['jam'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['send'])
_MESSAGE.fields_by_name['send'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['end_device'])
_MESSAGE.fields_by_name['end_device'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['router'])
_MESSAGE.fields_by_name['router'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['coordinator'])
_MESSAGE.fields_by_name['coordinator'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['start'])
_MESSAGE.fields_by_name['start'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['stop'])
_MESSAGE.fields_by_name['stop'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['mitm'])
_MESSAGE.fields_by_name['mitm'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['jammed'])
_MESSAGE.fields_by_name['jammed'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['raw_pdu'])
_MESSAGE.fields_by_name['raw_pdu'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['pdu'])
_MESSAGE.fields_by_name['pdu'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['SetNodeAddressCmd'] = _SETNODEADDRESSCMD
DESCRIPTOR.message_types_by_name['SniffCmd'] = _SNIFFCMD
DESCRIPTOR.message_types_by_name['JamCmd'] = _JAMCMD
DESCRIPTOR.message_types_by_name['SendCmd'] = _SENDCMD
DESCRIPTOR.message_types_by_name['EndDeviceCmd'] = _ENDDEVICECMD
DESCRIPTOR.message_types_by_name['RouterCmd'] = _ROUTERCMD
DESCRIPTOR.message_types_by_name['CoordinatorCmd'] = _COORDINATORCMD
DESCRIPTOR.message_types_by_name['StartCmd'] = _STARTCMD
DESCRIPTOR.message_types_by_name['StopCmd'] = _STOPCMD
DESCRIPTOR.message_types_by_name['ManInTheMiddleCmd'] = _MANINTHEMIDDLECMD
DESCRIPTOR.message_types_by_name['Jammed'] = _JAMMED
DESCRIPTOR.message_types_by_name['RawPduReceived'] = _RAWPDURECEIVED
DESCRIPTOR.message_types_by_name['PduReceived'] = _PDURECEIVED
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['ZigbeeCommand'] = _ZIGBEECOMMAND
DESCRIPTOR.enum_types_by_name['ZigbeeMitmRole'] = _ZIGBEEMITMROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetNodeAddressCmd = _reflection.GeneratedProtocolMessageType('SetNodeAddressCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETNODEADDRESSCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.SetNodeAddressCmd)
  })
_sym_db.RegisterMessage(SetNodeAddressCmd)

SniffCmd = _reflection.GeneratedProtocolMessageType('SniffCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.SniffCmd)
  })
_sym_db.RegisterMessage(SniffCmd)

JamCmd = _reflection.GeneratedProtocolMessageType('JamCmd', (_message.Message,), {
  'DESCRIPTOR' : _JAMCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.JamCmd)
  })
_sym_db.RegisterMessage(JamCmd)

SendCmd = _reflection.GeneratedProtocolMessageType('SendCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.SendCmd)
  })
_sym_db.RegisterMessage(SendCmd)

EndDeviceCmd = _reflection.GeneratedProtocolMessageType('EndDeviceCmd', (_message.Message,), {
  'DESCRIPTOR' : _ENDDEVICECMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.EndDeviceCmd)
  })
_sym_db.RegisterMessage(EndDeviceCmd)

RouterCmd = _reflection.GeneratedProtocolMessageType('RouterCmd', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.RouterCmd)
  })
_sym_db.RegisterMessage(RouterCmd)

CoordinatorCmd = _reflection.GeneratedProtocolMessageType('CoordinatorCmd', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATORCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.CoordinatorCmd)
  })
_sym_db.RegisterMessage(CoordinatorCmd)

StartCmd = _reflection.GeneratedProtocolMessageType('StartCmd', (_message.Message,), {
  'DESCRIPTOR' : _STARTCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.StartCmd)
  })
_sym_db.RegisterMessage(StartCmd)

StopCmd = _reflection.GeneratedProtocolMessageType('StopCmd', (_message.Message,), {
  'DESCRIPTOR' : _STOPCMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.StopCmd)
  })
_sym_db.RegisterMessage(StopCmd)

ManInTheMiddleCmd = _reflection.GeneratedProtocolMessageType('ManInTheMiddleCmd', (_message.Message,), {
  'DESCRIPTOR' : _MANINTHEMIDDLECMD,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.ManInTheMiddleCmd)
  })
_sym_db.RegisterMessage(ManInTheMiddleCmd)

Jammed = _reflection.GeneratedProtocolMessageType('Jammed', (_message.Message,), {
  'DESCRIPTOR' : _JAMMED,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.Jammed)
  })
_sym_db.RegisterMessage(Jammed)

RawPduReceived = _reflection.GeneratedProtocolMessageType('RawPduReceived', (_message.Message,), {
  'DESCRIPTOR' : _RAWPDURECEIVED,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.RawPduReceived)
  })
_sym_db.RegisterMessage(RawPduReceived)

PduReceived = _reflection.GeneratedProtocolMessageType('PduReceived', (_message.Message,), {
  'DESCRIPTOR' : _PDURECEIVED,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.PduReceived)
  })
_sym_db.RegisterMessage(PduReceived)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'protocol.zigbee.zigbee_pb2'
  # @@protoc_insertion_point(class_scope:zigbee.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
