# File: hello2.py
# -*- coding: utf-8 -*-

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        master.title("Svensk översättning")

        label = Label(frame, text="Lite blå text", bg="blue")
        label.pack(side=TOP)

        self.button = Button(frame, text="STÄNG", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, name="hello button", text="Hälsa", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hejsan, allihopa!"

root = Tk()

app = App(root)

root.mainloop()
