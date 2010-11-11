#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import hildon, gtk

class Example:
    # This callback quits the program
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = hildon.StackableWindow()
        
        # Set the window title
        self.window.set_title("Main Window")

        # Set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.delete_event)

        button = gtk.Button("Hello")
        button.show()
        self.window.set_edit_toolbar(button)

        self.window.show()

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    Example()
    main()
