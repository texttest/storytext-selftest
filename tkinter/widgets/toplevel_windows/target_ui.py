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
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, name="hello button", text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        master.protocol("WM_DELETE_WINDOW", self.ask)
    
    def ask(self):
        if tkMessageBox.askyesno("Quit", "Are you sure you want to terminate this fantastic program?"):
            self.master.destroy()
        
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
