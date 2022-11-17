# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/ble/ble.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protocol/ble/ble.proto\x12\x03\x62le\"J\n\x0fSetBdAddressCmd\x12\x12\n\nbd_address\x18\x01 \x01(\x0c\x12#\n\taddr_type\x18\x02 \x01(\x0e\x32\x10.ble.BleAddrType\"L\n\x0bSniffAdvCmd\x12\x18\n\x10use_extended_adv\x18\x01 \x01(\x08\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\r\x12\x12\n\nbd_address\x18\x03 \x01(\x0c\"\x0b\n\tJamAdvCmd\"%\n\x12JamAdvOnChannelCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"o\n\x0fSniffConnReqCmd\x12\x1a\n\x12show_empty_packets\x18\x01 \x01(\x08\x12\x1b\n\x13show_advertisements\x18\x02 \x01(\x08\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\r\x12\x12\n\nbd_address\x18\x04 \x01(\x0c\"3\n\x15SniffAccessAddressCmd\x12\x1a\n\x12monitored_channels\x18\x06 \x01(\x0c\"\x9c\x01\n\x12SniffActiveConnCmd\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\x12\x10\n\x08\x63rc_init\x18\x02 \x01(\r\x12\x13\n\x0b\x63hannel_map\x18\x03 \x01(\x0c\x12\x14\n\x0chop_interval\x18\x04 \x01(\r\x12\x15\n\rhop_increment\x18\x05 \x01(\r\x12\x1a\n\x12monitored_channels\x18\x06 \x01(\x0c\"$\n\nJamConnCmd\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\"\"\n\x0bScanModeCmd\x12\x13\n\x0b\x61\x63tive_scan\x18\x01 \x01(\x08\"5\n\nAdvModeCmd\x12\x11\n\tscan_data\x18\x01 \x01(\x0c\x12\x14\n\x0cscanrsp_data\x18\x02 \x01(\x0c\"8\n\rSetAdvDataCmd\x12\x11\n\tscan_data\x18\x01 \x01(\x0c\x12\x14\n\x0cscanrsp_data\x18\x02 \x01(\x0c\"\x10\n\x0e\x43\x65ntralModeCmd\"G\n\x0c\x43onnectToCmd\x12\x12\n\nbd_address\x18\x01 \x01(\x0c\x12#\n\taddr_type\x18\x02 \x01(\x0e\x32\x10.ble.BleAddrType\"\x8d\x01\n\rSendRawPDUCmd\x12$\n\tdirection\x18\x01 \x01(\x0e\x32\x11.ble.BleDirection\x12\x13\n\x0b\x63onn_handle\x18\x02 \x01(\r\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x03 \x01(\r\x12\x0b\n\x03pdu\x18\x04 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x05 \x01(\r\x12\x0f\n\x07\x65ncrypt\x18\x06 \x01(\x08\"e\n\nSendPDUCmd\x12$\n\tdirection\x18\x01 \x01(\x0e\x32\x11.ble.BleDirection\x12\x13\n\x0b\x63onn_handle\x18\x02 \x01(\r\x12\x0b\n\x03pdu\x18\x03 \x01(\x0c\x12\x0f\n\x07\x65ncrypt\x18\x04 \x01(\x08\"$\n\rDisconnectCmd\x12\x13\n\x0b\x63onn_handle\x18\x01 \x01(\x05\"<\n\x11PeripheralModeCmd\x12\x11\n\tscan_data\x18\x01 \x01(\x0c\x12\x14\n\x0cscanrsp_data\x18\x02 \x01(\x0c\"\n\n\x08StartCmd\"\t\n\x07StopCmd\")\n\x0fHijackMasterCmd\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\"(\n\x0eHijackSlaveCmd\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\"\'\n\rHijackBothCmd\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\"<\n\x10SetEncryptionCmd\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\n\n\x02iv\x18\x03 \x01(\x0c\"D\n\x0eReactiveJamCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0f\n\x07pattern\x18\x02 \x01(\x0c\x12\x10\n\x08position\x18\x03 \x01(\r\"\xa9\x04\n\x12PrepareSequenceCmd\x12\x30\n\x07trigger\x18\x01 \x01(\x0b\x32\x1f.ble.PrepareSequenceCmd.Trigger\x12$\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ble.BleDirection\x12\x37\n\x08sequence\x18\x03 \x03(\x0b\x32%.ble.PrepareSequenceCmd.PendingPacket\x1a\x41\n\x10ReceptionTrigger\x12\x0f\n\x07pattern\x18\x01 \x01(\x0c\x12\x0c\n\x04mask\x18\x02 \x01(\x0c\x12\x0e\n\x06offset\x18\x03 \x01(\r\x1a\x32\n\x16\x43onnectionEventTrigger\x12\x18\n\x10\x63onnection_event\x18\x01 \x01(\r\x1a\x0f\n\rManualTrigger\x1a\xd8\x01\n\x07Trigger\x12=\n\treception\x18\x01 \x01(\x0b\x32(.ble.PrepareSequenceCmd.ReceptionTriggerH\x00\x12J\n\x10\x63onnection_event\x18\x02 \x01(\x0b\x32..ble.PrepareSequenceCmd.ConnectionEventTriggerH\x00\x12\x37\n\x06manual\x18\x03 \x01(\x0b\x32%.ble.PrepareSequenceCmd.ManualTriggerH\x00\x42\t\n\x07trigger\x1a\x1f\n\rPendingPacket\x12\x0e\n\x06packet\x18\x01 \x01(\x0c\"s\n\x17\x41\x63\x63\x65ssAddressDiscovered\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x42\x07\n\x05_rssiB\x0c\n\n_timestamp\"\x8c\x01\n\x0e\x41\x64vPduReceived\x12!\n\x08\x61\x64v_type\x18\x01 \x01(\x0e\x32\x0f.ble.BleAdvType\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x12\n\nbd_address\x18\x03 \x01(\x0c\x12\x10\n\x08\x61\x64v_data\x18\x04 \x01(\x0c\x12#\n\taddr_type\x18\x05 \x01(\x0e\x32\x10.ble.BleAddrType\"\xb2\x01\n\tConnected\x12\x11\n\tinitiator\x18\x01 \x01(\x0c\x12\x12\n\nadvertiser\x18\x02 \x01(\x0c\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x03 \x01(\r\x12\x13\n\x0b\x63onn_handle\x18\x08 \x01(\r\x12\'\n\radv_addr_type\x18\t \x01(\x0e\x32\x10.ble.BleAddrType\x12(\n\x0einit_addr_type\x18\n \x01(\x0e\x32\x10.ble.BleAddrType\"3\n\x0c\x44isconnected\x12\x0e\n\x06reason\x18\x01 \x01(\r\x12\x13\n\x0b\x63onn_handle\x18\x02 \x01(\r\"z\n\x0cSynchronized\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\x12\x10\n\x08\x63rc_init\x18\x02 \x01(\r\x12\x14\n\x0chop_interval\x18\x03 \x01(\r\x12\x15\n\rhop_increment\x18\x04 \x01(\r\x12\x13\n\x0b\x63hannel_map\x18\x05 \x01(\x0c\"(\n\x0e\x44\x65synchronized\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x01 \x01(\r\"3\n\x08Hijacked\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x02 \x01(\r\"O\n\x08Injected\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x02 \x01(\r\x12\x1a\n\x12injection_attempts\x18\x03 \x01(\r\"\xda\x02\n\x0eRawPduReceived\x12$\n\tdirection\x18\x01 \x01(\x0e\x32\x11.ble.BleDirection\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\r\x12\x11\n\x04rssi\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x04 \x01(\rH\x01\x88\x01\x01\x12\x1f\n\x12relative_timestamp\x18\x05 \x01(\rH\x02\x88\x01\x01\x12\x19\n\x0c\x63rc_validity\x18\x06 \x01(\x08H\x03\x88\x01\x01\x12\x16\n\x0e\x61\x63\x63\x65ss_address\x18\x07 \x01(\r\x12\x0b\n\x03pdu\x18\x08 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\t \x01(\r\x12\x13\n\x0b\x63onn_handle\x18\n \x01(\r\x12\x11\n\tprocessed\x18\x0b \x01(\x08\x12\x11\n\tdecrypted\x18\x0c \x01(\x08\x42\x07\n\x05_rssiB\x0c\n\n_timestampB\x15\n\x13_relative_timestampB\x0f\n\r_crc_validity\"{\n\x0bPduReceived\x12$\n\tdirection\x18\x01 \x01(\x0e\x32\x11.ble.BleDirection\x12\x0b\n\x03pdu\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63onn_handle\x18\x03 \x01(\r\x12\x11\n\tprocessed\x18\x04 \x01(\x08\x12\x11\n\tdecrypted\x18\x05 \x01(\x08\"\xbd\x0b\n\x07Message\x12+\n\x0bset_bd_addr\x18\x01 \x01(\x0b\x32\x14.ble.SetBdAddressCmdH\x00\x12%\n\tsniff_adv\x18\x02 \x01(\x0b\x32\x10.ble.SniffAdvCmdH\x00\x12!\n\x07jam_adv\x18\x03 \x01(\x0b\x32\x0e.ble.JamAdvCmdH\x00\x12/\n\x0cjam_adv_chan\x18\x04 \x01(\x0b\x32\x17.ble.JamAdvOnChannelCmdH\x00\x12-\n\rsniff_connreq\x18\x05 \x01(\x0b\x32\x14.ble.SniffConnReqCmdH\x00\x12.\n\x08sniff_aa\x18\x06 \x01(\x0b\x32\x1a.ble.SniffAccessAddressCmdH\x00\x12-\n\nsniff_conn\x18\x07 \x01(\x0b\x32\x17.ble.SniffActiveConnCmdH\x00\x12#\n\x08jam_conn\x18\x08 \x01(\x0b\x32\x0f.ble.JamConnCmdH\x00\x12%\n\tscan_mode\x18\t \x01(\x0b\x32\x10.ble.ScanModeCmdH\x00\x12#\n\x08\x61\x64v_mode\x18\n \x01(\x0b\x32\x0f.ble.AdvModeCmdH\x00\x12*\n\x0cset_adv_data\x18\x0b \x01(\x0b\x32\x12.ble.SetAdvDataCmdH\x00\x12+\n\x0c\x63\x65ntral_mode\x18\x0c \x01(\x0b\x32\x13.ble.CentralModeCmdH\x00\x12$\n\x07\x63onnect\x18\r \x01(\x0b\x32\x11.ble.ConnectToCmdH\x00\x12*\n\x0csend_raw_pdu\x18\x0e \x01(\x0b\x32\x12.ble.SendRawPDUCmdH\x00\x12#\n\x08send_pdu\x18\x0f \x01(\x0b\x32\x0f.ble.SendPDUCmdH\x00\x12(\n\ndisconnect\x18\x10 \x01(\x0b\x32\x12.ble.DisconnectCmdH\x00\x12-\n\x0bperiph_mode\x18\x11 \x01(\x0b\x32\x16.ble.PeripheralModeCmdH\x00\x12\x1e\n\x05start\x18\x12 \x01(\x0b\x32\r.ble.StartCmdH\x00\x12\x1c\n\x04stop\x18\x13 \x01(\x0b\x32\x0c.ble.StopCmdH\x00\x12-\n\rhijack_master\x18\x14 \x01(\x0b\x32\x14.ble.HijackMasterCmdH\x00\x12+\n\x0chijack_slave\x18\x15 \x01(\x0b\x32\x13.ble.HijackSlaveCmdH\x00\x12)\n\x0bhijack_both\x18\x16 \x01(\x0b\x32\x12.ble.HijackBothCmdH\x00\x12+\n\nencryption\x18! \x01(\x0b\x32\x15.ble.SetEncryptionCmdH\x00\x12+\n\x0creactive_jam\x18\" \x01(\x0b\x32\x13.ble.ReactiveJamCmdH\x00\x12*\n\x07prepare\x18# \x01(\x0b\x32\x17.ble.PrepareSequenceCmdH\x00\x12/\n\x07\x61\x61_disc\x18\x17 \x01(\x0b\x32\x1c.ble.AccessAddressDiscoveredH\x00\x12&\n\x07\x61\x64v_pdu\x18\x18 \x01(\x0b\x32\x13.ble.AdvPduReceivedH\x00\x12#\n\tconnected\x18\x19 \x01(\x0b\x32\x0e.ble.ConnectedH\x00\x12)\n\x0c\x64isconnected\x18\x1a \x01(\x0b\x32\x11.ble.DisconnectedH\x00\x12)\n\x0csynchronized\x18\x1b \x01(\x0b\x32\x11.ble.SynchronizedH\x00\x12!\n\x08hijacked\x18\x1c \x01(\x0b\x32\r.ble.HijackedH\x00\x12\x1f\n\x03pdu\x18\x1d \x01(\x0b\x32\x10.ble.PduReceivedH\x00\x12&\n\x07raw_pdu\x18\x1e \x01(\x0b\x32\x13.ble.RawPduReceivedH\x00\x12!\n\x08injected\x18\x1f \x01(\x0b\x32\r.ble.InjectedH\x00\x12-\n\x0e\x64\x65synchronized\x18  \x01(\x0b\x32\x13.ble.DesynchronizedH\x00\x42\x05\n\x03msg*\x93\x03\n\nBleCommand\x12\x10\n\x0cSetBdAddress\x10\x00\x12\x0c\n\x08SniffAdv\x10\x01\x12\n\n\x06JamAdv\x10\x02\x12\x13\n\x0fJamAdvOnChannel\x10\x03\x12\x10\n\x0cSniffConnReq\x10\x04\x12\x16\n\x12SniffAccessAddress\x10\x05\x12\x13\n\x0fSniffActiveConn\x10\x06\x12\x0b\n\x07JamConn\x10\x07\x12\x0c\n\x08ScanMode\x10\x08\x12\x0b\n\x07\x41\x64vMode\x10\t\x12\x0e\n\nSetAdvData\x10\n\x12\x0f\n\x0b\x43\x65ntralMode\x10\x0b\x12\r\n\tConnectTo\x10\x0c\x12\x0e\n\nSendRawPDU\x10\r\x12\x0b\n\x07SendPDU\x10\x0e\x12\x0e\n\nDisconnect\x10\x0f\x12\x12\n\x0ePeripheralMode\x10\x10\x12\t\n\x05Start\x10\x11\x12\x08\n\x04Stop\x10\x12\x12\x10\n\x0cHijackMaster\x10\x13\x12\x0f\n\x0bHijackSlave\x10\x14\x12\x0e\n\nHijackBoth\x10\x15\x12\x0f\n\x0bReactiveJam\x10\x16\x12\x13\n\x0fPrepareSequence\x10\x17*w\n\nBleAdvType\x12\x0f\n\x0b\x41\x44V_UNKNOWN\x10\x00\x12\x0b\n\x07\x41\x44V_IND\x10\x01\x12\x12\n\x0e\x41\x44V_DIRECT_IND\x10\x02\x12\x13\n\x0f\x41\x44V_NONCONN_IND\x10\x03\x12\x10\n\x0c\x41\x44V_SCAN_IND\x10\x04\x12\x10\n\x0c\x41\x44V_SCAN_RSP\x10\x05*v\n\x0c\x42leDirection\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fMASTER_TO_SLAVE\x10\x01\x12\x13\n\x0fSLAVE_TO_MASTER\x10\x02\x12\x16\n\x12INJECTION_TO_SLAVE\x10\x03\x12\x17\n\x13INJECTION_TO_MASTER\x10\x04*%\n\x0b\x42leAddrType\x12\n\n\x06PUBLIC\x10\x00\x12\n\n\x06RANDOM\x10\x01\x62\x06proto3')

