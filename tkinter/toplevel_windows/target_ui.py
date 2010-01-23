# File: hello2.py

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, name="hello button", text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):	
        win = Toplevel()
	win.title('Hi!')
	def destroy(*args):
            win.destroy()
        label = Label(win, name="hello label", text="hi there, everyone!", bg="white")
        label.bind("<Button-1>", destroy)
	label.pack()

root = Tk()

app = App(root)

root.mainloop()
