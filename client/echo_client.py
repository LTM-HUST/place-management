
# Import socket module
import socket
from utils import recvall_str, sendall_str
 
 
def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
 
    # Define the port on which you want to connect
    port = 8000
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    s.connect((host,port))
 
    # message you send to server
    message = {
        "task": "send_friend_request",
        "content": {
            "target_friend_id": 3
        }
    }
    while True:
 
        # message sent to server
        sendall_str(s, message)
 
        # message received from server
        data = recvall_str(s)
 
        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', data)
        print("Length: ", len(data))
 
        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()
 
if __name__ == '__main__':
    Main()