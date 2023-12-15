import socket
from _thread import *
import threading

def recvall_str(sock):
    # Helper function to recv all streaming data using \r\n
    data = ""
    condition = True
    while condition:
        packet = sock.recv(1024)
        if not packet:
            return data
        packet_str = packet.decode('utf8')
        if packet_str.endswith("\r\n"):
            condition = False
        data += packet.decode('utf8')
    return str(data[:-2])

def sendall_str(sock, message):
    message += "\r\n"
    sock.sendall(message.encode("utf-8"))