_BLECOMMAND = DESCRIPTOR.enum_types_by_name['BleCommand']
BleCommand = enum_type_wrapper.EnumTypeWrapper(_BLECOMMAND)
_BLEADVTYPE = DESCRIPTOR.enum_types_by_name['BleAdvType']
BleAdvType = enum_type_wrapper.EnumTypeWrapper(_BLEADVTYPE)
_BLEDIRECTION = DESCRIPTOR.enum_types_by_name['BleDirection']
BleDirection = enum_type_wrapper.EnumTypeWrapper(_BLEDIRECTION)
_BLEADDRTYPE = DESCRIPTOR.enum_types_by_name['BleAddrType']
BleAddrType = enum_type_wrapper.EnumTypeWrapper(_BLEADDRTYPE)
SetBdAddress = 0
SniffAdv = 1
JamAdv = 2
JamAdvOnChannel = 3
SniffConnReq = 4
SniffAccessAddress = 5
SniffActiveConn = 6
JamConn = 7
ScanMode = 8
AdvMode = 9
SetAdvData = 10
CentralMode = 11
ConnectTo = 12
SendRawPDU = 13
SendPDU = 14
Disconnect = 15
PeripheralMode = 16
Start = 17
Stop = 18
HijackMaster = 19
HijackSlave = 20
HijackBoth = 21
ReactiveJam = 22
PrepareSequence = 23
ADV_UNKNOWN = 0
ADV_IND = 1
ADV_DIRECT_IND = 2
ADV_NONCONN_IND = 3
ADV_SCAN_IND = 4
ADV_SCAN_RSP = 5
UNKNOWN = 0
MASTER_TO_SLAVE = 1
SLAVE_TO_MASTER = 2
INJECTION_TO_SLAVE = 3
INJECTION_TO_MASTER = 4
PUBLIC = 0
RANDOM = 1


