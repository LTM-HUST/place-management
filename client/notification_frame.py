from customtkinter import *
from PIL import Image

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

class NotificationFrame(CTkScrollableFrame):

    def __init__(self, master, message=None):
        super().__init__(master)
        
        self.session_id = master.session_id
        self.notifications = None
        self.grid_columnconfigure(0, weight=1)
        if message:
            self.notifications = message.get("content", None)
        
        # General widgets
        self.label = CTkLabel(master=self, text='Notification Management', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, pady=15, sticky='nw')

        # Notification list widget
        if self.notifications:
            for index, notification in enumerate(self.notifications):
                notification_item = NotificationItem(master=self, notification=notification)
                notification_item.grid(row=index+1, column=0, sticky='ew') # stretch frame to fill master


class NotificationItem(CTkFrame):

    def __init__(self, master, notification, **kwargs):
        super().__init__(master)
        self.notification = notification
        self.color = "transparent" if notification["read"] else "#b4cbf0"
        self.message = f"{notification['username']} tagged you in {notification['place_name']}"
        self.message_time = notification['time']

        # General configuration
        self.configure(fg_color=self.color)
        self.columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
        self.columnconfigure(1, weight=1)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Button-1>', self.on_click)

        # Widgets
        message_label = CTkLabel(master=self, text=self.message)
        message_label.grid(row=0, column=0, sticky='nw')
        message_time_label = CTkLabel(master=self, text=self.message_time)
        message_time_label.grid(row=0, column=1, sticky='se')

    def on_enter(self, event):
        self.configure(fg_color='gray')

    def on_leave(self, event):
        self.configure(fg_color=self.color)

    def on_click(self, event):
        # Modify to render a new frame with the place details
        print(f"Message: {self.message}")
        print(f"Time: {self.message_time}")
        print(self.master.session_id)
        
