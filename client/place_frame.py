from customtkinter import *
from PIL import Image

places = [
    {
        "id": 1,
        "name": "Place 1",
        "address": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "id": 2,
        "name": "Place 2",
        "address": "Address 2",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 2",
    },
    {
        "id": 3,
        "name": "Place 3",
        "address": "Address 3",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 3",
    },
    {
        "id": 4,
        "name": "Place 4",
        "address": "Address 4",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 4",
    },
    {
        "id": 5,
        "name": "Place 5",
        "address": "Address 5",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 5",
    },
    {
        "id": 6,
        "name": "Place 6",
        "address": "Address 6",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 6",
    },
    {
        "id": 7,
        "name": "Place 7",
        "address": "Address 7",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 7",
    },
    {
        "id": 8,
        "name": "Place 8",
        "address": "Address 8",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 8",
    },
    {
        "id": 9,
        "name": "Place 9",
        "address": "Address 9",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 9",
    },
    {
        "id": 10,
        "name": "Place 10",
        "address": "Address 10",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 10",
    },
    {
        "id": 11,
        "name": "Place 11",
        "address": "Address 11",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 11",
    },
    {
        "id": 12,
        "name": "Place 12",
        "address": "Address 12",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 12",
    },
    {
        "id": 13,
        "name": "Place 13",
        "address": "Address 13",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 13",
    },
    {
        "id": 14,
        "name": "Place 14",
        "address": "Address 14",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 14",
    },
    {
        "id": 15,
        "name": "Place 15",
        "address": "Address 15",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 15",
    },
    {
        "id": 16,
        "name": "Place 16",
        "address": "Address 16",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 16",
    },
]
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
field_names = [
    ('Name', 'name'),
    ('Address', 'address'),
    ('Tags', 'tags'),
    ('Tagged friends', 'tagged_friends'),
    ('Description', 'description')
]


class PlaceFrame(CTkScrollableFrame):

    def __init__(self, master, places_message = None, my_places_message = None, liked_places_message = None):
        super().__init__(master) # init PlaceFrame (only once)
        self.places_message = places_message
        self.my_places_message = my_places_message
        self.liked_places_message = liked_places_message

        self.columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
        self.current_frame = ViewAllPlaceFrame(master=self) # init current_frame as ViewAllPlaceFrame
        self.current_frame.grid(row=0, column=0, sticky='nsew') # stretch frame to fill master
        self.current_frame.grid_columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space

    """
    All the following methods are used to switch between frames.
    What they do is to destroy the current frame and create a new one.
    """

    def view_all_places(self):
        self.current_frame.destroy()
        self.current_frame = ViewAllPlaceFrame(master=self)
        self.current_frame.grid(row=0, column=0, sticky='nsew')
        self.current_frame.grid_columnconfigure(0, weight=1)

    def view_place_detail(self, place, owned):
        self.current_frame.destroy()
        self.current_frame = ViewPlaceDetailFrame(master=self, place=place, owned=owned)
        self.current_frame.grid(row=0, column=0, sticky='nsew')
        self.current_frame.grid_columnconfigure(0, weight=1)

    def create_place(self):
        self.current_frame.destroy()
        self.current_frame = CreatePlaceFrame(master=self)
        self.current_frame.grid(row=0, column=0, sticky='nsew')
        self.current_frame.grid_columnconfigure(0, weight=1)


