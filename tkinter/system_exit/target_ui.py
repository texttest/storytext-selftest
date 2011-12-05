# File: hello2.py
try:
    from tkinter import *
except:
    from Tkinter import *
import sys

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)


root = Tk()

app = App(root)

root.mainloop()
# Shouldn't prevent the usecase name chooser appearing...
sys.exit(1)
