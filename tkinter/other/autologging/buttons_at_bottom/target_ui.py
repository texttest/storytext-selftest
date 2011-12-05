# File: hello2.py

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        label = Label(frame, text="A blue label", bg="blue")
        label.pack(side=BOTTOM)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, name="hello button", text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
