from customtkinter import *
from tkinter import messagebox
from utils import *

from response_code import code2message


class PasswordWindow(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id

        self.password_old = StringVar()
        self.password_new = StringVar()
        self.password_retype = StringVar()

        self.title("Change Password")
        self.geometry("400x300")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label_old = CTkLabel(master=self, text="Old password: ", font=CTkFont(size=15, weight='bold'))
        self.label_old.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_old = CTkEntry(master=self, placeholder_text="Enter your old password",
                                  width=200, textvariable=self.password_old, show='*')
        self.entry_old.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')

        self.label_new = CTkLabel(master=self, text="New password: ", font=CTkFont(size=15, weight='bold'))
        self.label_new.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_new = CTkEntry(master=self, placeholder_text="Enter your new password",
                                  width=200, textvariable=self.password_new, show='*')
        self.entry_new.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')

        self.label_retype = CTkLabel(master=self, text="Retype password: ", font=CTkFont(size=15, weight='bold'))
        self.label_retype.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry_retype = CTkEntry(master=self, placeholder_text="Retype your new password",
                                     width=200, textvariable=self.password_retype, show='*')
        self.entry_retype.grid(row=2, column=1, padx=5, pady=5, sticky='nswe')

        self.button_submit = CTkButton(master=self, text='Change Password', width=10, height=30, command=self.change_password)
        self.button_submit.grid(row=3, column=0, columnspan=2, sticky="ns", pady=20)

    def change_password(self):
        send_profile_task(self.sock, self.session_id, task="change_password",
                          old_password=self.password_old.get(),
                          new_password=self.password_new.get(),
                          retype_password=self.password_retype.get())
        response = recvall_str(self.sock)
        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            messagebox.showinfo("Success", message=code2message(response.get("code", None)))
            self.destroy()


class ProfileFrame(CTkFrame):
    def __init__(self, master, user_message=None):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        self.columnconfigure(0, weight=1)

        self.username = ""
        if user_message:
            self.username = user_message.get("content", dict()).get("username", "")

        # General widgets
        self.label = CTkLabel(master=self, text="Profile Management", font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky='w')

        self.label_name = CTkLabel(master=self, text="Username: ", font=CTkFont(size=15, weight='normal'))
        self.label_name.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky='w')
        self.label_username = CTkLabel(master=self, text=self.username, font=CTkFont(size=15, weight='normal'))
        self.label_username.grid(row=2, column=0, padx=5, pady=5, columnspan=3, sticky='w')

        self.button_change_pw = CTkButton(
            master=self, text='Change Password', width=10, height=30, command=self.password_toplevel)  # overwrite CTkButton default width and height
        self.button_change_pw.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        self.button_logout = CTkButton(
            master=self, text='Logout', width=10, height=30, command=self.logout)  # overwrite CTkButton default width and height
        self.button_logout.grid(row=3, column=2, padx=20, pady=5, sticky='e')

        self.toplevel_window = None

    def password_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = PasswordWindow(self)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def logout(self):
        send_profile_task(self.sock, self.session_id, task="logout")
        response = recvall_str(self.sock)
        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            self.master.master.guest_nav()
            messagebox.showinfo("Success", message=code2message(response.get("code", None)))       