_SETBDADDRESSCMD = DESCRIPTOR.message_types_by_name['SetBdAddressCmd']
_SNIFFADVCMD = DESCRIPTOR.message_types_by_name['SniffAdvCmd']
_JAMADVCMD = DESCRIPTOR.message_types_by_name['JamAdvCmd']
_JAMADVONCHANNELCMD = DESCRIPTOR.message_types_by_name['JamAdvOnChannelCmd']
_SNIFFCONNREQCMD = DESCRIPTOR.message_types_by_name['SniffConnReqCmd']
_SNIFFACCESSADDRESSCMD = DESCRIPTOR.message_types_by_name['SniffAccessAddressCmd']
_SNIFFACTIVECONNCMD = DESCRIPTOR.message_types_by_name['SniffActiveConnCmd']
_JAMCONNCMD = DESCRIPTOR.message_types_by_name['JamConnCmd']
_SCANMODECMD = DESCRIPTOR.message_types_by_name['ScanModeCmd']
_ADVMODECMD = DESCRIPTOR.message_types_by_name['AdvModeCmd']
_SETADVDATACMD = DESCRIPTOR.message_types_by_name['SetAdvDataCmd']
_CENTRALMODECMD = DESCRIPTOR.message_types_by_name['CentralModeCmd']
_CONNECTTOCMD = DESCRIPTOR.message_types_by_name['ConnectToCmd']
_SENDRAWPDUCMD = DESCRIPTOR.message_types_by_name['SendRawPDUCmd']
_SENDPDUCMD = DESCRIPTOR.message_types_by_name['SendPDUCmd']
_DISCONNECTCMD = DESCRIPTOR.message_types_by_name['DisconnectCmd']
_PERIPHERALMODECMD = DESCRIPTOR.message_types_by_name['PeripheralModeCmd']
_STARTCMD = DESCRIPTOR.message_types_by_name['StartCmd']
_STOPCMD = DESCRIPTOR.message_types_by_name['StopCmd']
_HIJACKMASTERCMD = DESCRIPTOR.message_types_by_name['HijackMasterCmd']
_HIJACKSLAVECMD = DESCRIPTOR.message_types_by_name['HijackSlaveCmd']
_HIJACKBOTHCMD = DESCRIPTOR.message_types_by_name['HijackBothCmd']
_SETENCRYPTIONCMD = DESCRIPTOR.message_types_by_name['SetEncryptionCmd']
_REACTIVEJAMCMD = DESCRIPTOR.message_types_by_name['ReactiveJamCmd']
_PREPARESEQUENCECMD = DESCRIPTOR.message_types_by_name['PrepareSequenceCmd']
_PREPARESEQUENCECMD_RECEPTIONTRIGGER = _PREPARESEQUENCECMD.nested_types_by_name['ReceptionTrigger']
_PREPARESEQUENCECMD_CONNECTIONEVENTTRIGGER = _PREPARESEQUENCECMD.nested_types_by_name['ConnectionEventTrigger']
_PREPARESEQUENCECMD_MANUALTRIGGER = _PREPARESEQUENCECMD.nested_types_by_name['ManualTrigger']
_PREPARESEQUENCECMD_TRIGGER = _PREPARESEQUENCECMD.nested_types_by_name['Trigger']
_PREPARESEQUENCECMD_PENDINGPACKET = _PREPARESEQUENCECMD.nested_types_by_name['PendingPacket']
_ACCESSADDRESSDISCOVERED = DESCRIPTOR.message_types_by_name['AccessAddressDiscovered']
_ADVPDURECEIVED = DESCRIPTOR.message_types_by_name['AdvPduReceived']
_CONNECTED = DESCRIPTOR.message_types_by_name['Connected']
_DISCONNECTED = DESCRIPTOR.message_types_by_name['Disconnected']
_SYNCHRONIZED = DESCRIPTOR.message_types_by_name['Synchronized']
_DESYNCHRONIZED = DESCRIPTOR.message_types_by_name['Desynchronized']
_HIJACKED = DESCRIPTOR.message_types_by_name['Hijacked']
_INJECTED = DESCRIPTOR.message_types_by_name['Injected']
_RAWPDURECEIVED = DESCRIPTOR.message_types_by_name['RawPduReceived']
_PDURECEIVED = DESCRIPTOR.message_types_by_name['PduReceived']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
SetBdAddressCmd = _reflection.GeneratedProtocolMessageType('SetBdAddressCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETBDADDRESSCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SetBdAddressCmd)
  })
