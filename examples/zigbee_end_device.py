from whad.zigbee import EndDevice
from whad.zigbee.stack.aps.constants import APSDestinationAddressMode
from whad.zigbee.stack.mac.constants import MACScanType
from whad.device import WhadDevice
from whad.zigbee.crypto import NetworkLayerCryptoManager
from whad.exceptions import WhadDeviceNotFound
from whad.zigbee.stack.apl.application import ApplicationObject
from whad.zigbee.stack.apl.zcl.clusters import ZCLOnOff#, ZCLTouchLink
from time import time,sleep
from whad.common.monitors import PcapWriterMonitor
from scapy.compat import raw
from scapy.layers.dot15d4 import Dot15d4
import sys

import logging
logging.basicConfig(level=logging.WARNING)
#logging.getLogger('whad.zigbee.stack.mac').setLevel(logging.INFO)
logging.getLogger('whad.zigbee.stack.nwk').setLevel(logging.INFO)
#logging.getLogger('whad.zigbee.stack.aps').setLevel(logging.INFO)
logging.getLogger('whad.zigbee.stack.apl').setLevel(logging.INFO)
logging.getLogger('whad.zigbee.stack.apl.zcl').setLevel(logging.INFO)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # Retrieve target interface
        interface = sys.argv[1]
        # Connect to target device and performs discovery
        try:
            #monitor = PcapWriterMonitor("/tmp/decrypt.pcap")

            dev = WhadDevice.create(interface)
            endDevice = EndDevice(dev)


            #monitor.attach(endDevice)
            #monitor.start()
            endDevice.start()
            endDevice.stack.set_channel(15)
            onoff = ZCLOnOff()
            myApp2 = ApplicationObject("onoff", 0x0104, 0x0100, device_version=0, input_clusters=[], output_clusters=[onoff])
            endDevice.stack.apl.attach_application(myApp2, endpoint=1)

            zdo = endDevice.stack.apl.get_application_by_name("zdo")

            endDevice.stack.apl.initialize()

            '''
            zdo.network_manager.configure_extended_address(0x00178801026e61e4)
            zdo.network_manager.configure_short_address(0x729b)
            zdo.network_manager.configure_extended_pan_id(0x0940843f53270013)
            zdo.security_manager.provision_network_key('02:39:84:09:24:51:56:E3:1D:98:A9:21:57:A8:A6:6F')
            '''
            endDevice.stack.apl.start()

            onoff.connect(0x3f00,10)
            input()
            complete, attributes = onoff.discover_attributes(0, 10)
            print(complete, attributes)
            
            while True:
                onoff.toggle()
                input()
        except (KeyboardInterrupt, SystemExit):
            dev.close()

        except WhadDeviceNotFound:
            print('[e] Device not found')
            exit(1)
    else:
        print('Usage: %s [device]' % sys.argv[0])