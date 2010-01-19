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

        notebook = gtk.Notebook()
        button = gtk.Button("Change the text!")
        label = gtk.Label("Original text")
        button.connect("clicked", self.changeText, (label, notebook))
        notebook.append_page(label, gtk.Label("Tab 1"))
        notebook.append_page(button, gtk.Label("Tab 2"))
        window.add(notebook)

        # Display the window
        window.show_all()

    def changeText(self, button, extra):
        label, notebook = extra
        label.set_text("New text")
        notebook.set_current_page(0)


def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    Example()
    main()