_sym_db.RegisterMessage(SetBdAddressCmd)

SniffAdvCmd = _reflection.GeneratedProtocolMessageType('SniffAdvCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFADVCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SniffAdvCmd)
  })
_sym_db.RegisterMessage(SniffAdvCmd)

JamAdvCmd = _reflection.GeneratedProtocolMessageType('JamAdvCmd', (_message.Message,), {
  'DESCRIPTOR' : _JAMADVCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.JamAdvCmd)
  })
_sym_db.RegisterMessage(JamAdvCmd)

JamAdvOnChannelCmd = _reflection.GeneratedProtocolMessageType('JamAdvOnChannelCmd', (_message.Message,), {
  'DESCRIPTOR' : _JAMADVONCHANNELCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.JamAdvOnChannelCmd)
  })
_sym_db.RegisterMessage(JamAdvOnChannelCmd)

SniffConnReqCmd = _reflection.GeneratedProtocolMessageType('SniffConnReqCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFCONNREQCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SniffConnReqCmd)
  })
_sym_db.RegisterMessage(SniffConnReqCmd)

SniffAccessAddressCmd = _reflection.GeneratedProtocolMessageType('SniffAccessAddressCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFACCESSADDRESSCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SniffAccessAddressCmd)
  })
_sym_db.RegisterMessage(SniffAccessAddressCmd)

