from customtkinter import *
from PIL import Image

from utils import *
from tkinter import messagebox

from response_code import code2message


image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')


class PlaceFrame(CTkScrollableFrame):

    def __init__(self, master, places_message, my_places_message, liked_places_message):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        self.places_message = places_message
        self.my_places_message = my_places_message
        self.liked_places_message = liked_places_message

        self.columnconfigure(0, weight=1)  # stretch the first column to fill the whole remaining space
        self.current_frame = ViewAllPlaceFrame(master=self)  # init current_frame as ViewAllPlaceFrame
        self.current_frame.grid(row=0, column=0, sticky='nsew')  # stretch frame to fill master
        self.current_frame.grid_columnconfigure(0, weight=1)  # stretch the first column to fill the whole remaining space

    """
    All the following methods are used to switch between frames.
    What they do is to destroy the current frame and create a new one.
    """

    def view_all_places(self):
        self.current_frame.destroy()
        self.current_frame = ViewAllPlaceFrame(master=self)
        self.current_frame.grid(row=0, column=0, sticky='nsew')
        self.current_frame.grid_columnconfigure(0, weight=1)

    def view_place_detail(self, id, owned):
        send_place_task(self.sock, self.session_id, task="view_place_detail", id=id)
        response = recvall_str(self.sock)
        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            self.current_frame.destroy()
            self.current_frame = ViewPlaceDetailFrame(master=self, place=response['content'], owned=owned)
            self.current_frame.grid(row=0, column=0, sticky='nsew')
            self.current_frame.grid_columnconfigure(0, weight=1)

    def create_place(self):
        send_place_task(self.sock, self.session_id, task="view_categories")
        categories_resp = recvall_str(self.sock)
        send_friend_task(self.sock, self.session_id, task="view_friend_list")
        friends_resp = recvall_str(self.sock)

        self.current_frame.destroy()
        self.current_frame = CreatePlaceFrame(master=self, categories=categories_resp['content'], friends=friends_resp['content'])
        self.current_frame.grid(row=0, column=0, sticky='nsew')
        self.current_frame.grid_columnconfigure(0, weight=1)

    def update_place(self, id):
        send_place_task(self.sock, self.session_id, task="view_place_detail", id=id)
        response = recvall_str(self.sock)
        send_place_task(self.sock, self.session_id, task="view_categories")
        categories_resp = recvall_str(self.sock)
        send_friend_task(self.sock, self.session_id, task="view_friend_list")
        friends_resp = recvall_str(self.sock)

        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            self.current_frame.destroy()
            self.current_frame = UpdatePlaceFrame(master=self, place=response['content'], categories=categories_resp['content'], friends=friends_resp['content'])
            self.current_frame.grid(row=0, column=0, sticky='nsew')
            self.current_frame.grid_columnconfigure(0, weight=1)


class ViewAllPlaceFrame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id

        # Images
        self.add_icon = CTkImage(Image.open(os.path.join(image_path, 'add_icon.png')), size=(30, 30))
        self.edit_icon = CTkImage(Image.open(os.path.join(image_path, 'edit_icon.png')), size=(30, 30))
        self.delete_icon = CTkImage(Image.open(os.path.join(image_path, 'delete_icon.png')), size=(30, 30))

        # General widgets
        self.label = CTkLabel(master=self, text='Place management', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w')

        self.add_button = CTkButton(
            master=self, text='', image=self.add_icon, width=30, height=30, fg_color='transparent')  # overwrite CTkButton default width and height
        self.add_button.grid(row=0, column=1, sticky='e')
        self.add_button.bind('<Button-1>', self.on_add_button_click)

        self.tabview = CTkTabview(master=self, anchor='w', height=20)  # overwrite CTkTabview default height
        self.tabview.add('All places')
        self.tabview.add('My created places')
        self.tabview.add('Liked places')
        self.tabview.grid(row=1, column=0, columnspan=2, sticky='ew')

        self.all_places_tab = self.tabview.tab('All places')
        self.all_places_tab.grid_columnconfigure(0, weight=1)
        self.my_created_places_tab = self.tabview.tab('My created places')
        self.my_created_places_tab.grid_columnconfigure(0, weight=1)
        self.liked_places_tab = self.tabview.tab('Liked places')
        self.liked_places_tab.grid_columnconfigure(0, weight=1)

        # All places widgets
        places = master.places_message.get("content", None)
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.all_places_tab, place=place, owned=False)
            place_item.grid(row=index, column=0, sticky='ew')

        # My created places widgets
        places = master.my_places_message.get("content", None)
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.my_created_places_tab, place=place)
            place_item.grid(row=index, column=0, sticky='ew')

        # Liked places widgets
        places = master.liked_places_message.get("content", None)
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.liked_places_tab, place=place, owned=False)
            place_item.grid(row=index, column=0, sticky='ew')

    def on_add_button_click(self, event):
        # ViewAllPlaceFrame -> PlaceFrame
        self.master.create_place()


