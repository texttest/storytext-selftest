#!/usr/bin/env python

# example frame.py

import pygtk
pygtk.require('2.0')
import gtk

class FrameExample:
    def __init__(self):
        # Create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Example")

        # Here we connect the "destroy" event to a signal handler 
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_size_request(300, 300)

        # Sets the border width of the window.
        window.set_border_width(10)

        # Create a Frame
        frame = gtk.Frame()
        box = gtk.VBox()
        window.add(box)
        box.pack_start(frame)

        # Set the frame's label
        frame.set_label("GTK Frame Widget")

        # Align the label at the right of the frame
        frame.set_label_align(1.0, 0.0)

        # Set the style of the frame
        frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
        frame.add(gtk.Label("A label"))
        
        frame2 = gtk.Frame()
        frame2.add(gtk.Label("Another Label"))
        box.pack_start(frame2)

        # Display the window
        window.show_all()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    FrameExample()
    main()
