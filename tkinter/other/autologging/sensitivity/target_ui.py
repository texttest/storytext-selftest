# File: hello2.py

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()


        self.cb = Checkbutton(frame, text="Quit Allowed", variable=IntVar(), command=self.enable_quit)
        self.cb.pack(side=TOP)

        self.quit = Button(frame, text="QUIT", fg="red", state=DISABLED, command=frame.quit)
        self.quit.pack(side=LEFT)

        self.disableCb = Button(frame, text="Disable Check", command=self.disable_check)
        self.disableCb.pack(side=LEFT)

    def disable_check(self):
        self.cb.config(state=DISABLED)

    def enable_quit(self):
        self.quit.config(state=NORMAL)

root = Tk()

app = App(root)

root.mainloop()
