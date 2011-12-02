# menu-example-3.py

try:
    import tkinter as Tkinter
    from tkinter.scrolledtext import ScrolledText
except:
    import Tkinter
    from ScrolledText import ScrolledText

root = Tkinter.Tk()

def hello():
    print("hello")
    text.insert(Tkinter.END, "Did something from a menu!\n")

menubar = Tkinter.Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

Tkinter.Label(root, text="Some text:").grid(row=0, column=0)
text = ScrolledText(root)
text.grid(row=0, column=1)

Tkinter.mainloop()