SniffActiveConnCmd = _reflection.GeneratedProtocolMessageType('SniffActiveConnCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFACTIVECONNCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SniffActiveConnCmd)
  })
_sym_db.RegisterMessage(SniffActiveConnCmd)

JamConnCmd = _reflection.GeneratedProtocolMessageType('JamConnCmd', (_message.Message,), {
  'DESCRIPTOR' : _JAMCONNCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.JamConnCmd)
  })
_sym_db.RegisterMessage(JamConnCmd)

ScanModeCmd = _reflection.GeneratedProtocolMessageType('ScanModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _SCANMODECMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.ScanModeCmd)
  })
_sym_db.RegisterMessage(ScanModeCmd)

AdvModeCmd = _reflection.GeneratedProtocolMessageType('AdvModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _ADVMODECMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.AdvModeCmd)
  })
_sym_db.RegisterMessage(AdvModeCmd)

SetAdvDataCmd = _reflection.GeneratedProtocolMessageType('SetAdvDataCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETADVDATACMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SetAdvDataCmd)
  })
_sym_db.RegisterMessage(SetAdvDataCmd)

CentralModeCmd = _reflection.GeneratedProtocolMessageType('CentralModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _CENTRALMODECMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.CentralModeCmd)
  })
_sym_db.RegisterMessage(CentralModeCmd)

