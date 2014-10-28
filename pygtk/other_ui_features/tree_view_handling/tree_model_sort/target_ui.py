#!/usr/bin/env python

# example treemodelsort.py

import pygtk
pygtk.require('2.0')
import gtk

class TreeModelSortExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def add_row(self, b):
        # add a row of random ints
        model = self.window.sm.get_model()
        i0 = model.append([ self.num, self.num + 1, self.num + 2 ])
        self.num += 3
        sel = self.window.tv.get_selection()
        i1 = self.window.sm.convert_child_iter_to_iter(None, i0)
        sel.select_iter(i1)

    def __init__(self):
        # create a liststore with three int columns
        self.liststore = gtk.ListStore(int, int, int)
        self.num = 0

        # Create new windows
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        win.set_title("TreeModelSort Example")
        win.set_size_request(220, 200)
        win.connect("delete_event", self.delete_event)
        win.vbox = gtk.VBox()
        win.add(win.vbox)
        win.sw = gtk.ScrolledWindow()
        win.sm = gtk.TreeModelSort(self.liststore)
        # Set sort column
        win.sm.set_sort_column_id(0, gtk.SORT_DESCENDING)
        win.tv = gtk.TreeView(win.sm)
        win.vbox.pack_start(win.sw)
        win.b = gtk.Button('Add a Row')
        win.b.connect('clicked', self.add_row)
        win.vbox.pack_start(win.b, False)
        win.sw.add(win.tv)
        win.tv.column = [None]*3
        win.tv.column[0] = gtk.TreeViewColumn('Rem 0')
        win.tv.column[1] = gtk.TreeViewColumn('Rem 1')
        win.tv.column[2] = gtk.TreeViewColumn('Rem 2')
        win.tv.cell = [None]*3
        for i in range(3):
            win.tv.cell[i] = gtk.CellRendererText()
            win.tv.append_column(win.tv.column[i])
            win.tv.column[i].set_sort_column_id(i)
            win.tv.column[i].pack_start(win.tv.cell[i], True)
            win.tv.column[i].set_attributes(win.tv.cell[i], text=i)
        win.show_all()
        self.window = win

def main():
    gtk.main()

if __name__ == "__main__":
    tmsexample = TreeModelSortExample()
    main()
