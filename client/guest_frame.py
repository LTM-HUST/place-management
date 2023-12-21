from customtkinter import *
from tkinter import messagebox
from utils import recvall_str, sendall_str


class GuestFrame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        self.frame = None
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.login_nav()

    def login_nav(self):
        self.frame.grid_forget() if self.frame else None
        self.frame = LoginFrame(self)
        self.frame.configure(fg_color='transparent')
        self.frame.grid(row=0, column=0, sticky='nsew')

    def register_nav(self):
        self.frame.grid_forget()
        self.frame = RegisterFrame(self)
        self.frame.configure(fg_color='transparent')
        self.frame.grid(row=0, column=0, sticky='nsew')


class LoginFrame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.sock = master.sock
        self.sesssion_id = master.session_id
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.grid_columnconfigure(0, weight=1)

        self.title = CTkLabel(master=self, text='Login', font=CTkFont(size=18, weight='bold'))
        self.title.grid(row=0, column=0, sticky='ew', pady=(100, 20))

        self.username_label = CTkLabel(master=self, text='Username')
        self.username_entry = CTkEntry(master=self, textvariable=self.username_var)
        self.username_label.grid(row=1, column=0, sticky='w', padx=(200, 0))
        self.username_entry.grid(row=2, column=0, sticky='we', padx=(200, 200))

        self.password_label = CTkLabel(master=self, text='Password')
        self.password_entry = CTkEntry(master=self, textvariable=self.password_var, show='*')
        self.password_label.grid(row=3, column=0, sticky='w', padx=(200, 0))
        self.password_entry.grid(row=4, column=0, sticky='we', padx=(200, 200), pady=(0, 20))

        self.login_button = CTkButton(master=self, text='Login', command=self.login)
        self.login_button.grid(row=5, column=0, sticky='we', padx=(200, 200), pady=(10, 20))

        self.register_label = CTkLabel(master=self, text='New to the site? Register here', cursor='hand2')
        self.register_label.bind('<Button-1>', self.register_nav)
        self.register_label.grid(row=6, column=0, sticky='we')

    def login(self):
        message = {
            "task": "login",
            "content": {
                "username": self.username_var.get(),
                "password": self.password_var.get()
            }
        }
        sendall_str(self.sock, message, self.sesssion_id)

        resp = recvall_str(self.sock)
        if resp['success']:
            self.master.master.main_nav()
        else:
            if resp['code'] == 202:
                messagebox.showerror("Error", "Username or password is incorrect!")
            elif resp['code'] == 204:
                messagebox.showerror("Error", "This account is already logged in somewhere else!")

    def register_nav(self, event):
        self.master.register_nav()


class RegisterFrame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.sock = master.sock
        self.sesssion_id = master.session_id
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.retype_password_var = StringVar()
        self.grid_columnconfigure(0, weight=1)

        self.title = CTkLabel(master=self, text='Register', font=CTkFont(size=18, weight='bold'))
        self.title.grid(row=0, column=0, sticky='ew', pady=(100, 20))

        self.username_label = CTkLabel(master=self, text='Username')
        self.username_entry = CTkEntry(master=self, textvariable=self.username_var)
        self.username_label.grid(row=1, column=0, sticky='w', padx=(200, 0))
        self.username_entry.grid(row=2, column=0, sticky='we', padx=(200, 200))

        self.password_label = CTkLabel(master=self, text='Password')
        self.password_entry = CTkEntry(master=self, textvariable=self.password_var, show='*')
        self.password_label.grid(row=3, column=0, sticky='w', padx=(200, 0))
        self.password_entry.grid(row=4, column=0, sticky='we', padx=(200, 200))

        self.retype_password_label = CTkLabel(master=self, text='Re-type password')
        self.retype_password_entry = CTkEntry(master=self, textvariable=self.retype_password_var, show='*')
        self.retype_password_label.grid(row=5, column=0, sticky='w', padx=(200, 0))
        self.retype_password_entry.grid(row=6, column=0, sticky='we', padx=(200, 200), pady=(0, 20))

        self.register_button = CTkButton(master=self, text='Register', command=self.register)
        self.register_button.grid(row=7, column=0, sticky='we', padx=(200, 200), pady=(10, 20))

        self.register_label = CTkLabel(master=self, text='Already have an account? Login here', cursor='hand2')
        self.register_label.bind('<Button-1>', self.login_nav)
        self.register_label.grid(row=8, column=0, sticky='we')

    def register(self):
        message = {
            "task": "register",
            "content": {
                "username": self.username_var.get(),
                "password": self.password_var.get(),
                "retype_password": self.retype_password_var.get()
            }
        }
        sendall_str(self.sock, message, self.sesssion_id)

        resp = recvall_str(self.sock)
        if resp['success']:
            messagebox.showinfo("Success", "Register successfully!")
            self.master.login_nav()
        else:
            if resp['code'] == 201:
                messagebox.showerror("Error", "Username has been used!")
            elif resp['code'] == 203:
                messagebox.showerror("Error", "Password and retype password are not the same!")
            elif resp['code'] == 214:
                messagebox.showerror("Error", "Required field is missing!")

    def login_nav(self, event):
        self.master.login_nav()