class PlaceItem(CTkFrame):

    def __init__(self, master, place, owned=True):
        super().__init__(master)
        self.place = place
        self.owned = owned
        self.sock = master.master.master.sock
        self.session_id = master.master.master.session_id

        # General configuration
        self.columnconfigure(0, weight=1)
        self.configure(fg_color='transparent')
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)

        # Image
        self.edit_icon = CTkImage(Image.open(os.path.join(image_path, 'edit_icon.png')), size=(30, 30))
        self.delete_icon = CTkImage(Image.open(os.path.join(image_path, 'delete_icon.png')), size=(30, 30))

        # Widgets
        place_name_label = CTkLabel(master=self, text=self.place['name'], wraplength=1000, justify='left')
        place_name_label.grid(row=0, column=0, sticky='w')
        place_name_addr = CTkLabel(master=self, text=self.place['description'], wraplength=1000, justify='left')
        place_name_addr.grid(row=1, column=0, sticky='w')

        if self.owned:
            edit_button = CTkButton(master=self, text='', image=self.edit_icon, width=30, height=30, fg_color='transparent', command=self.on_edit_button_click)
            edit_button.grid(row=0, column=1, rowspan=2, sticky='e')
            delete_button = CTkButton(master=self, text='', image=self.delete_icon, width=30, height=30, fg_color='transparent', command=self.on_delete_button_click)
            delete_button.grid(row=0, column=2, rowspan=2, sticky='e')

    def on_enter(self, event):
        self.configure(fg_color='gray')

    def on_leave(self, event):
        self.configure(fg_color='transparent')

    def on_click(self, event):
        """ 
        Call view_place_detail method from a PlaceFrame instance.
        It goes from PlaceItem(self) -> tab in Tabview -> Tabview -> ViewAllPlaceFrame -> PlaceFrame
        """
        self.master.master.master.master.view_place_detail(self.place['id'], self.owned)

    def on_edit_button_click(self):
        self.master.master.master.master.update_place(self.place['id'])

    def on_delete_button_click(self):
        messagebox.askokcancel("Delete place", "Are you sure you want to delete this place?", command=send_place_task(self.sock, self.session_id, task="delete_place", id=self.place['id']))
        response = recvall_str(self.sock)
        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            messagebox.showinfo("Success", message="Place deleted successfully!")


