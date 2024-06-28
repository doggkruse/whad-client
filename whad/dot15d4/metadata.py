from whad.common.metadata import Metadata
from whad.dot15d4.utils.phy import channel_to_frequency
from whad.scapy.layers.dot15d4tap import Dot15d4TAP_Hdr, Dot15d4TAP_TLV_Hdr,\
    Dot15d4TAP_Received_Signal_Strength, Dot15d4TAP_Channel_Assignment, \
    Dot15d4TAP_Channel_Center_Frequency, Dot15d4TAP_Link_Quality_Indicator
from dataclasses import dataclass

@dataclass(repr=False)
class Dot15d4Metadata(Metadata):
    is_fcs_valid : bool = None
    lqi : int = None
    timestamp : int = None

    def convert_to_header(self):
        timestamp = None
        tlv = []
        if self.timestamp is not None:
            timestamp = self.timestamp
        if self.rssi is not None:
            tlv.append(Dot15d4TAP_TLV_Hdr()/Dot15d4TAP_Received_Signal_Strength(rss = self.rssi))
        if self.lqi is not None:
            tlv.append(Dot15d4TAP_TLV_Hdr()/Dot15d4TAP_Link_Quality_Indicator(lqi = self.lqi))
        if self.channel is not None:
            tlv.append(Dot15d4TAP_TLV_Hdr()/Dot15d4TAP_Channel_Assignment(channel_number=self.channel, channel_page=0))
            channel_frequency = channel_to_frequency(self.channel) * 1000
            tlv.append(Dot15d4TAP_TLV_Hdr()/Dot15d4TAP_Channel_Center_Frequency(channel_frequency=channel_frequency))
        return Dot15d4TAP_Hdr(data=tlv), timestamp

    @classmethod
    def convert_from_header(cls, pkt):
        rssi = None
        lqi = None
        channel = None
        for layer in pkt[Dot15d4TAP_Hdr].data:
            if Dot15d4TAP_Received_Signal_Strength in layer:
                rssi = layer.rss
            elif Dot15d4TAP_Link_Quality_Indicator in layer:
                lqi = layer.lqi
            elif Dot15d4TAP_Channel_Assignment in layer:
                channel = layer.channel_number
            else:
                pass
        return Dot15d4Metadata(
            rssi = int(rssi),
            lqi = lqi,
            channel = channel,
            timestamp = int(100000 * pkt.time)
        )

def generate_dot15d4_metadata(message):
    metadata = Dot15d4Metadata()

    if message.lqi is not None:
        metadata.lqi = message.lqi
    if message.rssi is not None:
        metadata.rssi = message.rssi
    metadata.channel = message.channel
    if message.timestamp is not None:
        metadata.timestamp = message.timestamp
    if message.fcs_validity is not None:
        metadata.is_fcs_valid = message.fcs_validity

    return metadata