ConnectToCmd = _reflection.GeneratedProtocolMessageType('ConnectToCmd', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTTOCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.ConnectToCmd)
  })
_sym_db.RegisterMessage(ConnectToCmd)

SendRawPDUCmd = _reflection.GeneratedProtocolMessageType('SendRawPDUCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDRAWPDUCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SendRawPDUCmd)
  })
_sym_db.RegisterMessage(SendRawPDUCmd)

SendPDUCmd = _reflection.GeneratedProtocolMessageType('SendPDUCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDPDUCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SendPDUCmd)
  })
_sym_db.RegisterMessage(SendPDUCmd)

DisconnectCmd = _reflection.GeneratedProtocolMessageType('DisconnectCmd', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.DisconnectCmd)
  })
_sym_db.RegisterMessage(DisconnectCmd)

PeripheralModeCmd = _reflection.GeneratedProtocolMessageType('PeripheralModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALMODECMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.PeripheralModeCmd)
  })
_sym_db.RegisterMessage(PeripheralModeCmd)

StartCmd = _reflection.GeneratedProtocolMessageType('StartCmd', (_message.Message,), {
  'DESCRIPTOR' : _STARTCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.StartCmd)
  })
_sym_db.RegisterMessage(StartCmd)

StopCmd = _reflection.GeneratedProtocolMessageType('StopCmd', (_message.Message,), {
  'DESCRIPTOR' : _STOPCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.StopCmd)
  })
_sym_db.RegisterMessage(StopCmd)

HijackMasterCmd = _reflection.GeneratedProtocolMessageType('HijackMasterCmd', (_message.Message,), {
  'DESCRIPTOR' : _HIJACKMASTERCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.HijackMasterCmd)
  })
_sym_db.RegisterMessage(HijackMasterCmd)

HijackSlaveCmd = _reflection.GeneratedProtocolMessageType('HijackSlaveCmd', (_message.Message,), {
  'DESCRIPTOR' : _HIJACKSLAVECMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.HijackSlaveCmd)
  })
_sym_db.RegisterMessage(HijackSlaveCmd)

HijackBothCmd = _reflection.GeneratedProtocolMessageType('HijackBothCmd', (_message.Message,), {
  'DESCRIPTOR' : _HIJACKBOTHCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.HijackBothCmd)
  })
_sym_db.RegisterMessage(HijackBothCmd)

SetEncryptionCmd = _reflection.GeneratedProtocolMessageType('SetEncryptionCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETENCRYPTIONCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.SetEncryptionCmd)
  })
_sym_db.RegisterMessage(SetEncryptionCmd)

ReactiveJamCmd = _reflection.GeneratedProtocolMessageType('ReactiveJamCmd', (_message.Message,), {
  'DESCRIPTOR' : _REACTIVEJAMCMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.ReactiveJamCmd)
  })
_sym_db.RegisterMessage(ReactiveJamCmd)