class ViewPlaceDetailFrame(CTkFrame):

    def __init__(self, master, place, owned):
        super().__init__(master)
        self.place = place
        self.owned = owned
        self.sock = master.sock
        self.session_id = master.session_id

        # Images
        self.edit_icon = CTkImage(Image.open(os.path.join(image_path, 'edit_icon.png')), size=(30, 30))

        # General configuration

        # Widgets
        self.label = CTkLabel(master=self, text='Place detail', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w', pady=(0, 20))

        if owned:
            self.edit_button = CTkButton(master=self, text='', image=self.edit_icon, width=30, height=30, fg_color='transparent', command=self.on_edit_button_click)
            self.edit_button.grid(row=0, column=1, sticky='e')

        name_label = CTkLabel(master=self, text='Name')
        name_label.grid(row=1, column=0, sticky='w')
        name_value = CTkLabel(master=self, text=place['name'], wraplength=1000, justify='left')
        name_value.grid(row=2, column=0, sticky='w', pady=(0, 20))

        address_label = CTkLabel(master=self, text='Address')
        address_label.grid(row=3, column=0, sticky='w')
        address_value = CTkLabel(master=self, text=place['address'], wraplength=1000, justify='left')
        address_value.grid(row=4, column=0, sticky='w', pady=(0, 20))

        tags_label = CTkLabel(master=self, text='Tags')
        tags_label.grid(row=5, column=0, sticky='w')
        tags_value = CTkLabel(master=self, text=', '.join(category['category'] for category in place['categories']), wraplength=1000, justify='left')
        tags_value.grid(row=6, column=0, sticky='w', pady=(0, 20))

        tagged_friends_label = CTkLabel(master=self, text='Tagged friends')
        tagged_friends_label.grid(row=7, column=0, sticky='w')
        tagged_friends_value = CTkLabel(master=self, text=', '.join(friends['username'] for friends in place['tagged_friends']), wraplength=1000, justify='left')
        tagged_friends_value.grid(row=8, column=0, sticky='w', pady=(0, 20))

        description_label = CTkLabel(master=self, text='Description')
        description_label.grid(row=9, column=0, sticky='w')
        description_value = CTkLabel(master=self, text=place['description'], wraplength=1000, justify='left')
        description_value.grid(row=10, column=0, sticky='w', pady=(0, 20))

        self.back_button = CTkButton(master=self, text='Back', width=50, height=30, fg_color='gray')
        self.back_button.grid(row=11, column=1, sticky='e')
        self.back_button.bind('<Button-1>', self.on_back_button_click)

    def on_edit_button_click(self):
        self.master.update_place(self.place['id'])

    def on_back_button_click(self, event):
        # ViewPlaceDetailFrame -> PlaceFrame
        self.master.view_all_places()


class CreatePlaceFrame(CTkFrame):

    def __init__(self, master, categories, friends):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        self.categories = categories
        self.friends = friends

        self.name_var = StringVar()
        self.address_var = StringVar()
        self.description_var = StringVar()
        self.chosen_categories = []
        self.categories_var = StringVar()
        self.tagged_friends = []
        self.chosen_friends = self.tagged_friends
        self.chosen_friends_var = StringVar()

        self.toplevel_window = None

        # General configuration
        self.columnconfigure(0, weight=1)

        # Widgets
        self.label = CTkLabel(master=self, text='Create place', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w', pady=(0, 20))

        self.name_label = CTkLabel(master=self, text='Name')
        self.name_label.grid(row=1, column=0, sticky='w')
        self.name_entry = CTkEntry(master=self, textvariable=self.name_var)
        self.name_entry.grid(row=2, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.address_label = CTkLabel(master=self, text='Address')
        self.address_label.grid(row=3, column=0, sticky='w')
        self.address_entry = CTkEntry(master=self, textvariable=self.address_var)
        self.address_entry.grid(row=4, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.tags_label = CTkLabel(master=self, text='Tags')
        self.tags_label.grid(row=5, column=0, sticky='w')
        self.tags_add_button = CTkButton(master=self, text='Modify', width=50, height=30, fg_color='gray', command=self.tag_toplevel)
        self.tags_add_button.grid(row=5, column=2, sticky='e')
        self.tags_entry = CTkEntry(master=self, state='disabled', textvariable=self.categories_var)
        self.tags_entry.grid(row=6, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.tagged_friends_label = CTkLabel(master=self, text='Tagged friends')
        self.tagged_friends_label.grid(row=7, column=0, sticky='w')
        self.tagged_friends_add_button = CTkButton(master=self, text='Modify', width=50, height=30, fg_color='gray', command=self.friend_toplevel)
        self.tagged_friends_add_button.grid(row=7, column=2, sticky='e')
        self.tagged_friends_entry = CTkEntry(master=self, state='disabled', textvariable=self.chosen_friends_var)
        self.tagged_friends_entry.grid(row=8, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.description_label = CTkLabel(master=self, text='Description')
        self.description_label.grid(row=9, column=0, sticky='w')
        self.description_entry = CTkEntry(master=self, textvariable=self.description_var)
        self.description_entry.grid(row=10, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.submit_button = CTkButton(master=self, text='Submit', width=50, height=30, fg_color='gray', command=self.submit)
        self.submit_button.grid(row=11, column=1, padx=(0, 20), sticky='e')

        self.cancel_button = CTkButton(master=self, text='Cancel', width=50, height=30, fg_color='gray', command=self.cancel)
        self.cancel_button.grid(row=11, column=2, sticky='e')

    def tag_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TagWindow(self, callback=self.submit_tag)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def submit_tag(self, checkbox_vars):
        self.chosen_categories = []
        categories_str = ""
        # for id, var in checkbox_vars.items():
        #     if var.get() == 1:
        #         self.chosen_categories.append(id)
        # for category in self.categories:
        #     if category['id'] in self.chosen_categories:
        #         categories_str += category['category'] + '\t'
        for category_name, var in checkbox_vars.items():
            if var.get() == 1:
                self.chosen_categories.append(category_name)
        categories_str = ', '.join(self.chosen_categories)

        self.categories_var.set(categories_str)

    def friend_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = FriendWindow(self, callback=self.submit_friends)
        else:
            self.toplevel_window.focus()

    def submit_friends(self, checkbox_vars):
        self.chosen_friends = []
        friends_str = ""
        for id, var in checkbox_vars.items():
            if var.get() == 1:
                self.chosen_friends.append(id)
        for friend in self.friends:
            if friend['id'] in self.chosen_friends:
                friends_str += friend['username'] + '\t'
        self.chosen_friends_var.set(value=friends_str)

    def submit(self):
        send_place_task(self.sock, self.session_id, task="create_place", name=self.name_var.get(), address=self.address_var.get(),
                        description=self.description_var.get(), tags=self.chosen_categories, tagged_friends=self.chosen_friends)
        response = recvall_str(self.sock)
        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            self.master.view_all_places()

    def cancel(self):
        self.master.view_all_places()


class TagWindow(CTkToplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.categories = master.categories
        self.chosen_categories = master.chosen_categories
        self.callback = callback

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title('Modify category tags')
        self.geometry('300x600')
        self.resizable(False, False)

        self.scrollableframe = CTkScrollableFrame(self)
        self.scrollableframe.grid(row=0, column=0, columnspan=2, sticky='nesw')
        self.scrollableframe.columnconfigure(0, weight=1)

        self.checkbox_vars = {}
        for index, category in enumerate(self.categories):
            self.checkbox_vars[category['category']] = IntVar()
            if category['category'] in self.chosen_categories:
                self.checkbox_vars[category['category']].set(value=1)
            checkbox = CTkCheckBox(self.scrollableframe, text=category['category'], variable=self.checkbox_vars[category['category']], onvalue=1, offvalue=0)
            checkbox.grid(row=index, column=0, sticky='w')

        self.submit_button = CTkButton(self, text="Submit", width=50, height=30, fg_color='gray', command=self.submit)
        self.submit_button.grid(row=1, column=0, sticky='e')
        self.cancel_button = CTkButton(self, text="Cancel", width=50, height=30, fg_color='gray', command=self.cancel)
        self.cancel_button.grid(row=1, column=1, sticky='e')

    def submit(self):
        self.callback(self.checkbox_vars)
        self.destroy()

    def cancel(self):
        self.destroy()


class FriendWindow(CTkToplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.friends = master.friends
        self.tagged_friends = master.tagged_friends
        self.chosen_friends = master.chosen_friends

        self.callback = callback

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title('Modify friend tags')
        self.geometry('300x600')
        self.resizable(False, False)

        self.scrollableframe = CTkScrollableFrame(self)
        self.scrollableframe.grid(row=0, column=0, columnspan=2, sticky='nesw')
        self.scrollableframe.columnconfigure(0, weight=1)

        self.checkbox_vars = {}
        for index, friend in enumerate(self.friends):
            self.checkbox_vars[friend['id']] = IntVar()

            checkbox = CTkCheckBox(self.scrollableframe, text=friend['username'], variable=self.checkbox_vars[friend['id']], onvalue=1, offvalue=0)
            if int(friend['id']) in self.chosen_friends:
                self.checkbox_vars[friend['id']].set(value=1)
            if int(friend['id']) in self.tagged_friends:
                checkbox.configure(state='disabled')
            checkbox.grid(row=index, column=0, sticky='w')

        self.submit_button = CTkButton(self, text="Submit", width=50, height=30, fg_color='gray', command=self.submit)
        self.submit_button.grid(row=1, column=0, sticky='e')
        self.cancel_button = CTkButton(self, text="Cancel", width=50, height=30, fg_color='gray', command=self.cancel)
        self.cancel_button.grid(row=1, column=1, sticky='e')

    def submit(self):
        self.callback(self.checkbox_vars)
        self.destroy()

    def cancel(self):
        self.destroy()


class UpdatePlaceFrame(CTkFrame):

    def __init__(self, master, place, categories, friends):
        super().__init__(master)
        self.sock = master.sock
        self.session_id = master.session_id
        self.place = place
        self.categories = categories
        self.friends = friends

        self.name_var = StringVar(value=place['name'])
        self.address_var = StringVar(value=place['address'])
        self.description_var = StringVar(value=place['description'])
        self.chosen_categories = [category['category'] for category in place['categories']]
        self.categories_var = StringVar()
        self.tagged_friends = [friend['id'] for friend in place['tagged_friends']]
        self.chosen_friends = self.tagged_friends
        self.chosen_friends_var = StringVar()

        self.toplevel_window = None

        # General configuration
        self.columnconfigure(0, weight=1)

        # Widgets
        self.label = CTkLabel(master=self, text='Create place', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w', pady=(0, 20))

        self.name_label = CTkLabel(master=self, text='Name')
        self.name_label.grid(row=1, column=0, sticky='w')
        self.name_entry = CTkEntry(master=self, textvariable=self.name_var)
        self.name_entry.grid(row=2, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.address_label = CTkLabel(master=self, text='Address')
        self.address_label.grid(row=3, column=0, sticky='w')
        self.address_entry = CTkEntry(master=self, textvariable=self.address_var)
        self.address_entry.grid(row=4, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.tags_label = CTkLabel(master=self, text='Tags')
        self.tags_label.grid(row=5, column=0, sticky='w')
        self.tags_add_button = CTkButton(master=self, text='Modify', width=50, height=30, fg_color='gray', command=self.tag_toplevel)
        self.tags_add_button.grid(row=5, column=2, sticky='e')
        self.tags_entry = CTkEntry(master=self, state='disabled', textvariable=self.categories_var)
        self.tags_entry.grid(row=6, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.tagged_friends_label = CTkLabel(master=self, text='Tagged friends')
        self.tagged_friends_label.grid(row=7, column=0, sticky='w')
        self.tagged_friends_add_button = CTkButton(master=self, text='Modify', width=50, height=30, fg_color='gray', command=self.friend_toplevel)
        self.tagged_friends_add_button.grid(row=7, column=2, sticky='e')
        self.tagged_friends_entry = CTkEntry(master=self, state='disabled', textvariable=self.chosen_friends_var)
        self.tagged_friends_entry.grid(row=8, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.description_label = CTkLabel(master=self, text='Description')
        self.description_label.grid(row=9, column=0, sticky='w')
        self.description_entry = CTkEntry(master=self, textvariable=self.description_var)
        self.description_entry.grid(row=10, column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.submit_button = CTkButton(master=self, text='Submit', width=50, height=30, fg_color='gray', command=self.submit)
        self.submit_button.grid(row=11, column=1, padx=(0, 20), sticky='e')

        self.cancel_button = CTkButton(master=self, text='Cancel', width=50, height=30, fg_color='gray', command=self.cancel)
        self.cancel_button.grid(row=11, column=2, sticky='e')

    def tag_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TagWindow(self, callback=self.submit_tag)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def submit_tag(self, checkbox_vars):
        self.chosen_categories = []
        categories_str = ""
        for id, var in checkbox_vars.items():
            if var.get() == 1:
                self.chosen_categories.append(id)
        for category in self.categories:
            if category['id'] in self.chosen_categories:
                categories_str += category['category'] + '\t'
        self.categories_var.set(categories_str)

    def friend_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = FriendWindow(self, callback=self.submit_friends)
        else:
            self.toplevel_window.focus()

    def submit_friends(self, checkbox_vars):
        self.chosen_friends = []
        friends_str = ""
        for id, var in checkbox_vars.items():
            if var.get() == 1:
                self.chosen_friends.append(id)
        for friend in self.friends:
            if friend['id'] in self.chosen_friends:
                friends_str += friend['username'] + '\t'
        self.chosen_friends_var.set(value=friends_str)

    def submit(self):
        send_place_task(self.sock, self.session_id, task="update_place", id=self.place['id'], name=self.name_var.get(), address=self.address_var.get(),
                        description=self.description_var.get(), tags=self.chosen_categories, tagged_friends=self.chosen_friends)
        response = recvall_str(self.sock)
        if not response.get("success", None):
            messagebox.showerror("Error", message=code2message(response.get("code", None)))
        else:
            self.master.view_all_places()

    def cancel(self):
        self.master.view_all_places()
