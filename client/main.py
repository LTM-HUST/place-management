import customtkinter
import os
from PIL import Image
from guest_frame import GuestFrame
from place_frame import PlaceFrame
from friend_frame import FriendFrame
from notification_frame import NotificationFrame
import socket
from utils import recvall_str, sendall_str, send_friend_task, send_notification_task

customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self, sock, session_id):
        super().__init__()
        
        self.sock = sock
        self.session_id = session_id
        self.title("Place Management")
        self.minsize(1300, 600)
    
        # set grid layout 1x2
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        
        # load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_app.png")), size=(30, 30))
        self.icon_place = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "map_trans.png")), size=(25, 27))
        self.icon_friend = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "team-icon.png")), size=(25, 27))
        self.icon_notification = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "notification_trans.png")), size=(25, 27))
        self.icon_profile = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "profile_trans.png")), size=(25, 27))
        
        # create navigation frame (sidebar)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        # self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Place App", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.place_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Place",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.icon_place, font=customtkinter.CTkFont(size=12, weight="bold"),
                                                   anchor="w", command=lambda: self.select_frame_by_name("place"))
        self.place_button.grid(row=1, column=0, sticky="ew")

        self.friend_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Friend",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.icon_friend, font=customtkinter.CTkFont(size=12, weight="bold"),
                                                      anchor="w", command=lambda: self.select_frame_by_name("friend"))
        self.friend_button.grid(row=2, column=0, sticky="ew")

        self.notification_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Notification",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.icon_notification, font=customtkinter.CTkFont(size=12, weight="bold"),
                                                      anchor="w", command=lambda: self.select_frame_by_name("notification"))
        self.notification_button.grid(row=3, column=0, sticky="ew")
        
        self.profile_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Profile",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.icon_profile, font=customtkinter.CTkFont(size=12, weight="bold"),
                                                      anchor="w", command=lambda: self.select_frame_by_name("profile"))
        self.profile_button.grid(row=4, column=0, sticky="ew")
        
        # create place frame
        self.place_frame = PlaceFrame(self)
        self.place_frame.grid_columnconfigure(0, weight=1)
        
        # create friend frame
        self.friend_frame = FriendFrame(self)
        self.friend_frame.grid_columnconfigure(0, weight=1)
        
        # create notification frame
        self.notification_frame = NotificationFrame(self)
        self.notification_frame.grid_columnconfigure(0, weight=1)
        
        # create profile frame
        self.profile_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.profile_frame.grid_columnconfigure(0, weight=1)
    
        
        # select default frame

        self.frame = GuestFrame(self)
        self.frame.grid(row=0, column=0, sticky="nsew")

        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.place_button.configure(fg_color=("gray75", "gray25") if name == "place" else "transparent")
        self.friend_button.configure(fg_color=("gray75", "gray25") if name == "friend" else "transparent")
        self.notification_button.configure(fg_color=("gray75", "gray25") if name == "notification" else "transparent")
        self.profile_button.configure(fg_color=("gray75", "gray25") if name == "profile" else "transparent")

        # show selected frame
        if name == "place":
            self.place_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.place_frame.grid_forget()
            
        if name == "friend":
            send_friend_task(self.sock, self.session_id, task="view_friend_list")
            all_friend_message = recvall_str(self.sock)
            send_friend_task(self.sock, self.session_id, task="view_friend_request")
            request_friend_message = recvall_str(self.sock)
            
            self.friend_frame = FriendFrame(self, all_friend_message, request_friend_message)
            self.friend_frame.grid_columnconfigure(0, weight=1)
            self.friend_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.friend_frame.grid_forget()
            
        if name == "notification":
            send_notification_task(self.sock, self.session_id)
            message = recvall_str(self.sock)
            self.notification_frame = NotificationFrame(self, message)
            self.notification_frame.grid_columnconfigure(0, weight=1)
            self.notification_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.notification_frame.grid_forget()
            
        if name == "profile":
            self.profile_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.profile_frame.grid_forget()
        

        
if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8000
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    
    data = recvall_str(s)
    session_id = data.get("session_id", None)
    if session_id is None:
        print("No connection!")
        s.close()
        exit(1)
    
    app = App(s, session_id)
    app.mainloop()