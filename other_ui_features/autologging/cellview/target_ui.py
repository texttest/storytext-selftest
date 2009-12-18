#!/usr/bin/env python

import time
import pygtk
pygtk.require('2.0')
import gtk

class Example:
    def __init__(self):
        window = gtk.Window()
        window.set_title("Example")
        window.connect('destroy', lambda w: gtk.main_quit())
        cellview = gtk.CellView()
        model = gtk.ListStore(str)
        model.append([ "Cell View Text "])
        cell = gtk.CellRendererText()
        cellview.set_model(model)
        cellview.pack_start(cell)
        cellview.set_attributes(cell, text=0)
        cellview.set_displayed_row((0,))
        window.add(cellview)
        window.show_all()
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ee = Example()
    main()
