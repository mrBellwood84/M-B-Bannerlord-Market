import tkinter as tk

def create_frame(frame, r=0, c=0):
    """
    Create frame object \n
    INPUT: parent Frame, row, column \n
    OUTPUT: Frame object
    """

    frame = tk.Frame(frame)
    frame.grid(column=c, row=r)
    return frame


def create_label(frame, text, c=0, r=0, font=("Arial",12), x=5, y=2):
    """
    Create label\n

    INPUTS: 
        - parent Frame,
        - text string,
        - font tuple
        - indexed font from tuple, 
        - row and column, have default values
        - padx and pady, have default values
    OUTPUT:
        - label object
    """
    label = tk.Label(frame,text=text, font=font,padx=x,pady=y)
    label.grid(column = c, row = r)
    return label


def create_button(frame, text, c=0, r=0, f=("Arial Bold",12), w=5, x=5, y=2):
    """
    Create Button.
    Set command by configure method\n
    INPUT:\n
        - parent Frame
        - text
        - column and row for grid, default values
        - font index for tuple, default values
        - x and y for padding, default values
    Output:\n
        - Button Object
    """
    
    # set font
    button = tk.Button(frame, text=text, font=f, width=w)
    button.grid(column=c, row=r, padx=x, pady=y)
    return button


def create_entry(frame, c=0, r=0, f=("Arial",12), w=5,x=5,y=2 ):
    """
    Create entry.
    Set command by configure method\n
    INPUT:\n
        - frame: parent Frame
        - c and r: column and row for grid, default values
        - w: width, defauly value
        - x, y: padx, pady, for padding, default values
    Output:\n
        - Button Object
    """

    entry = tk.Entry(frame,width=w,font=f)
    entry.grid(column=c,row=r,padx=x,pady=y)
    return entry