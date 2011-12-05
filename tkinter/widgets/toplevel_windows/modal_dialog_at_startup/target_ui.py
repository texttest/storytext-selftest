# File: hello2.py

try:
    from tkinter import *
    import tkinter.messagebox as tkMessageBox
except:
    from Tkinter import *
    import tkMessageBox

class App:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()

        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

        win = Toplevel(self.master)
        win.title('Hi!')
        win.grab_set()
        def destroy(*args):
            win.destroy()
        label = Label(win, name="hello label", text="hi there, everyone!", bg="white")
        label.bind("<Button-1>", destroy)
        label.pack()
        win.wait_window(win)

root = Tk()

app = App(root)

root.mainloop()
