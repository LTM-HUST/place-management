import socket
from _thread import *
import threading

from typing import Literal
import json

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
    
def send_friend_task(sock,
                     task: Literal["send_friend_request", "accept_friend_request", "reject_friend_request",
                                   "delete_friend", "view_friend_list", "view_friend_request"],
                     friend_id: int = None):
    if task in ["send_friend_request", "accept_friend_request", "reject_friend_request", "delete_friend"] and friend_id is None:
        raise ValueError("friend_id is required!")
    
    if task == "send_friend_request":
        content = {
            "target_friend_id": friend_id
        }
    elif task in ["accept_friend_request", "reject_friend_request"]:
        content = {
            "source_friend_id": friend_id
        }
    elif task == "delete_friend":
        content = {
            "friend_id": friend_id
        }
    else:
        content = {}
        
    message_json = {
        "task": task,
        "content": content
    }
    
    message = json.dumps(message_json)
    sendall_str(sock, message)
        