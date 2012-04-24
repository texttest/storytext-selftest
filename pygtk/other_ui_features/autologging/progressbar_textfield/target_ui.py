#!/usr/bin/env python

# example progressbar.py

import pygtk
pygtk.require('2.0')
import gtk, gobject
from storytext import applicationEvent

# Update the value of the progress bar so that we get
# some movement
def progress_timeout(pbobj):
    # Calculate the value of the progress bar using the
    # value range set in the adjustment object
    new_val = pbobj.pbar.get_fraction() + 0.02
    if new_val > 1.0:
        new_val = 0.0
    # Set the new value
    pbobj.pbar.set_fraction(new_val)
    percVal = int(new_val * 100)
    percText = str(percVal) + "%"
    applicationEvent("progress bar to be updated", "bar")
    applicationEvent("progress to reach " + percText, "reliable")
    if percVal in [ 2, 8 ]:
        applicationEvent("unreliable progress to reach " + percText, "unreliable")
    
    # As this is a timeout function, return TRUE so that it
    # continues to get called
    return True

class ProgressBar:
    # Callback that toggles the text display within the progress
    # bar trough
    def toggle_show_text(self, widget, data=None):
        if widget.get_active():
            self.pbar.set_text("some text")
        else:
            self.pbar.set_text("")

    # Callback that toggles the activity mode of the progress
    # bar
    def toggle_activity_mode(self, widget, data=None):
        if widget.get_active():
            self.pbar.pulse()
        else:
            self.pbar.set_fraction(0.0)

    # Callback that toggles the orientation of the progress bar
    def toggle_orientation(self, widget, data=None):
        if self.pbar.get_orientation() == gtk.PROGRESS_LEFT_TO_RIGHT:
            self.pbar.set_orientation(gtk.PROGRESS_RIGHT_TO_LEFT)
        elif self.pbar.get_orientation() == gtk.PROGRESS_RIGHT_TO_LEFT:
            self.pbar.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)

    # Clean up allocated memory and remove the timer
    def destroy_progress(self, widget, data=None):
        gobject.source_remove(self.timer)
        self.timer = 0
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(True)

        self.window.connect("destroy", self.destroy_progress)
        self.window.set_title("ProgressBar")
        self.window.set_border_width(0)

        vbox = gtk.VBox(False, 5)
        vbox.set_border_width(10)
        self.window.add(vbox)
        vbox.show()
  
        # Create a centering alignment object
        align = gtk.Alignment(0.5, 0.5, 0, 0)
        vbox.pack_start(align, False, False, 5)
        align.show()

        # Create the ProgressBar
        self.pbar = gtk.ProgressBar()

        align.add(self.pbar)
        self.pbar.show()

        separator = gtk.HSeparator()
        vbox.pack_start(separator, False, False, 0)
        separator.show()

        # rows, columns, homogeneous
        entry = gtk.Entry()
        entry.set_name("Entry1")
        vbox.pack_start(entry, False, True, 0)

        # rows, columns, homogeneous
        entry2 = gtk.Entry()
        entry2.set_name("Entry2")
        vbox.pack_start(entry2, False, True, 0)

        # Add a button to exit the program
        button = gtk.Button("close")
        button.connect("clicked", self.destroy_progress)
        vbox.pack_start(button, False, False, 0)

        # This makes it so the button is the default.
        button.set_flags(gtk.CAN_DEFAULT)

        # This grabs this button to be the default button. Simply hitting
        # the "Enter" key will cause this button to activate.
        button.grab_default ()
        entry.show()
        entry2.show()
        button.show()

        self.window.show()
        # Add a timer callback to update the value of the progress bar
        self.timer = gobject.timeout_add (200, progress_timeout, self)

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ProgressBar()
    main()
