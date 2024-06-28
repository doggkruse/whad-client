"""WHAD server tool

This utility implements a server module, allowing to create a TCP proxy
which can be used to access a device remotely.
"""
import logging
from prompt_toolkit import print_formatted_text, HTML
import time
from whad.common.monitors.pcap import PcapWriterMonitor
from whad.cli.app import CommandLinePipe, CommandLineApp
from scapy.all import *
from whad.common.pcap import extract_pcap_metadata
import sys, os, stat
from whad.device import WhadDevice
from whad.exceptions import WhadDeviceNotFound, WhadDeviceNotReady
from whad.tools.wsniff import list_implemented_sniffers, build_configuration_from_args, WhadSniffApp, WhadDomainSubParser

logger = logging.getLogger(__name__)

class WhadPlayApp(WhadSniffApp):#CommandLineApp):
    #build_subparsers = WhadSniffApp.build_subparsers

    def __init__(self):
        """Application uses an interface and has commands.
        """
        super().__init__(
            description='WHAD play tool',
            interface=False,
            pcap_argument=True
        )


    def infer_domain_from_pcap(self):
        self.pcap_file = None
        index_pcap_file = None
        override_domain = False
        for i in range(len(sys.argv)):
            if ".pcap" in sys.argv[i]:
                self.pcap_file = sys.argv[i]
                index_pcap_file = i
            elif sys.argv[i] in list_implemented_sniffers().keys():
                override_domain = True
        if index_pcap_file is not None and not override_domain:
            domain = extract_pcap_metadata(self.pcap_file)
            sys.argv.insert(index_pcap_file + 1, domain)

    def pre_run(self):
        """Pre-run operations: configure scapy theme.
        """

        # If no color is not selected, configure scapy color theme
        self.infer_domain_from_pcap()
        super().pre_run()


        if self.args.pcap is not None:
            self.interface = WhadDevice.create("pcap:" + self.args.pcap)

        if not self.args.nocolor:
            conf.color_theme = BrightTheme()

def wplay_main():
    app = WhadPlayApp()
    app.run()