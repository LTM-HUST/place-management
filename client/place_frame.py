from customtkinter import *
from PIL import Image

places = [
    {
        "id": 1,
        "name": "Place 1",
        "address": "Address 1",
        "tags": ["tag1", "tag2"],
        "tagged_friends": ["friend1", "friend2"],
        "description": "Description 1",
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
]

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

class PlaceFrame(CTkScrollableFrame):

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

        self.tabview = CTkTabview(master=self, anchor='w')
        self.tabview.add('All places')
        self.tabview.add('My created places')
        self.tabview.add('Liked places')
        self.tabview.grid(row=1, column=0, columnspan=2, sticky='ew') # stretch frame to fill master

        self.all_places_tab = self.tabview.tab('All places')
        self.all_places_tab.grid_columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
        self.my_created_places_tab = self.tabview.tab('My created places')
        self.my_created_places_tab.grid_columnconfigure(0, weight=1)
        self.liked_places_tab = self.tabview.tab('Liked places')
        self.liked_places_tab.grid_columnconfigure(0, weight=1)

        # All places widget
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.all_places_tab, place=place, owned=False)
            place_item.grid(row=index, column=0, sticky='ew') # stretch frame to fill master

        # My created places widget
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.my_created_places_tab, place=place)
            place_item.grid(row=index, column=0, sticky='ew')
        
        # Liked places widget
        for index, place in enumerate(places):
            place_item = PlaceItem(master=self.liked_places_tab, place=place, owned=False)
            place_item.grid(row=index, column=0, sticky='ew')


class PlaceItem(CTkFrame):

    def __init__(self, master, place, owned=True):
        super().__init__(master)
        self.place = place
        self.owned = owned

        # General configuration
        self.columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)

        # Image
        self.edit_icon = CTkImage(Image.open(os.path.join(image_path, 'edit_icon.png')), size=(30, 30))
        self.delete_icon = CTkImage(Image.open(os.path.join(image_path, 'delete_icon.png')), size=(30, 30))

        # Widgets
        place_name_label = CTkLabel(master=self, text=place['name'])
        place_name_label.grid(row=0, column=0, sticky='w')
        place_name_addr = CTkLabel(master=self, text=place['address'])
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
        # Modify to render a new frame with the place details
        print(f"Place name: {self.place['name']}")
        print(f"Place address: {self.place['address']}")
        print(f"Place tags: {self.place['tags']}")
        print(f"Place tagged friends: {self.place['tagged_friends']}") if self.owned else None
        print(f"Place description: {self.place['description']}")
