from whad.unifying import Dongle
from whad.device import WhadDevice
from whad.exceptions import WhadDeviceNotFound
from whad.scapy.layers.esb import *
from whad.scapy.layers.unifying import *
from scapy.compat import raw
import sys,time
from whad.esb.esbaddr import ESBAddress

def show(pkt):
    print(pkt.metadata, repr(pkt))

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # Retrieve target interface
        interface = sys.argv[1]

        # Connect to target device and performs discovery
        try:
            dev = WhadDevice.create(interface)

            connector = Dongle(dev)
            connector.start()
            #connector.attach_callback(show, on_reception=True, on_transmission=False)
            connector.address = ESBAddress("9b:0a:90:42:00")#"9b:0a:90:42:00"
            connector.channel = 5
            input()
            connector.address = "9b:0a:90:42:97"#"9b:0a:90:42:96"

            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            connector.stop()
            dev.close()

        except WhadDeviceNotFound:
            print('[e] Device not found')
            exit(1)
    else:
        print('Usage: %s [device]' % sys.argv[0])
