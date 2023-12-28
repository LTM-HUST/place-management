from customtkinter import *
from PIL import Image


image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
field_names = [
    ('Name', 'name'),
    ('Address', 'address'),
    ('Tags', 'tags'),
    ('Tagged friends', 'tagged_friends'),
    ('Description', 'description')
]


class PlaceFrame(CTkScrollableFrame):

    def __init__(self, master, places_message, my_places_message, liked_places_message):
        super().__init__(master)  # init PlaceFrame (only once)
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
        place_name_addr = CTkLabel(master=self, text=place['description'], wraplength=1000, justify='left')
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
        self.master.master.master.master.view_place_detail(self.place.id, self.owned)


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
            field_value.grid(row=2*(index+1), column=0, columnspan=3, sticky='we', pady=(0, 20))

        self.submit_button = CTkButton(master=self, text='Submit', width=50, height=30, fg_color='gray')
        self.submit_button.grid(row=2*len(field_names)+1, column=1, padx=(0, 20), sticky='e')

        self.cancel_button = CTkButton(master=self, text='Cancel', width=50, height=30, fg_color='gray')
        self.cancel_button.grid(row=2*len(field_names)+1, column=2, sticky='e')
