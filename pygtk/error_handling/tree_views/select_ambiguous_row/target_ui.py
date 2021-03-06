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

        # create a TreeStore with one string column to use as the model
        self.treestore = gtk.TreeStore(str, str)

        # we'll add some data now - 4 rows with 3 child rows each
        for parent in range(4):
            piter = self.treestore.append(None, ['parent %i' % parent, "bold"])
            for child in range(3):
                self.treestore.append(piter, ["<span foreground='red'>child %i" % child + "</span>", "" ])

        # create the TreeView using treestore
        self.treeview = gtk.TreeView(self.treestore)

        # create the TreeViewColumn to display the data
        self.tvcolumn = gtk.TreeViewColumn('Column 0')

        # add tvcolumn to treeview
        self.treeview.append_column(self.tvcolumn)

        # create a CellRendererText to render the data
        self.cell = gtk.CellRendererText()

        # add the cell to the tvcolumn and allow it to expand
        self.tvcolumn.pack_start(self.cell, True)

        # set the cell "markup" attribute to column 0 - retrieve marked-up text
        # from that column in treestore
        self.tvcolumn.add_attribute(self.cell, 'markup', 0)
        self.tvcolumn.add_attribute(self.cell, 'font', 1)

        # make it searchable
        self.treeview.set_search_column(0)
        self.treeview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        self.treeview.get_selection().connect("changed", self.selectionChanged)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)

        self.window.add(self.treeview)

        self.treeview.grab_focus()
        self.window.show_all()

    def selectionChanged(self, selection, *args):
        print "There are now", selection.count_selected_rows(), "rows selected."
        

def main():
    gtk.main()

if __name__ == "__main__":
    tvexample = BasicTreeViewExample()
    main()
