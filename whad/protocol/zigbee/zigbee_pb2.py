# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/zigbee/zigbee.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cprotocol/zigbee/zigbee.proto\x12\x06zigbee\"$\n\x11SetNodeAddressCmd\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"\x1b\n\x08SniffCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"\x19\n\x06JamCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"4\n\x07SendCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0b\n\x03pdu\x18\x02 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x03 \x01(\r\"\x0e\n\x0c\x45ndDeviceCmd\"\x0b\n\tRouterCmd\"\x10\n\x0e\x43oordinatorCmd\"\n\n\x08StartCmd\"\t\n\x07StopCmd\"9\n\x11ManInTheMiddleCmd\x12$\n\x04role\x18\x01 \x01(\x0e\x32\x16.zigbee.ZigbeeMitmRole\"\x1b\n\x06Jammed\x12\x11\n\ttimestamp\x18\x01 \x01(\r\"\xa9\x01\n\x0eRawPduReceived\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0c\x66\x63s_validity\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x0b\n\x03pdu\x18\x05 \x01(\x0c\x12\x0b\n\x03\x66\x63s\x18\x06 \x01(\rB\x07\n\x05_rssiB\x0c\n\n_timestampB\x0f\n\r_fcs_validity\"\x99\x01\n\x0bPduReceived\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0c\x66\x63s_validity\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x0b\n\x03pdu\x18\x05 \x01(\x0c\x42\x07\n\x05_rssiB\x0c\n\n_timestampB\x0f\n\r_fcs_validity\"\x87\x04\n\x07Message\x12\x32\n\rset_node_addr\x18\x01 \x01(\x0b\x32\x19.zigbee.SetNodeAddressCmdH\x00\x12!\n\x05sniff\x18\x02 \x01(\x0b\x32\x10.zigbee.SniffCmdH\x00\x12\x1d\n\x03jam\x18\x03 \x01(\x0b\x32\x0e.zigbee.JamCmdH\x00\x12\x1f\n\x04send\x18\x04 \x01(\x0b\x32\x0f.zigbee.SendCmdH\x00\x12*\n\nend_device\x18\x05 \x01(\x0b\x32\x14.zigbee.EndDeviceCmdH\x00\x12#\n\x06router\x18\x06 \x01(\x0b\x32\x11.zigbee.RouterCmdH\x00\x12-\n\x0b\x63oordinator\x18\x07 \x01(\x0b\x32\x16.zigbee.CoordinatorCmdH\x00\x12!\n\x05start\x18\x08 \x01(\x0b\x32\x10.zigbee.StartCmdH\x00\x12\x1f\n\x04stop\x18\t \x01(\x0b\x32\x0f.zigbee.StopCmdH\x00\x12)\n\x04mitm\x18\n \x01(\x0b\x32\x19.zigbee.ManInTheMiddleCmdH\x00\x12 \n\x06jammed\x18\x0b \x01(\x0b\x32\x0e.zigbee.JammedH\x00\x12)\n\x07raw_pdu\x18\x0c \x01(\x0b\x32\x16.zigbee.RawPduReceivedH\x00\x12\"\n\x03pdu\x18\r \x01(\x0b\x32\x13.zigbee.PduReceivedH\x00\x42\x05\n\x03msg*\xa2\x01\n\rZigbeeCommand\x12\x12\n\x0eSetNodeAddress\x10\x00\x12\t\n\x05Sniff\x10\x01\x12\x07\n\x03Jam\x10\x02\x12\x08\n\x04Send\x10\x03\x12\x11\n\rEndDeviceMode\x10\x04\x12\x13\n\x0f\x43oordinatorMode\x10\x05\x12\x0e\n\nRouterMode\x10\x06\x12\t\n\x05Start\x10\x07\x12\x08\n\x04Stop\x10\x08\x12\x12\n\x0eManInTheMiddle\x10\t*4\n\x0eZigbeeMitmRole\x12\x13\n\x0fREACTIVE_JAMMER\x10\x00\x12\r\n\tCORRECTOR\x10\x01\x62\x06proto3')

_ZIGBEECOMMAND = DESCRIPTOR.enum_types_by_name['ZigbeeCommand']
ZigbeeCommand = enum_type_wrapper.EnumTypeWrapper(_ZIGBEECOMMAND)
_ZIGBEEMITMROLE = DESCRIPTOR.enum_types_by_name['ZigbeeMitmRole']
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


_SETNODEADDRESSCMD = DESCRIPTOR.message_types_by_name['SetNodeAddressCmd']
_SNIFFCMD = DESCRIPTOR.message_types_by_name['SniffCmd']
_JAMCMD = DESCRIPTOR.message_types_by_name['JamCmd']
_SENDCMD = DESCRIPTOR.message_types_by_name['SendCmd']
_ENDDEVICECMD = DESCRIPTOR.message_types_by_name['EndDeviceCmd']
_ROUTERCMD = DESCRIPTOR.message_types_by_name['RouterCmd']
_COORDINATORCMD = DESCRIPTOR.message_types_by_name['CoordinatorCmd']
_STARTCMD = DESCRIPTOR.message_types_by_name['StartCmd']
_STOPCMD = DESCRIPTOR.message_types_by_name['StopCmd']
_MANINTHEMIDDLECMD = DESCRIPTOR.message_types_by_name['ManInTheMiddleCmd']
_JAMMED = DESCRIPTOR.message_types_by_name['Jammed']
_RAWPDURECEIVED = DESCRIPTOR.message_types_by_name['RawPduReceived']
_PDURECEIVED = DESCRIPTOR.message_types_by_name['PduReceived']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
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

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ZIGBEECOMMAND._serialized_start=1197
  _ZIGBEECOMMAND._serialized_end=1359
  _ZIGBEEMITMROLE._serialized_start=1361
  _ZIGBEEMITMROLE._serialized_end=1413
  _SETNODEADDRESSCMD._serialized_start=40
  _SETNODEADDRESSCMD._serialized_end=76
  _SNIFFCMD._serialized_start=78
  _SNIFFCMD._serialized_end=105
  _JAMCMD._serialized_start=107
  _JAMCMD._serialized_end=132
  _SENDCMD._serialized_start=134
  _SENDCMD._serialized_end=186
  _ENDDEVICECMD._serialized_start=188
  _ENDDEVICECMD._serialized_end=202
  _ROUTERCMD._serialized_start=204
  _ROUTERCMD._serialized_end=215
  _COORDINATORCMD._serialized_start=217
  _COORDINATORCMD._serialized_end=233
  _STARTCMD._serialized_start=235
  _STARTCMD._serialized_end=245
  _STOPCMD._serialized_start=247
  _STOPCMD._serialized_end=256
  _MANINTHEMIDDLECMD._serialized_start=258
  _MANINTHEMIDDLECMD._serialized_end=315
  _JAMMED._serialized_start=317
  _JAMMED._serialized_end=344
  _RAWPDURECEIVED._serialized_start=347
  _RAWPDURECEIVED._serialized_end=516
  _PDURECEIVED._serialized_start=519
  _PDURECEIVED._serialized_end=672
  _MESSAGE._serialized_start=675
  _MESSAGE._serialized_end=1194
# @@protoc_insertion_point(module_scope)
