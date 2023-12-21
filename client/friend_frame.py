from customtkinter import *
from PIL import Image

from utils import recvall_str, sendall_str, send_friend_task

friends = [
    {
        "id": 123,
        "username": "hieu"
    },
    {
        "id": 124,
        "username": "huy"
    },
    {
        "id": 125,
        "username": "hoang"
    },
    {
        "id": 126,
        "username": "tien"
    },
]

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

class FriendFrame(CTkScrollableFrame):

    def __init__(self, master, all_friend_message=None, request_friend_message=None):
        super().__init__(master)
        
        self.sock = master.sock
        self.session_id = master.session_id
        self.columnconfigure(0, weight=1)
        
        self.all_friends = None
        self.request_friends = None
        if all_friend_message:
            self.all_friends = all_friend_message.get("content", None)
            self.request_friends = request_friend_message.get("content", None)

        # General widgets
        self.label = CTkLabel(master=self, text='Friend Management', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w')

        self.tabview = CTkTabview(master=self, anchor='w')
        self.tabview.add('Friend List')
        self.tabview.add('Friend Request')
        self.tabview.grid(row=1, column=0, columnspan=2, sticky='ew') # stretch frame to fill master

        self.friend_list_tab = self.tabview.tab('Friend List')
        self.friend_list_tab.grid_columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
        self.friend_request_tab = self.tabview.tab('Friend Request')
        self.friend_request_tab.grid_columnconfigure(0, weight=1)

        # Friend list widget
        if (self.all_friends):
            for index, friend in enumerate(self.all_friends):
                friend_item = FriendItem(master=self.friend_list_tab, friend=friend, request_friend=False)
                friend_item.grid(row=index, column=0, sticky='ew') # stretch frame to fill master

        # Friend request widget
        if (self.request_friends):
            for index, friend in enumerate(self.request_friends):
                friend_item = FriendItem(master=self.friend_request_tab, friend=friend, request_friend=True)
                friend_item.grid(row=index, column=0, sticky='ew')


class FriendItem(CTkFrame):

    def __init__(self, master, friend, request_friend=True):
        super().__init__(master)
        self.sock = self.master.master.master.sock
        self.session_id = self.master.master.master.session_id
        self.friend = friend
        self.request_friend = request_friend

        # General configuration
        self.columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)

        # Images
        self.accept_icon = CTkImage(Image.open(os.path.join(image_path, 'accept_icon.png')), size=(30, 30))
        self.reject_icon = CTkImage(Image.open(os.path.join(image_path, 'reject_icon.png')), size=(30, 30))
        self.delete_icon = CTkImage(Image.open(os.path.join(image_path, 'delete_icon.png')), size=(30, 30))

        # Widgets
        friend_name_label = CTkLabel(master=self, text=friend['username'])
        friend_name_label.grid(row=0, column=0, sticky='w')
        space_label = CTkLabel(master=self, text=" ")
        space_label.grid(row=1, column=0, sticky='w')

        if request_friend:
            accept_button = CTkButton(master=self, text='', image=self.accept_icon, width=30, height=30, 
                                      fg_color='transparent', command=self.accept_friend)
            accept_button.grid(row=0, column=1, rowspan=2, sticky='e')
            reject_button = CTkButton(master=self, text='', image=self.reject_icon, width=30, height=30, 
                                      fg_color='transparent', command=self.reject_friend)
            reject_button.grid(row=0, column=2, rowspan=2, sticky='e')
        else:
            delete_button = CTkButton(master=self, text='', image=self.delete_icon, width=30, height=30, 
                                      fg_color='transparent', command=self.delete_friend)
            delete_button.grid(row=0, column=1, rowspan=2, sticky='e')

    def on_enter(self, event):
        self.configure(fg_color='gray')

    def on_leave(self, event):
        self.configure(fg_color='transparent')

    def on_click(self, event):
        # Modify to render a new frame with the place details
        print(f"Friend ID: {self.friend['id']}")
        print(f"Friend name: {self.friend['username']}")
        
    def accept_friend(self):
        send_friend_task(self.sock, self.session_id, task="accept_friend_request", friend_id=self.friend["id"])
        response = recvall_str(self.sock)
        if len(response) == 0:
            print("No connection!")
        elif response.get("success"):
            print(f"{self.friend['username']} is now your friend!")
            self.destroy()
        else:
            print("Not successful")
        
    def reject_friend(self):
        send_friend_task(self.sock, self.session_id, task="reject_friend_request", friend_id=self.friend["id"])
        response = recvall_str(self.sock)
        if len(response) == 0:
            print("No connection!")
        elif response.get("success"):
            print(f"{self.friend['username']} is rejected!")
            self.destroy()
        else:
            print("Not successful")
        
    def delete_friend(self):
        send_friend_task(self.sock, self.session_id, task="delete_friend", friend_id=self.friend["id"])
        response = recvall_str(self.sock)
        if len(response) == 0:
            print("No connection!")
        elif response.get("success"):
            print(f"{self.friend['username']} is no longer in your friend list!")
            self.destroy()
        else:
            print("Not successful")
