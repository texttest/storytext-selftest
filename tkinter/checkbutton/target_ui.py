# menu-example-3.py

from Tkinter import *

top = Tk()
lf1 = LabelFrame(top, text="Settings", padx=6, pady=6)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(lf1, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(lf1, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2.select()
C1.pack()
C2.pack()
lf1.pack()
top.mainloop()
