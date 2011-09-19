#!/usr/bin/env python

import time
import pygtk
pygtk.require('2.0')
import gtk

class Example:
    def __init__(self):
        window = gtk.Window()
        window.set_title("Naming")
        window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox()
        label = gtk.Label('First Name')
        vbox.pack_start(label)
        entry = gtk.Entry()
        entry.connect("activate", self.activateEntry)
        entry.set_name("First Name Entry")
        vbox.pack_start(entry)
        label = gtk.Label('Last Name')
        vbox.pack_start(label)
        entry = gtk.Entry()
        entry.connect("activate", self.activateEntry)
        vbox.pack_start(entry)
        window.add(vbox)
        window.show_all()

    def activateEntry(self, entry, *args):
        entry.set_sensitive(False)

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ee = Example()
    main()
