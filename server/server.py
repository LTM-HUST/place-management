import socket
from _thread import *
import threading
import json
from sqlalchemy.orm import sessionmaker

from utils import recvall_str, sendall_str
from database import meta, conn, Base
from models import *
from friend_wrapper import FriendRoute

TASK_FRIEND = ["send_friend_request", "accept_friend_request", "reject_friend_request", 
               "delete_friend", "view_friend_list", "view_friend_request"]

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def echo(sock):
    while True:
        data = recvall_str(sock)
        if not data:
            break
        data = "Accept: " + data
        sendall_str(sock, data)
        
    sock.close()
    
def task(sock):
    user_id = 11
    while True:
        data = recvall_str(sock)
        if not data:
            break
        data = json.loads(data)
        task = data.get("task", None)
        if task in TASK_FRIEND:
            route = FriendRoute(session, user_id, data)
            response = route.response()
        sendall_str(sock, response)
    
    sock.close()
            

if __name__ == '__main__':
    host = ""
    port = 8000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print("socket binded to port", port)
    
    server_socket.listen(5)
    print("socket is listening")
    
    while True:
        connection = None
        try:
            connection, addr = server_socket.accept()
            
            print('Connected to :', addr[0], ':', addr[1])
            
            start_new_thread(task, (connection,))
        except KeyboardInterrupt:
            if connection:
                connection.close()
            break
    
    server_socket.close()
    