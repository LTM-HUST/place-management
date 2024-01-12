import json
import socket
from utils import recvall_str, sendall_str


def main():
    host = '127.0.0.1'
    port = 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    first_resp = recvall_str(sock)
    session_id = first_resp['session_id']

    # with open('./client/testing_send.txt', 'r') as file:
    #     for line in file:
    #         try:
    #             message = json.loads(line)
    #             message['session_id'] = session_id
    #         except json.decoder.JSONDecodeError:
    #             message = line

    #         sendall_str(sock, message)
    #         print(recvall_str(sock))

    message = '{"session_id": "", "task": "register", "content": {"username": "huy", "password": "123456", "retype_password": "111111"}}\r\n{"session_id": "", "task": "register", "content": {"username": "huy", "password": "", "retype_password": "123456"}}\r\n'
    sock.sendall(message.encode("utf-8"))
    packet = sock.recv(1024)
    print(packet)
    packet = sock.recv(1024)
    print(packet)

    sock.close()


if __name__ == '__main__':
    main()