class ViewAllPlaceFrame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # Images
        self.add_icon = CTkImage(Image.open(os.path.join(image_path, 'add_icon.png')), size=(30, 30))
        self.edit_icon = CTkImage(Image.open(os.path.join(image_path, 'edit_icon.png')), size=(30, 30))
        self.delete_icon = CTkImage(Image.open(os.path.join(image_path, 'delete_icon.png')), size=(30, 30))

        # General widgets
        self.label = CTkLabel(master=self, text='Place management', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w')

        self.add_button = CTkButton(
            master=self, text='', image=self.add_icon, width=30, height=30 , fg_color='transparent') # overwrite CTkButton default width and height
        self.add_button.grid(row=0, column=1, sticky='e')
        self.add_button.bind('<Button-1>', self.on_add_button_click)

        self.tabview = CTkTabview(master=self, anchor='w')
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
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.my_created_places_tab, place=place)
            place_item.grid(row=index, column=0, sticky='ew')
        
        # Liked places widgets
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.liked_places_tab, place=place, owned=False)
            place_item.grid(row=index, column=0, sticky='ew')
    
    def on_add_button_click(self, event):
        # ViewAllPlaceFrame -> PlaceFrame
        self.master.create_place()


class PlaceItem(CTkFrame):

    def __init__(self, master, place, owned=True):
        super().__init__(master)

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
        place_name_label = CTkLabel(master=self, text=place['name'], wraplength=1000, justify='left')
        place_name_label.grid(row=0, column=0, sticky='w')
        place_name_addr = CTkLabel(master=self, text=place['address'], wraplength=1000, justify='left')
        place_name_addr.grid(row=1, column=0, sticky='w')

        if owned:
            edit_button = CTkButton(master=self, text='', image=self.edit_icon, width=30, height=30, fg_color='transparent')
            edit_button.grid(row=0, column=1, rowspan=2, sticky='e')
            delete_button = CTkButton(master=self, text='', image=self.delete_icon, width=30, height=30, fg_color='transparent')
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
        self.master.master.master.master.view_place_detail(self.place, self.owned)


class ViewPlaceDetailFrame(CTkFrame):

    def __init__(self, master, place, owned):
        super().__init__(master)
        self.place = place
        self.owned = owned

        # Images
        self.edit_icon = CTkImage(Image.open(os.path.join(image_path, 'edit_icon.png')), size=(30, 30))

        # General configuration

        # Widgets
        self.label = CTkLabel(master=self, text='Place detail', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w', pady=(0, 20))

        if owned:
            self.edit_button = CTkButton(master=self, text='', image=self.edit_icon, width=30, height=30, fg_color='transparent')
            self.edit_button.grid(row=0, column=1, sticky='e')

        for index, field in enumerate(field_names):
            field_label = CTkLabel(master=self, text=field[0])
            field_label.grid(row=2*(index+1)-1, column=0, sticky='w')
            field_value = CTkLabel(master=self, text=place[field[1]], wraplength=1000, justify='left')
            field_value.grid(row=2*(index+1), column=0, sticky='w', pady=(0, 20))

        self.back_button = CTkButton(master=self, text='Back', width=50, height=30, fg_color='gray')
        self.back_button.grid(row=2*len(field_names)+1, column=1, sticky='e')
        self.back_button.bind('<Button-1>', self.on_back_button_click)

    def on_back_button_click(self, event):
        # ViewPlaceDetailFrame -> PlaceFrame
        self.master.view_all_places()


class CreatePlaceFrame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # General configuration
        self.columnconfigure(0, weight=1)

        # Widgets
        self.label = CTkLabel(master=self, text='Create place', font=CTkFont(size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w', pady=(0, 20))

        for index, field in enumerate(field_names):
            field_label = CTkLabel(master=self, text=field[0])
            field_label.grid(row=2*(index+1)-1, column=0, columnspan=3, sticky='w')
            field_value = CTkEntry(master=self)
            field_value.grid(row=2*(index+1), column=0, columnspan=3,sticky='we', pady=(0, 20))

        self.submit_button = CTkButton(master=self, text='Submit', width=50, height=30, fg_color='gray')
        self.submit_button.grid(row=2*len(field_names)+1, column=1, padx=(0, 20),sticky='e')
        
        self.cancel_button = CTkButton(master=self, text='Cancel', width=50, height=30, fg_color='gray')
        self.cancel_button.grid(row=2*len(field_names)+1, column=2, sticky='e')