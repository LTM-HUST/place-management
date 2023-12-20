import socket
from _thread import *
import threading
import json

from sqlalchemy.orm import sessionmaker

from session import session_manager
from utils import recvall_str, sendall_str, write_log
from database import meta, conn, Base
from models import *

from friend_wrapper import FriendRoute
from notification_wrapper import NotificationRoute
from user_wrapper import UserRoute

TASK_FRIEND = ["send_friend_request", "accept_friend_request", "reject_friend_request",
               "delete_friend", "view_friend_list", "view_friend_request"]
TASK_NOTIFICATION = ["view_notification_list"]
TASK_USER = ["register", "login", "logout", "view_profile", "change_password"]

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


def task(sock, session_id, ip, port):

    while True:
        try:
            data = recvall_str(sock)
        except ConnectionResetError as e:
            write_log(ip, port, type="close")
            print(f"{ip}:{port} has been disconnected!")
            print(session_manager.sessions)
            session_manager.delete_session(session_id)
            print(session_manager.sessions)
            break

        if not data:
            write_log(ip, port, type="close")
            break
        write_log(ip, port, type="request", data=data)
        data = json.loads(data)
        print(data)
        task = data.get("task", None)
        if task in TASK_FRIEND:
            route = FriendRoute(session, session_id, data)
            response = route.response()
        elif task in TASK_NOTIFICATION:
            route = NotificationRoute(session, session_id, data)
            response = route.response()
        elif task in TASK_USER:
            route = UserRoute(session, session_id, data)
            response = route.response()
        else:
            response = {
                "success": False,
                "code": 300,
                "content": {}
            }
        sendall_str(sock, response)
        write_log(ip, port, type="response", data=response)

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
            write_log(addr[0], addr[1], type="connect")

            session_id = session_manager.create_session()
            sendall_str(connection, {"session_id": session_id})

            start_new_thread(task, (connection, session_id, addr[0], addr[1]))
        except KeyboardInterrupt:
            if connection:
                connection.close()
            break

    server_socket.close()
