import socket
from _thread import *
import threading

def recvall(sock):
    # Helper function to recv all streaming data using \r\n
    data = ""
    condition = True
    while condition:
        packet = sock.recv(1024)
        if not packet:
            return data
        packet_str = packet.decode('utf8')
        if "\r\n" in packet_str:
            condition = False
        data += packet.decode('utf8')
    return data