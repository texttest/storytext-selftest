# File: hello2.py

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

class App:

    def __init__(self, master):
        Label(master, text="Top Left").grid(row=0, column=0)
        Label(master, text="Top Right").grid(row=0, column=1, rowspan=3)
        Label(master, text="Bottom Left").grid(row=1, column=0)
        Button(master, text="QUIT", fg="red", command=master.quit).grid(row=2, column=0)

root = Tk()

app = App(root)

root.mainloop()
