import socket
from _thread import *
import threading

from typing import Literal, Union
import json

data_client = ""

def recvall_str(sock):
    # Helper function to recv all streaming data using \r\n
    
    global data_client
    condition = True   
    while condition:
        packet = sock.recv(1024)
        if not packet:
            condition = False
        packet_str = packet.decode('utf8')
        if "\r\n" in packet_str:
            packet_str_list = packet_str.split("\r\n")
            data_client += packet_str_list[0]
            return_data = data_client
            data_client = ""
            for i in range(1, len(packet_str_list)):
                data_client += packet_str_list[i]
            break
        data_client += packet.decode('utf8')
    return json.loads(str(return_data))

def sendall_str(sock, message: Union[dict, str], session_id=None):
    if isinstance(message, dict):
        if session_id and message.get("session_id", None):
            message["session_id"] = session_id
        message = json.dumps(message)
    
    if not message.endswith("\r\n"):
        message += "\r\n"
    sock.sendall(message.encode("utf-8"))
    
def send_friend_task(sock,
                     session_id,
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
        "session_id": session_id,
        "task": task,
        "content": content
    }
    
    message = json.dumps(message_json)
    sendall_str(sock, message)
    
def send_notification_task(sock,
                            session_id,
                            task: Literal["view_notification_list"] = "view_notification_list"):
    if task in ["view_notification_list"]:
        content = {}
        
    message_json = {
        "session_id": session_id,
        "task": task,
        "content": content
    }
    
    message = json.dumps(message_json)
    sendall_str(sock, message)
    
def send_profile_task(sock, session_id, task: Literal["view_profile, change_password"], 
                      old_password: str = "", 
                      new_password: str = "", 
                      retype_password: str = ""):
    if task == "view_profile":
        content = {}
    if task == "change_password":
        content = {
            "old_password": old_password,
            "new_password": new_password,
            "retype_password": retype_password
        }
        
    message_json = {
        "session_id": session_id,
        "task": task,
        "content": content
    }
        
    message = json.dumps(message_json)
    sendall_str(sock, message)   