PrepareSequenceCmd = _reflection.GeneratedProtocolMessageType('PrepareSequenceCmd', (_message.Message,), {

  'ReceptionTrigger' : _reflection.GeneratedProtocolMessageType('ReceptionTrigger', (_message.Message,), {
    'DESCRIPTOR' : _PREPARESEQUENCECMD_RECEPTIONTRIGGER,
    '__module__' : 'protocol.ble.ble_pb2'
    # @@protoc_insertion_point(class_scope:ble.PrepareSequenceCmd.ReceptionTrigger)
    })
  ,

  'ConnectionEventTrigger' : _reflection.GeneratedProtocolMessageType('ConnectionEventTrigger', (_message.Message,), {
    'DESCRIPTOR' : _PREPARESEQUENCECMD_CONNECTIONEVENTTRIGGER,
    '__module__' : 'protocol.ble.ble_pb2'
    # @@protoc_insertion_point(class_scope:ble.PrepareSequenceCmd.ConnectionEventTrigger)
    })
  ,

  'ManualTrigger' : _reflection.GeneratedProtocolMessageType('ManualTrigger', (_message.Message,), {
    'DESCRIPTOR' : _PREPARESEQUENCECMD_MANUALTRIGGER,
    '__module__' : 'protocol.ble.ble_pb2'
    # @@protoc_insertion_point(class_scope:ble.PrepareSequenceCmd.ManualTrigger)
    })
  ,

  'Trigger' : _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
    'DESCRIPTOR' : _PREPARESEQUENCECMD_TRIGGER,
    '__module__' : 'protocol.ble.ble_pb2'
    # @@protoc_insertion_point(class_scope:ble.PrepareSequenceCmd.Trigger)
    })
  ,

  'PendingPacket' : _reflection.GeneratedProtocolMessageType('PendingPacket', (_message.Message,), {
    'DESCRIPTOR' : _PREPARESEQUENCECMD_PENDINGPACKET,
    '__module__' : 'protocol.ble.ble_pb2'
    # @@protoc_insertion_point(class_scope:ble.PrepareSequenceCmd.PendingPacket)
    })
  ,
  'DESCRIPTOR' : _PREPARESEQUENCECMD,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.PrepareSequenceCmd)
  })
_sym_db.RegisterMessage(PrepareSequenceCmd)
_sym_db.RegisterMessage(PrepareSequenceCmd.ReceptionTrigger)
_sym_db.RegisterMessage(PrepareSequenceCmd.ConnectionEventTrigger)
_sym_db.RegisterMessage(PrepareSequenceCmd.ManualTrigger)
_sym_db.RegisterMessage(PrepareSequenceCmd.Trigger)
_sym_db.RegisterMessage(PrepareSequenceCmd.PendingPacket)

AccessAddressDiscovered = _reflection.GeneratedProtocolMessageType('AccessAddressDiscovered', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSADDRESSDISCOVERED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.AccessAddressDiscovered)
  })
_sym_db.RegisterMessage(AccessAddressDiscovered)

AdvPduReceived = _reflection.GeneratedProtocolMessageType('AdvPduReceived', (_message.Message,), {
  'DESCRIPTOR' : _ADVPDURECEIVED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.AdvPduReceived)
  })
_sym_db.RegisterMessage(AdvPduReceived)

Connected = _reflection.GeneratedProtocolMessageType('Connected', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Connected)
  })
_sym_db.RegisterMessage(Connected)

Disconnected = _reflection.GeneratedProtocolMessageType('Disconnected', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Disconnected)
  })
_sym_db.RegisterMessage(Disconnected)

Synchronized = _reflection.GeneratedProtocolMessageType('Synchronized', (_message.Message,), {
  'DESCRIPTOR' : _SYNCHRONIZED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Synchronized)
  })
_sym_db.RegisterMessage(Synchronized)

Desynchronized = _reflection.GeneratedProtocolMessageType('Desynchronized', (_message.Message,), {
  'DESCRIPTOR' : _DESYNCHRONIZED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Desynchronized)
  })
_sym_db.RegisterMessage(Desynchronized)

Hijacked = _reflection.GeneratedProtocolMessageType('Hijacked', (_message.Message,), {
  'DESCRIPTOR' : _HIJACKED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Hijacked)
  })
_sym_db.RegisterMessage(Hijacked)

Injected = _reflection.GeneratedProtocolMessageType('Injected', (_message.Message,), {
  'DESCRIPTOR' : _INJECTED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Injected)
  })
_sym_db.RegisterMessage(Injected)

RawPduReceived = _reflection.GeneratedProtocolMessageType('RawPduReceived', (_message.Message,), {
  'DESCRIPTOR' : _RAWPDURECEIVED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.RawPduReceived)
  })
_sym_db.RegisterMessage(RawPduReceived)

PduReceived = _reflection.GeneratedProtocolMessageType('PduReceived', (_message.Message,), {
  'DESCRIPTOR' : _PDURECEIVED,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.PduReceived)
  })
