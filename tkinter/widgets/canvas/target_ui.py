from Tkinter import *

def describe(event):
    widget = event.widget
    item = widget.find_closest(widget.canvasx(event.x), widget.canvasy(event.y))
    if widget.type(item) == "polygon":
        widget.itemconfigure(item, fill="yellow")
    print "Clicked item", item

root = Tk()
canvas = Canvas(root, width=300, height=320)
canvas.pack(fill=BOTH)
square = canvas.create_rectangle(0,0,150,150, fill="green", tags="rectangle")
circle = canvas.create_oval(0,150,150,300, fill="blue")
diamond = canvas.create_polygon(150,75,225,0,300,75,225,150, fill="red", tags="10000") # A tag that looks like a number, to trip up Tk
text = canvas.create_text(230,230, text="Tkinter canvas", fill="purple", 
                          font=("Helvetica", "16"))
label = canvas.create_text(0,75, text="Green rectangle", anchor=W, tags="rectangle")
button = Button(root, text="A button")
canvas.create_window(0, 300, window=button, anchor=NW)
canvas.bind('<Button-1>', describe)

root.mainloop()
