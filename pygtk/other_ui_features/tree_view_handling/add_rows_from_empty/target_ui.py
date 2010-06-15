#!/usr/bin/env python

import os, stat, time, sys
import pygtk
pygtk.require('2.0')
import gtk, gobject

filexpm = [
    "12 12 3 1",
    "  c #000000",
    ". c #ffff04",
    "X c #b2c0dc",
    "X        XXX",
    "X ...... XXX",
    "X ......   X",
    "X .    ... X",
    "X ........ X",
    "X .   .... X",
    "X ........ X",
    "X .     .. X",
    "X ........ X",
    "X .     .. X",
    "X ........ X",
    "X          X"
    ]
filepb = gtk.gdk.pixbuf_new_from_xpm_data(filexpm)

class FileListingCellDataExample:
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
 
    def __init__(self): 
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
 
        self.window.set_size_request(400, 300)
        self.window.set_title("Basic TreeView Example")
        self.window.connect("delete_event", self.delete_event)
 
        listmodel = gtk.ListStore(str)
 
        # create the TreeView
        self.treeview = gtk.TreeView(listmodel)
 
        # create the TreeViewColumns to display the data
        cell = gtk.CellRendererText()
        self.tvcolumn = gtk.TreeViewColumn("Name", cell)
        self.tvcolumn.set_cell_data_func(cell, self.file_name) 
        self.treeview.append_column(self.tvcolumn)

        self.scrolledwindow = gtk.ScrolledWindow()
        self.scrolledwindow.add(self.treeview)
        box = gtk.VBox()
        box.pack_start(self.scrolledwindow)
        button = gtk.Button("Add File")
        button.connect("clicked", self.add_file)
        box.pack_start(button)
        self.window.add(box)
 
        self.window.show_all()
        return

    def file_name(self, column, cell, model, iter):
        cell.set_property("text", model.get_value(iter, 0))
                
    def add_file(self, *args):
        self.treeview.get_model().append([ "The File" ])

def main():
    gtk.main()

if __name__ == "__main__":
    flcdexample = FileListingCellDataExample()
    main()
