from customtkinter import *
from PIL import Image

places = [
    {
        "place_id": 1,
        "place_name": "Place 1",
        "place_address": "Address 1",
    },
    {
        "place_id": 2,
        "place_name": "Place 2",
        "place_address": "Address 2",
    },
    {
        "place_id": 3,
        "place_name": "Place 3",
        "place_address": "Address 3",
    },
    {
        "place_id": 4,
        "place_name": "Place 4",
        "place_address": "Address 4",
    },
    {
        "place_id": 5,
        "place_name": "Place 5",
        "place_address": "Address 5",
    },
    {
        "place_id": 6,
        "place_name": "Place 6",
        "place_address": "Address 6",
    },
    {
        "place_id": 7,
        "place_name": "Place 7",
        "place_address": "Address 7",
    },
    {
        "place_id": 8,
        "place_name": "Place 8",
        "place_address": "Address 8",
    },
    {
        "place_id": 9,
        "place_name": "Place 9",
        "place_address": "Address 9",
    },
    {
        "place_id": 10,
        "place_name": "Place 10",
        "place_address": "Address 10",
    }
]


class PlaceFrame(CTkScrollableFrame):

    def __init__(self, master):
        super().__init__(master)

        # Images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'images')
        self.add_icon = CTkImage(Image.open(os.path.join(
            image_path, 'add_icon.png')), size=(30, 30))
        self.edit_icon = CTkImage(Image.open(os.path.join(
            image_path, 'edit_icon.png')), size=(30, 30))
        self.delete_icon = CTkImage(Image.open(os.path.join(
            image_path, 'delete_icon.png')), size=(30, 30))

        # General widgets
        self.label = CTkLabel(master=self, text='Place management', font=CTkFont(
            size=18, weight='bold'))
        self.label.grid(row=0, column=0, sticky='w')

        self.add_button = CTkButton(
            master=self, text='', image=self.add_icon, width=30, height=30 , fg_color='transparent') #overwrite CTkButton default width and height
        self.add_button.grid(row=0, column=1, sticky='e')

        self.tabview = CTkTabview(master=self, anchor='w')
        self.tabview.add('All places')
        self.tabview.add('My created places')
        self.tabview.add('Liked places')
        self.tabview.grid(row=1, column=0, columnspan=2, sticky='ew') # stretch frame to fill master

        self.all_places_tab = self.tabview.tab('All places')
        self.all_places_tab.grid_columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space

        # All places widget
        self.all_places_tab.frames = []
        for i, place in enumerate(places):
            place_frame = CTkFrame(master=self.all_places_tab)
            place_frame.grid(row=i, column=0, sticky='ew') # stretch frame to fill master
            place_frame.grid_columnconfigure(0, weight=1) # stretch the first column to fill the whole remaining space
            self.all_places_tab.frames.append(place_frame)

            place_name_label = CTkLabel(
                master=place_frame, text=place['place_name'])
            place_name_label.grid(row=0, column=0, sticky='w')
            place_name_addr = CTkLabel(
                master=place_frame, text=place['place_address'])
            place_name_addr.grid(row=1, column=0, sticky='w')
            edit_button = CTkButton(
                master=place_frame, text='', image=self.edit_icon, width=30, height=30, fg_color='transparent')
            edit_button.grid(row=0, column=1, rowspan=2, sticky='e')
            delete_button = CTkButton(
                master=place_frame, text='', image=self.delete_icon, width=30, height=30, fg_color='transparent')
            delete_button.grid(row=0, column=2, rowspan=2, sticky='e')
