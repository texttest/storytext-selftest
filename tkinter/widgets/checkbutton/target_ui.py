# menu-example-3.py

try:
    from tkinter import *
except:
    from Tkinter import *

def printMusic():
    print("Let the music play...")

top = Tk()
lf1 = LabelFrame(top, text="Settings", padx=6, pady=6)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(lf1, text = "Music",
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20)
# Try to set this stuff in lots of different ways...
C1["variable"] = CheckVar1
C1["command"] = printMusic
C2 = Checkbutton(lf1, text = "Video",
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20)
C2.config(variable=CheckVar2)
C2.select()
C3 = Checkbutton(lf1, text = "Subtitles", variable = CheckVar3,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20)


C1.pack()
C2.pack()
C3.pack()
lf1.pack()
top.mainloop()