_sym_db.RegisterMessage(PduReceived)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'protocol.ble.ble_pb2'
  # @@protoc_insertion_point(class_scope:ble.Message)
  })
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLECOMMAND._serialized_start=4765
  _BLECOMMAND._serialized_end=5168
  _BLEADVTYPE._serialized_start=5170
  _BLEADVTYPE._serialized_end=5289
  _BLEDIRECTION._serialized_start=5291
  _BLEDIRECTION._serialized_end=5409
  _BLEADDRTYPE._serialized_start=5411
  _BLEADDRTYPE._serialized_end=5448
  _SETBDADDRESSCMD._serialized_start=31
  _SETBDADDRESSCMD._serialized_end=105
  _SNIFFADVCMD._serialized_start=107
  _SNIFFADVCMD._serialized_end=183
  _JAMADVCMD._serialized_start=185
  _JAMADVCMD._serialized_end=196
  _JAMADVONCHANNELCMD._serialized_start=198
  _JAMADVONCHANNELCMD._serialized_end=235
  _SNIFFCONNREQCMD._serialized_start=237
  _SNIFFCONNREQCMD._serialized_end=348
  _SNIFFACCESSADDRESSCMD._serialized_start=350
  _SNIFFACCESSADDRESSCMD._serialized_end=401
  _SNIFFACTIVECONNCMD._serialized_start=404
  _SNIFFACTIVECONNCMD._serialized_end=560
  _JAMCONNCMD._serialized_start=562
  _JAMCONNCMD._serialized_end=598
  _SCANMODECMD._serialized_start=600
  _SCANMODECMD._serialized_end=634
  _ADVMODECMD._serialized_start=636
  _ADVMODECMD._serialized_end=689
  _SETADVDATACMD._serialized_start=691
  _SETADVDATACMD._serialized_end=747
  _CENTRALMODECMD._serialized_start=749
  _CENTRALMODECMD._serialized_end=765
  _CONNECTTOCMD._serialized_start=767
  _CONNECTTOCMD._serialized_end=838
  _SENDRAWPDUCMD._serialized_start=841
  _SENDRAWPDUCMD._serialized_end=982
  _SENDPDUCMD._serialized_start=984
  _SENDPDUCMD._serialized_end=1085
  _DISCONNECTCMD._serialized_start=1087
  _DISCONNECTCMD._serialized_end=1123
  _PERIPHERALMODECMD._serialized_start=1125
  _PERIPHERALMODECMD._serialized_end=1185
  _STARTCMD._serialized_start=1187
  _STARTCMD._serialized_end=1197
  _STOPCMD._serialized_start=1199
  _STOPCMD._serialized_end=1208
  _HIJACKMASTERCMD._serialized_start=1210
  _HIJACKMASTERCMD._serialized_end=1251
  _HIJACKSLAVECMD._serialized_start=1253
  _HIJACKSLAVECMD._serialized_end=1293
  _HIJACKBOTHCMD._serialized_start=1295
  _HIJACKBOTHCMD._serialized_end=1334
  _SETENCRYPTIONCMD._serialized_start=1336
  _SETENCRYPTIONCMD._serialized_end=1396
  _REACTIVEJAMCMD._serialized_start=1398
  _REACTIVEJAMCMD._serialized_end=1466
  _PREPARESEQUENCECMD._serialized_start=1469
  _PREPARESEQUENCECMD._serialized_end=2022
  _PREPARESEQUENCECMD_RECEPTIONTRIGGER._serialized_start=1636
  _PREPARESEQUENCECMD_RECEPTIONTRIGGER._serialized_end=1701
  _PREPARESEQUENCECMD_CONNECTIONEVENTTRIGGER._serialized_start=1703
  _PREPARESEQUENCECMD_CONNECTIONEVENTTRIGGER._serialized_end=1753
  _PREPARESEQUENCECMD_MANUALTRIGGER._serialized_start=1755
  _PREPARESEQUENCECMD_MANUALTRIGGER._serialized_end=1770
  _PREPARESEQUENCECMD_TRIGGER._serialized_start=1773
  _PREPARESEQUENCECMD_TRIGGER._serialized_end=1989
  _PREPARESEQUENCECMD_PENDINGPACKET._serialized_start=1991
  _PREPARESEQUENCECMD_PENDINGPACKET._serialized_end=2022
  _ACCESSADDRESSDISCOVERED._serialized_start=2024
  _ACCESSADDRESSDISCOVERED._serialized_end=2139
  _ADVPDURECEIVED._serialized_start=2142
  _ADVPDURECEIVED._serialized_end=2282
  _CONNECTED._serialized_start=2285
  _CONNECTED._serialized_end=2463
  _DISCONNECTED._serialized_start=2465
  _DISCONNECTED._serialized_end=2516
  _SYNCHRONIZED._serialized_start=2518
  _SYNCHRONIZED._serialized_end=2640
  _DESYNCHRONIZED._serialized_start=2642
  _DESYNCHRONIZED._serialized_end=2682
  _HIJACKED._serialized_start=2684
  _HIJACKED._serialized_end=2735
  _INJECTED._serialized_start=2737
  _INJECTED._serialized_end=2816
  _RAWPDURECEIVED._serialized_start=2819
  _RAWPDURECEIVED._serialized_end=3165
  _PDURECEIVED._serialized_start=3167
  _PDURECEIVED._serialized_end=3290
  _MESSAGE._serialized_start=3293
  _MESSAGE._serialized_end=4762
# @@protoc_insertion_point(module_scope)
