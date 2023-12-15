import socket
from _thread import *
import threading
from utils import recvall_str, sendall_str

def echo(sock):
    while True:
        data = recvall_str(sock)
        if not data:
            break
        data = "Accept: " + data
        sendall_str(sock, data)
        
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
            
            start_new_thread(echo, (connection,))
        except KeyboardInterrupt:
            if connection:
                connection.close()
            break
    
    server_socket.close()
    