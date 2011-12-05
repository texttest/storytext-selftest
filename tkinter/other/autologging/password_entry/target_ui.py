
try:
    from tkinter import *
except:
    from Tkinter import *


class App:
    def __init__(self,parent):
        f = Frame(parent)
        f.pack(padx=15,pady=15)
		
        Label(f, text="User Name").grid(row=0, column=0)
        self.userEntry = Entry(f, name="username")
        self.userEntry.grid(row=0, column=1)
        
        Label(f, text="Password").grid(row=1, column=0)
        self.passwordEntry = Entry(f, name="password", show="*")
        self.passwordEntry.grid(row=1, column=1)
        
        Button(f, text="Login", command=self.login).grid(row=2, column=0)
        Button(f, text="Quit", command=f.quit).grid(row=2, column=1)
        
    def login(self):
        print("Logging in with username " + self.userEntry.get() + " and password " + self.passwordEntry.get())


root = Tk()
root.title('Login screen')
app = App(root)

root.mainloop()
