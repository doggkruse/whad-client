from whad.device import WhadDevice
from whad.zigbee import Coordinator
from whad.common.monitors import WiresharkMonitor
from whad.zigbee.stack.apl.application import ApplicationObject
from whad.zigbee.stack.apl.zcl.clusters.onoff import OnOffServer
from whad.exceptions import WhadDeviceNotFound
from scapy.compat import raw
from random import randint
import sys

import logging

logging.getLogger('whad.zigbee.stack.apl').setLevel(logging.INFO)
logging.getLogger('whad.zigbee.stack.apl.zcl').setLevel(logging.INFO)


def show(pkt):
    if hasattr(pkt, "metadata"):
        print(pkt.metadata, bytes(pkt).hex(), repr(pkt))

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # Retrieve target interface

        interface = sys.argv[1]

        try:
            monitor = WiresharkMonitor()

            dev = WhadDevice.create(interface)

            onoff = OnOffServer()
            #end_device = EndDevice(dev,
            #touchlink = ZCLTouchLinkClient()
            #zll = ApplicationObject("zll_app", 0xc05e, 0x0100, device_version=0, input_clusters=[], output_clusters=[])
            #zll.add_output_cluster(touchlink)

            basic_app = ApplicationObject(
                "basic_app",
                profile_id = 0x0104,
                device_id = 0x0100,
                device_version = 0,
                input_clusters=[],
                output_clusters=[]
            )
            basic_app.add_output_cluster(
                onoff
            )
            coordinator = Coordinator(dev, applications=[basic_app])
            monitor.attach(coordinator)
            monitor.start()
            coordinator.attach_callback(show)
            coordinator.start()

            print("[i] network formation !")
            coordinator.start_network()
            while True:
                input()
        except (KeyboardInterrupt, SystemExit):
            dev.close()

        except WhadDeviceNotFound:
            print('[e] Device not found')
            exit(1)
    else:
        print('Usage: %s [device]' % sys.argv[0])
