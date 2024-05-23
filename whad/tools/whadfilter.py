"""WHAD server tool

This utility implements a server module, allowing to create a TCP proxy
which can be used to access a device remotely.
"""
import logging
from prompt_toolkit import print_formatted_text, HTML
import time
from whad.tools.whadsniff import display_packet
from whad.cli.app import CommandLinePipe
from scapy.all import *
from whad.common.ipc import IPCPacket
import sys
from whad.exceptions import WhadDeviceNotFound, WhadDeviceNotReady
logger = logging.getLogger(__name__)

class WhadFilterApp(CommandLinePipe):

    def __init__(self):
        """Application uses an interface and has commands.
        """
        super().__init__(
            description='WHAD extraction tool',
            interface=True,
            commands=False
        )

        self.add_argument(
            'filter',
            help='filter to evaluate',
            nargs = "*"
        )


        self.add_argument(
            '-o',
            '--or',
            dest='any',
            action="store_true",
            default=False,
            help='xor between filters'
        )
        self.add_argument(
            '-e',
            '--invert',
            dest='invert',
            action="store_true",
            default=False,
            help='invert filter'
        )

        self.add_argument(
            '-d',
            '--debug',
            dest='debug',
            action="store_true",
            default=False,
            help='debug filter'
        )


    filter_template = "lambda p : {}"


    def run(self):
        # Launch pre-run tasks
        self.pre_run()
        try:
            while True:
                dump = sys.stdin.readline()
                data = IPCPacket.from_dump(dump.replace("\n", ""))

                accept_list = []
                for filter in self.args.filter:
                    filter_func = self.filter_template.format(filter)

                    try:
                        if eval(filter_func)(data):
                            accept = True
                        else:
                            accept = False
                    except:
                        accept = False

                    accept_list.append(accept)

                aggregation_func = any if self.args.any else all


                result = aggregation_func(accept_list)
                if self.args.invert:
                    result = not result

                if self.args.debug:
                    print("[i] evaluate {} -> {}".format(("or" if self.args.any else "and".join(self.args.filter)) + ("(inverted)" if self.args.invert else ""), result))
                if result or self.args.debug:
                    display_packet(data, show_metadata=True, format="repr")
        except:
            pass

        # Launch post-run tasks
        self.post_run()


def whadfilter_main():
    app = WhadFilterApp()
    app.run()
