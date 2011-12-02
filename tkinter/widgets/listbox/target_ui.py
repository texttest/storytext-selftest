try:
    from tkinter import *
except:
    from Tkinter import *

def select(event):
    print("Selected " + repr(listbox.curselection()))

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

listbox.bind("<<ListboxSelect>>", select)

master.mainloop()
