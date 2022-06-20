"""
Bluetooth Low Energy
"""
from binascii import hexlify
from whad import WhadDomain, WhadCapability
from whad.device import WhadDeviceConnector
from whad.helpers import message_filter, is_message_type, bd_addr_to_bytes
from whad.device.uart import UartDevice
from whad.exceptions import UnsupportedDomain, UnsupportedCapability
from whad.protocol.generic_pb2 import ResultCode
from whad.protocol.whad_pb2 import Message
from whad.protocol.ble.ble_pb2 import BleDirection, CentralMode, StartCmd, StopCmd, \
    ScanMode, Start, Stop, BleAdvType, ConnectToCmd, ConnectTo, CentralModeCmd, \
    SendPDUCmd

from scapy.layers.bluetooth4LE import *


class BLE(WhadDeviceConnector):
    """
    BLE protocol connector.

    This connector drives a BLE-capable device with BLE-specific WHAD messages.
    It is required by various role classes to interact with a real device and pre-process
    domain-specific messages.
    """
    # correlation table
    SCAPY_CORR_ADV = {
        BleAdvType.ADV_IND: BTLE_ADV_IND,
        BleAdvType.ADV_NONCONN_IND: BTLE_ADV_NONCONN_IND,
        BleAdvType.ADV_DIRECT_IND: BTLE_ADV_DIRECT_IND,
        BleAdvType.ADV_SCAN_IND: BTLE_ADV_SCAN_IND,
        BleAdvType.ADV_SCAN_RSP: BTLE_SCAN_RSP
    }

    def __init__(self, device=None):
        """
        Initialize the connector, open the device (if not already opened), discover
        the services (if not already discovered). 
        """
        super().__init__(device)

        # Open device and make sure it is compatible
        self.device.open()
        self.device.discover()

        # Check device supports BLE
        if not self.device.has_domain(WhadDomain.BtLE):
            raise UnsupportedDomain()

    def can_scan(self):
        """
        Determine if the device implements a scanner mode.
        """
        # Retrieve supported commands
        commands = self.device.get_domain_commands(WhadDomain.BtLE)
        return (
            (commands & (1 << ScanMode))>0 and
            (commands & (1 << Start))>0 and
            (commands & (1 << Stop))>0
        )

    def can_be_central(self):
        """
        Determine if the device implements a central mode.
        """
        # Retrieve supported commands
        commands = self.device.get_domain_commands(WhadDomain.BtLE)
        return (
            (commands & (1 << CentralMode))>0 and
            (commands & (1 << ConnectTo))>0 and
            (commands & (1 << Start))>0 and
            (commands & (1 << Stop))>0
        )


    def enable_scan_mode(self, active=False):
        msg = Message()
        msg.ble.scan_mode.active_scan = active
        resp = self.send_command(msg, message_filter('generic', 'cmd_result'))

    def enable_central_mode(self):
        msg = Message()
        msg.ble.central_mode.CopyFrom(CentralModeCmd())
        resp = self.send_command(msg, message_filter('generic', 'cmd_result'))

    def connect_to(self, bd_addr):
        msg = Message()
        msg.ble.connect.bd_address = bd_addr_to_bytes(bd_addr)
        resp = self.send_command(msg, message_filter('generic', 'cmd_result'))

    def start(self):
        # Enable scanner
        msg = Message()
        msg.ble.start.CopyFrom(StartCmd())
        resp = self.send_command(msg, message_filter('generic', 'cmd_result'))
        return (resp.generic.cmd_result.result == ResultCode.SUCCESS)

    def stop(self):
        # Disable scanner
        msg = Message()
        msg.ble.stop.CopyFrom(StopCmd())
        resp = self.send_command(msg, message_filter('generic', 'cmd_result'))

    def on_generic_msg(self, message):
        #print('generic: %s' % message)
        pass

    def on_discovery_msg(self, message):
        pass

    def on_domain_msg(self, domain, message):
        if domain == 'ble':
            msg_type = message.WhichOneof('msg')
            if msg_type == 'adv_pdu':
                if message.adv_pdu.adv_type in BLE.SCAPY_CORR_ADV:
                    self.on_adv_pdu(
                        message.adv_pdu.rssi,
                        BLE.SCAPY_CORR_ADV[message.adv_pdu.adv_type](
                            bytes(message.adv_pdu.bd_address) + bytes(message.adv_pdu.adv_data)
                        )
                    )
            elif msg_type == 'pdu':
                self.on_pdu(message.pdu)

    def on_adv_pdu(self, rssi, packet):
        pass

    def on_pdu(self, pdu):
        print(hexlify(pdu.pdu))
        if pdu.pdu[0] & 0x3 == 0x03:
            self.on_ctl_pdu(pdu.direction, pdu.pdu)
        elif (pdu.pdu[0] & 0x3) in [0x01, 0x02]:
            self.on_data_pdu(pdu.direction, pdu.pdu)
        else:
            print('[!] Wrong LLID')
    
    def on_data_pdu(self, direction, pdu):
        print('[rx:data] %s' % hexlify(pdu))
        pass

    def on_ctl_pdu(self, direction, pdu):
        print('[rx:ctl] %s' % hexlify(pdu))
        pass

    def send_ctrl_pdu(self, pdu):
        """
        Send CTRL PDU
        """
        final_pdu = bytes([0x03, len(pdu)] + pdu)
        print('injecting pdu: %s' % final_pdu)
        msg = Message()
        msg.ble.send_pdu.direction = BleDirection.MASTER_TO_SLAVE
        msg.ble.send_pdu.pdu = final_pdu
        resp = self.send_command(msg, message_filter('generic', 'cmd_result'))
        print('cmd resp: %s' % resp)
        return (resp.generic.cmd_result.result == ResultCode.SUCCESS)

class Scanner(BLE):
    """
    BLE Observer interface for compatible WHAD device.
    """

    def __init__(self, device):
        super().__init__(device)

        # Check device accept scanning mode
        if not self.can_scan():
            raise UnsupportedCapability('Scan')
        else:
            self.stop()
            self.enable_scan_mode(True)

    def discover_devices(self):
        """
        Listen incoming messages and yield advertisements.
        """
        # correlation table
        scapy_corr_adv = {
            BleAdvType.ADV_IND: BTLE_ADV_IND,
            BleAdvType.ADV_NONCONN_IND: BTLE_ADV_NONCONN_IND,
            BleAdvType.ADV_DIRECT_IND: BTLE_ADV_DIRECT_IND,
            BleAdvType.ADV_SCAN_IND: BTLE_ADV_SCAN_IND,
            BleAdvType.ADV_SCAN_RSP: BTLE_SCAN_RSP
        }

        while True:
            message = self.wait_for_message(filter=message_filter('ble', 'adv_pdu'))
            # Convert message from rebuilt PDU
            if message.ble.adv_pdu.adv_type in scapy_corr_adv:
                yield (
                    message.ble.adv_pdu.rssi,
                    scapy_corr_adv[message.ble.adv_pdu.adv_type](
                        bytes(message.ble.adv_pdu.bd_address) + bytes(message.ble.adv_pdu.adv_data)
                    )
                )
            else:
                print('nope')

class Central(BLE):

    def __init__(self, device):
        super().__init__(device)

        # Check device accept central mode
        if not self.can_be_central():
            raise UnsupportedCapability('Central')
        else:
            self.stop()
            self.enable_central_mode()

