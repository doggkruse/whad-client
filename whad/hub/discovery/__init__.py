"""WHAD Protocol Discovery message abstraction layer.
"""
from typing import List
from whad.hub.message import HubMessage
from whad.hub.message import pb_bind, Registry
from whad.hub import ProtocolHub

@pb_bind(ProtocolHub, name='discovery', version=1)
class Discovery(Registry):
    """WHAD Discovery message parser/factory.
    """

    VERSIONS = {}

    def __init__(self, version: int):
        self.proto_version = version

    @staticmethod
    def parse(proto_version: int, message) -> HubMessage:
        """Parses a WHAD discovery message as seen by protobuf
        """
        message_type = message.discovery.WhichOneof('msg')
        message_clazz = Discovery.bound(message_type, proto_version)
        return message_clazz.parse(proto_version, message)
    
    def createInfoQuery(self, proto_ver: int) -> HubMessage:
        """Create a device info query message.
        """
        return Discovery.bound('info_query', self.proto_version)(
            proto_ver=proto_ver
        )
    
    def createInfoResp(self, type: int, device_id: bytes, proto_min_ver: int,
                              max_speed: int, fw_author: bytes, fw_url: bytes,
                              fw_version_major: int, fw_version_minor: int,
                              fw_version_rev: int, capabilities: List[int]) -> HubMessage:
        """Create a device info query response message.
        """
        return Discovery.bound('info_resp', self.proto_version)(
            type=type, device_id=device_id, proto_min_ver=proto_min_ver,
            max_speed=max_speed, fw_author=fw_author, fw_url=fw_url,
            fw_version_major=fw_version_major, fw_version_min=fw_version_minor,
            fw_version_rev=fw_version_rev, capabilities=capabilities
        )
    
    def createDomainQuery(self, domain: int) -> HubMessage:
        """Create a domain info query message.
        """
        return Discovery.bound('domain_query', self.proto_version)(
            domain=domain
        )

    def createDomainResp(self, domain: int, supported_commands: int) -> HubMessage:
        """Create a device info response message
        """
        return Discovery.bound('domain_resp', self.proto_version)(
            domain=domain, supported_commands=supported_commands
        )
    
    def createSetSpeed(self, speed: int) -> HubMessage:
        """Create a speed update message.
        """
        return Discovery.bound('set_speed', self.proto_version)(
            speed=speed
        )
    
    def createResetQuery(self) -> HubMessage:
        """Create a device reset query.
        """
        return Discovery.bound('reset_query', self.proto_version)()
    
    def createDeviceReady(self) -> HubMessage:
        """Create a device ready response.
        """
        return Discovery.bound('ready_resp', self.proto_version)()
    
from .info import InfoQuery, InfoQueryResp
from .domain import DomainInfoQuery, DomainInfoQueryResp
from .speed import SetSpeed
from .reset import DeviceReady, ResetQuery

__all__ = [
    'Discovery',
    'InfoQuery',
    'InfoQueryResp',
    'DomainInfoQuery',
    'DomainInfoQueryResp',
    'SetSpeed',
    'DeviceReady',
    'ResetQuery'
]