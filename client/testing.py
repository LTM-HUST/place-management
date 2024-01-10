import json
import socket
from utils import recvall_str, sendall_str

initial_login = [
    {
        'task': 'register',
        'content': {
            'username': 'huy',
            'password': '123456',
            'retype_password': '111111'
        }
    },
    {
        'task': 'register',
        'content': {
            'username': 'huy',
            'password': '',
            'retype_password': '123456'
        }
    },
    {
        'task': 'register',
        'content': {
            'username': 'huy',
            'password': '123456',
            'retype_password': '123456'
        }
    },
    {
        'task': 'register',
        'content': {
            'username': 'huy',
            'password': '123456789',
            'retype_password': '123456789'
        }
    },
    {
        'task': 'login',
        'content': {
            'username': 'huy',
            'password': '123456a'
        }
    },
    {
        'task': 'login',
        'content': {
            'username': 'huy',
            'password': '123456'
        }
    },
    {
        'task': 'login',
        'content': {
            'username': 'huy',
            'password': '123456'
        }
    },
    {
        'task': 'view_profile',
        'content': {}
    },
    {
        'task': 'change_password',
        'content': {
            'old_password': '123456',
            'new_password': '123456789',
            'retype_password': '1'
        }
    },
    {
        'task': 'change_password',
        'content': {
            'old_password': '1',
            'new_password': '123456789',
            'retype_password': '123456789'
        }
    },
    {
        'task': 'change_password',
        'content': {
            'old_password': '123456',
            'new_password': '123456789',
            'retype_password': '123456789'
        }
    },
    {
        'task': 'logout',
        'content': {}
    }
]

friend_test = [
    {
        'task': 'login',
        'content': {
            'username': 'a',
            'password': 1
        }
    },
    {
        'task': 'view_friend_list',
        'content': {}
    },
    {
        'task': 'view_friend_request',
        'content': {}
    },
    {
        'task': 'send_friend_request',
        'content': {
            'target_friend_name': 'dfkdfk'
        }
    },
    {
        'task': 'send_friend_request',
        'content': {
            'target_friend_name': 'ewald69'
        }
    },
    {
        'task': 'send_friend_request',
        'content': {
            'target_friend_name': 'huy'
        }
    },
    {
        'task': 'accept_friend_request',
        'content': {
            'source_friend_id': 22
        }
    },
    {
        'task': 'accept_friend_request',
        'content': {
            'source_friend_id': 25
        }
    },
    {
        'task': 'accept_friend_request',
        'content': {
            'source_friend_id': 4
        }
    },
    {
        'task': 'reject_friend_request',
        'content': {
            'source_friend_id': 22
        }
    },
    {
        'task': 'reject_friend_request',
        'content': {
            'source_friend_id': 25
        }
    },
    {
        'task': 'reject_friend_request',
        'content': {
            'source_friend_id': 5
        }
    },
    {
        'task': 'delete_friend',
        'content': {
            'friend_id': 22
        }
    },
    {
        'task': 'delete_friend',
        'content': {
            'friend_id': 25
        }
    },
    {
        'task': 'delete_friend',
        'content': {
            'friend_id': 4
        }
    }
]


def main():
    host = '127.0.0.1'
    port = 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    first_resp = recvall_str(sock)
    session_id = first_resp['session_id']

    with open('./client/testing.txt', 'r') as file:
        for line in file:
            message = json.loads(line)
            message['session_id'] = session_id
            sendall_str(sock, message)
            print(recvall_str(sock))

    sock.close()


if __name__ == '__main__':
    main()
