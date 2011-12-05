try:
    from tkinter import *
except:
    from Tkinter import *

root = Tk()

w = Label(root, text="Right-click to display menu", width=40, height=20)
w.pack()

def next(*args):
    print("Next")

def previous(*args):
    print("Prev")

def home(*args):
    print("Home")

# create a menu
popup = Menu(root, name="popup menu", tearoff=0)
popup.add_command(label="Next", command=next)
popup.add_command(label="Previous", command=previous)
submenu = Menu(popup, tearoff=0)
submenu.add_command(label="Next again", command=next)
popup.add_cascade(label="Submenu", menu=submenu)
popup.add_separator()
popup.add_command(label="Home", command=home)

def do_popup(event):
    # display the popup menu
    popup.post(event.x_root, event.y_root)
    
w.bind("<Button-3>", do_popup)

b = Button(root, text="Quit", command=root.destroy)
b.pack()

root.mainloop()
