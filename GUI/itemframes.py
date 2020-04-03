import tkinter as tk

from GUI.create_widgets import create_label, create_entry, create_button



class Itemframe:

    def __init__(self, frame, item):
        """ 
        Create a frame for each item in item list\n
        INPUT:\n
            - parent Frame
            - item object
        OUTPUT:\n
            - Frame object
        """

        self.item = item

        self.itemframe = tk.Frame(frame)
        self.itemframe.configure(highlightbackground="darkgrey", highlightthickness=1)

        self.input = create_entry(self.itemframe)
        self.input.bind('<Return>',self.add_value)
        
        self.add = create_button(self.itemframe,"Add",1)
        self.add.configure(command=self.add_value)

        self.undo = create_button(self.itemframe, "Undo",2)
        self.undo.configure(command=self.undo_last)

        self.name = create_label(self.itemframe, self.item.name,3)
        self.name.configure(width=15)

        self.avg = create_label(self.itemframe, round(self.item.avg_price),4)
        self.avg.configure(width=5)

        self.min = create_label(self.itemframe, round(self.item.min_price), 5)
        self.min.configure(width=5)

        self.max = create_label(self.itemframe, round(self.item.max_price), 6)
        self.max.configure(width=5)

        self.remove_item = create_button(self.itemframe, "Remove",7)
        self.remove_item.configure(width=10,command=self.remove)

        self.isRemoved = False

        self.remove_counter = 2
    
    def print(self,r):
        self.itemframe.grid(column=0, row=r)
    
    def add_value(self, event=None):        
        value = self.input.get()
        self.input.delete(0,'end')
        valid = True

        try:
            int(value)
        except ValueError:
            valid = False

        if valid:
            self.item.append(int(value))
            self.change_text()

    def undo_last(self):
        self.item.undo_last()
        self.change_text()

    def change_text(self):
        self.avg.configure(text=round(self.item.avg_price))
        self.min.configure(text=round(self.item.min_price))
        self.max.configure(text=round(self.item.max_price))

    def remove(self, confirm=True):

        def reset():
            self.remove_item.configure(text="Remove")
            self.remove_counter = 2

        if confirm:
            self.remove_counter -= 1
            if self.remove_counter == 1:
                self.remove_item.configure(text="Confirm")
                self.itemframe.after(2000,reset)
            else:
                self.itemframe.destroy()
                self.isRemoved = True
        else:
            self.itemframe.destroy()
        
 