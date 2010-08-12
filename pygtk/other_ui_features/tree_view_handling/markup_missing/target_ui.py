#!/usr/bin/env python

# example basictreeview.py

import pygtk
pygtk.require('2.0')
import gtk

class BasicTreeViewExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Basic TreeView Example")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        self.liststore = gtk.ListStore(str, str)

        self.liststore.append([ "<b>Bold Text</b>", "<i>Italic Text</i>" ])
        self.liststore.append([ "<u>Underline Text</u>", None ])

        # create the TreeView using liststore
        self.treeview = gtk.TreeView(self.liststore)

        self.tvcolumn = gtk.TreeViewColumn('Column 0')
        self.treeview.append_column(self.tvcolumn)
        self.cell = gtk.CellRendererText()
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn.add_attribute(self.cell, 'markup', 0)

        self.tvcolumn2 = gtk.TreeViewColumn('Column 1')
        self.treeview.append_column(self.tvcolumn2)
        self.treeview.get_selection().set_mode(gtk.SELECTION_NONE)
        self.cell2 = gtk.CellRendererText()
        self.tvcolumn2.pack_start(self.cell2, True)
        self.tvcolumn2.add_attribute(self.cell2, 'markup', 1)

        self.window.add(self.treeview)

        self.window.show_all()
        

def main():
    gtk.main()

if __name__ == "__main__":
    tvexample = BasicTreeViewExample()
    main()
