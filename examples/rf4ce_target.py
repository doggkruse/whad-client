from whad.device import WhadDevice
from whad.rf4ce import Target, Dot15d4Address
from whad.common.monitors import WiresharkMonitor
from whad.exceptions import WhadDeviceNotFound
from scapy.compat import raw
from random import randint
import sys
import logging

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

            target = Target(dev)
            target.set_channel(15)
            monitor.attach(target)
            monitor.start()
            target.start()

            target.auto_discovery()
            input()
            # temp: let's start a pairing resp here
            target.stack.get_layer('nwk').get_service('management').pair_response(
                pan_id=0x1234,
                destination_address=Dot15d4Address("C4:19:D1:AE:35:0D:70:02").value,
                application_capability=0,
                accept=True,
                list_of_device_types=[9],
                list_of_profiles=[192],
                pairing_reference=pairing_reference
            )
            #target.discovery_response(True, destination_address="C4:19:D1:AE:35:0D:70:02")
        except (KeyboardInterrupt, SystemExit):
            dev.close()

        except WhadDeviceNotFound:
            print('[e] Device not found')
            exit(1)
    else:
        print('Usage: %s [device]' % sys.argv[0])
