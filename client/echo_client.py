
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
    message1 = {
        "task": "send_friend_request",
        "content": {
            "target_friend_id": 5
        }
    }
    message2 = {
        "task": "accept_friend_request",
        "content": {
            "source_friend_id": 1
        }
    }
    message3 = {
        "task": "reject_friend_request",
        "content": {
            "source_friend_id": 4
        }
    }
    message4 = {
        "task": "delete_friend",
        "content": {
            "friend_id": 3
        }
    }
    message5 = {
        "task": "view_friend_list",
        "content": {}
    }
    message6 = {
        "task": "view_friend_request",
        "content": {}
    }
    message7 = {
        "task": "view_notification_list",
        "content": {}
    }
    message8 = {
        "task": "register",
        "content": {
            "username": "nguyenhieu",
            "password": "111111",
            "retype_password": "111111"
        }
    }

    message9 = {
        "task": "login",
        "content": {
            "username": "nguyenhieu",
            "password": "111111"
        }
    }

    message10 = {
        "task": "logout",
        "content": {}
    }

    message11 = {
        "task": "view_profile",
        "content": {}
    }

    message12 = {
        "task": "change_password",
        "content": {
            "old_password": "222222",
            "new_password": "111111",
            "retype_password": "111111"
        }
    }

    
    while True:
        # message sent to server
        for message in [message8, message11, message12, message10, message9]:
            sendall_str(s, message)
    
            # message received from server
            data = recvall_str(s) 
    
            # print the received message
            # here it would be a reverse of sent message
            print('Received from the server:', data)
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