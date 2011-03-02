#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

if __name__ == "__main__":
    window = gtk.Window()
    window.set_title("Example")
    window.connect('destroy', lambda w: gtk.main_quit())
    hbox = gtk.HBox()
    button1 = gtk.Button("Click me!")
    hbox.pack_start(button1)
    button2 = gtk.Button("Click me!")
    button2.set_sensitive(False)
    hbox.pack_start(button2)
    window.add(hbox)
    window.show_all()
    gtk.main()
