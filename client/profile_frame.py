from customtkinter import *

class ProfileFrame(CTkFrame):
    def __init__(self, master, user_message=None):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(2, weight=1)
        
        self.username = "Huy"
        if user_message:
            self.username = user_message.get("username", "")
            
        # General widgets
        self.label = CTkLabel(master=self, text="Profile Management", font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky='w')
        
        self.label_name = CTkLabel(master=self, text="Username: ", font=CTkFont(size=15, weight='normal'))
        self.label_name.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky='w')
        self.label_username = CTkLabel(master=self, text=self.username, font=CTkFont(size=15, weight='normal'))
        self.label_username.grid(row=2, column=0, padx=5, pady=5, columnspan=3, sticky='w')

        self.button_change_pw = CTkButton(
            master=self, text='Change Password', width=10, height=30) # overwrite CTkButton default width and height
        self.button_change_pw.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        self.button_logout = CTkButton(
            master=self, text='Logout', width=10, height=30) # overwrite CTkButton default width and height
        self.button_logout.grid(row=3, column=2, padx=20, pady=5, sticky='e')
        # self.add_button.bind('<Button-1>', self.on_add_button_click)
            