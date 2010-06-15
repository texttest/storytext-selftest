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
        button1 = gtk.Button("Grey and Ungrey")
        button2 = gtk.Button("Ungrey and Grey")
        button3 = gtk.Button("I'm just Grey")
        button1.connect("clicked", self.greyAndUngrey, button2)
        button2.connect("clicked", self.ungreyAndGrey, button3)
        button3.set_sensitive(False)
        box.pack_start(button1)
        box.pack_start(button2)
        box.pack_start(button3)

        # Display the window
        window.show_all()

    def greyAndUngrey(self, button, toChange):
        toChange.set_sensitive(False)
        toChange.set_sensitive(True)

    def ungreyAndGrey(self, button, toChange):
        toChange.set_sensitive(True)
        toChange.set_sensitive(False)


def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    Example()
    main()
