import tkinter as tk

from GUI.create_widgets import create_frame, create_label, create_button, create_entry
from GUI.itemframes import Itemframe

from Modules import database
from Modules.items import Item


class App:
    """
    Set and run app GUI
    """

    # tuple with font style

    def __init__(self, items):
        """
        Default constructor.\n
        Create and run mainloop
        """

        # Tuple with font styles
        self.font = (("Arial Bold",32),("Arial Bold",12))

        # dict with items objects
        self.ITEMS = items
        # list with frame objects
        self.ITEMFRAMES = {}


        # Create MainWindow
        self.root = tk.Tk()
        self.root.title("Bannerlord Markets")



        ## HEADER FRAME ##
        self.header = create_frame(self.root)
        self.header.configure(padx=10,pady=10)

        # header text
        header_text = "M&B2 Bannerlord Markets"
        self.header_label = create_label(self.header, header_text,0,0,("Arial Bold",32),20,20)



        # EXIT/LOAD/SAVE FRAME
        self.els_frame = create_frame(self.header, 0,1)

        # Exit button
        self.exit = create_button(self.els_frame, "EXIT",0,0,self.font[1],10)
        self.exit.configure(command=self.quit_app)
        # Load button
        self.load = create_button(self.els_frame,"LOAD",0,1,self.font[1],10)
        self.load.configure(command=self.load_from_db)
        # Save Button
        self.save = create_button(self.els_frame,"SAVE",0,2,self.font[1],10)
        self.save.configure(command=self.save_to_db)



        # ADD ITEM FRAME
        self.add_frame = create_frame(self.root,2)
        
        # add item entry
        self.add_entry = create_entry(self.add_frame,0,0,self.font[1],10)
        # event on enter
        self.add_entry.bind('<Return>',self.get_new_item)
        # add item button
        self.add_button = create_button(self.add_frame, "Add Item",1,0)
        self.add_button.configure(width=10)
        # event on click
        self.add_button.configure(command=self.get_new_item)



        # DATA FRAME
        self.data_frame = create_frame(self.root, 1)
        self.data_frame.configure(padx=20,pady=20)
        self.print_item_data(self.data_frame)


        # Run MainLoop
        self.root.mainloop()

    ###   METODS   ###

    def print_item_data(self,frame):

        # Get keys and sort
        keys = list(self.ITEMS.keys())
        keys.sort()

        for index,key in enumerate(keys):
            itemframe = Itemframe(frame, self.ITEMS[key])
            self.ITEMFRAMES[key] = itemframe

            itemframe.print(index+1)

    def get_new_item(self,event=None):
        # Get value
        value = self.add_entry.get()
        self.add_entry.delete(0,'end')
        value = value.capitalize()

        # Check if value is valid
        valid = True
        keys = self.ITEMFRAMES.keys()
        if value in keys or len(value) < 2:
            valid = False

        if valid:
            items = {}

            for key in keys:
                if not self.ITEMFRAMES[key].isRemoved:
                    items[key] = self.ITEMFRAMES[key].item
                    self.ITEMFRAMES[key].remove(False)

            self.ITEMS = items
            self.ITEMS[value] = Item(value)
            self.ITEMFRAMES = {}

            self.print_item_data(self.data_frame)
    
    def save_to_db(self):

        db_items = database.get_item_dict()

        db_keys = db_items.keys()
        list_keys = self.ITEMFRAMES.keys()
        insert = []
        delete = []
        update = []
        remove = []

        for key in list_keys:
            if self.ITEMFRAMES[key].isRemoved:
                remove.append(key)

            if not key in db_keys:
                insert.append(self.ITEMFRAMES[key].item)
            else:
                update.append(self.ITEMFRAMES[key].item)
        
        for key in remove:
            del self.ITEMFRAMES[key]

        for key in db_keys:
            if not key in list_keys:
                delete.append(db_items[key])

        database.insert_many(insert)
        database.update_many(update)
        database.delete_many(delete)

    def load_from_db(self):

        keys = self.ITEMFRAMES.keys()
        for key in keys:
            self.ITEMFRAMES[key].remove(False)
        self.ITEMFRAMES = {}

        self.ITEMS = database.get_item_dict()
        self.print_item_data(self.data_frame)

    def quit_app(self):
        self.save_to_db()
        self.root.destroy()
