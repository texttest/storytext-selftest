#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Example:
    def __init__(self):
        # Create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Example")

        # Here we connect the "destroy" event to a signal handler 
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_size_request(300, 300)

        # Sets the border width of the window.
        window.set_border_width(10)

        box = gtk.HBox()
        window.add(box)
        box.pack_start(gtk.Label("A label"))
        box.pack_start(gtk.VSeparator())
        paned = gtk.HPaned()
        paned.add1(gtk.Label("Left Window"))
        paned.add2(gtk.Label("Right Window"))
        box.pack_start(paned)

        # Display the window
        window.show_all()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    Example()
    main()
