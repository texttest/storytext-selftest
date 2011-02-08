# menu-example-3.py
# -*- coding: utf-8 -*-

import Tkinter
from ScrolledText import ScrolledText

root = Tkinter.Tk()

def hello():
    print "hejsan"
    text.insert(Tkinter.END, "Gjorde någonting från en meny!\n")

menubar = Tkinter.Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Öppna", command=hello)
filemenu.add_command(label="Spara", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Avsluta", command=root.quit)
menubar.add_cascade(label="Fil", menu=filemenu)

# create more pulldown menus
editmenu = Tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Klippa", command=hello)
editmenu.add_command(label="Kopiera", command=hello)
editmenu.add_command(label="Klistra", command=hello)
menubar.add_cascade(label="Ändra", menu=editmenu)

helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Om", command=hello)
menubar.add_cascade(label="Hjälp", menu=helpmenu)

# display the menu
root.config(menu=menubar)

Tkinter.Label(root, text="En textfält:").grid(row=0, column=0)
text = ScrolledText(root)
text.grid(row=0, column=1)

Tkinter.mainloop()
