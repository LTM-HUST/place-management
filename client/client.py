from customtkinter import *
import socket
from guest_frame import GuestFrame
from place_frame import PlaceFrame
from friend_frame import FriendFrame
from notification_frame import NotificationFrame
from profile_frame import ProfileFrame
from utils import recvall_str
from PIL import Image


set_appearance_mode("light")
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")


class App(CTk):
    def __init__(self, sock, session_id):
        super().__init__()
        self.sock = sock
        self.session_id = session_id
        self.title("Place Management")
        self.minsize(1300, 600)
        self.frame = None

        self.guest_nav()

    def guest_nav(self):
        self.frame.grid_forget() if self.frame else None
        self.frame = GuestFrame(self)
        self.frame.configure(fg_color='transparent')
        self.frame.grid(row=0, column=0, sticky='nsew')

    def main_nav(self):
        self.frame.grid_forget()
        self.frame = MainFrame(self)
        self.frame.configure(fg_color='transparent')
        self.frame.grid(row=0, column=0, sticky='nsew')


class MainFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        master.grid_columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Load images
        self.logo_image = CTkImage(Image.open(os.path.join(image_path, "logo_app.png")), size=(30, 30))
        self.icon_place = CTkImage(light_image=Image.open(os.path.join(image_path, "map_trans.png")), size=(25, 27))
        self.icon_friend = CTkImage(light_image=Image.open(os.path.join(image_path, "team-icon.png")), size=(25, 27))
        self.icon_notification = CTkImage(light_image=Image.open(os.path.join(image_path, "notification_trans.png")), size=(25, 27))
        self.icon_profile = CTkImage(light_image=Image.open(os.path.join(image_path, "profile_trans.png")), size=(25, 27))

        # Create navigation frame (sidebar)
        self.navigation_frame = CTkFrame(master=self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')

        self.navigation_frame_label = CTkLabel(self.navigation_frame, text=" Place App", image=self.logo_image,
                                               compound="left", font=CTkFont(size=18, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.place_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Place",
                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                      image=self.icon_place, font=CTkFont(size=12, weight="bold"),
                                      anchor="w", command=lambda: self.place_nav())
        self.place_button.grid(row=1, column=0, sticky="ew")

        self.friend_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Friend",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       image=self.icon_friend, font=CTkFont(size=12, weight="bold"),
                                       anchor="w", command=lambda: self.friend_nav())
        self.friend_button.grid(row=2, column=0, sticky="ew")

        self.notification_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Notification",
                                             fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                             image=self.icon_notification, font=CTkFont(size=12, weight="bold"),
                                             anchor="w", command=lambda: self.notification_nav())
        self.notification_button.grid(row=3, column=0, sticky="ew")

        self.profile_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Profile",
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        image=self.icon_profile, font=CTkFont(size=12, weight="bold"),
                                        anchor="w", command=lambda: self.profile_nav())
        self.profile_button.grid(row=4, column=0, sticky="ew")

        # Creat content frame
        self.content_frame = None
        self.place_nav()

    def place_nav(self):
        self.content_frame.grid_forget() if self.content_frame else None
        self.content_frame = PlaceFrame(self)
        self.content_frame.configure(fg_color='transparent')
        self.content_frame.grid(row=0, column=1, sticky='nsew')

    def friend_nav(self):
        self.content_frame.grid_forget()
        self.content_frame = FriendFrame(self)
        self.content_frame.configure(fg_color='transparent')
        self.content_frame.grid(row=0, column=1, sticky='nsew')

    def notification_nav(self):
        self.content_frame.grid_forget()
        self.content_frame = NotificationFrame(self)
        self.content_frame.configure(fg_color='transparent')
        self.content_frame.grid(row=0, column=1, sticky='nsew')

    def profile_nav(self):
        self.content_frame.grid_forget()
        self.content_frame = ProfileFrame(self)
        self.content_frame.configure(fg_color='transparent')
        self.content_frame.grid(row=0, column=1, sticky='nsew')


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = recvall_str(s)
    session_id = data.get("session_id", None)
    if session_id is None:
        print("No connection!")
        s.close()
        exit(1)

    app = App(s, session_id)
    app.mainloop()
