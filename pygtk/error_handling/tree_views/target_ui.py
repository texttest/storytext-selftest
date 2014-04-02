#!/usr/bin/env python

# example treemodelfilter.py

import pygtk
pygtk.require('2.0')
import gtk

bugdata="""120595 NEW Custom GtkTreeModelFilter wrappers need
121339 RESO dsextras.py installation directory is incorrect
122569 NEW gtk.Window derived class segfaults
123014 NEW PyGtk build problem on Win32 using the 'distutils' approach.
123037 NEW gtk.ListStore.set_column_types is missing
123456 RESO ItemFactory.create_items and <ImageItem> bug
123458 NEED pygtk does not wrap all of gdk-pixbuf
124181 NEED Python Shell inside a gtk GUI
138163 VERI NOTA gtk.main_iteration(TRUE) unblocks every .1 seconds
138619 UNCO codegen/definitions.py could use some refactoring
138804 UNCO In gtk2.4, gdk_font_get_display and gdk_pixmap_lookup is ..."""

class TreeModelFilterExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("TreeModelFilter Example")

        self.window.set_size_request(400, 400)

        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(int, str, str)

        self.modelfilter = self.liststore.filter_new()

        # create the TreeView
        self.treeview = gtk.TreeView()

        # create the TreeViewColumns to display the data
        self.treeview.columns = [None]*3
        self.treeview.columns[0] = gtk.TreeViewColumn('Bug No.')
        self.treeview.columns[1] = gtk.TreeViewColumn('Status')
        self.treeview.columns[2] = gtk.TreeViewColumn('Description')

        # add bug data
        self.states = []
        for line in bugdata.split('\n'):
            l = line.split()
            self.liststore.append([int(l[0]), l[1], ' '.join(l[2:])])
            if not l[1] in self.states:
                self.states.append(l[1])

        self.show_states = self.states[:]
        self.modelfilter.set_visible_func(self.visible_cb, self.show_states)

        self.treeview.set_model(self.modelfilter)

        for n in range(3):
            # add columns to treeview
            self.treeview.append_column(self.treeview.columns[n])
            # create a CellRenderers to render the data
            self.treeview.columns[n].cell = gtk.CellRendererText()
            # add the cells to the columns
            self.treeview.columns[n].pack_start(self.treeview.columns[n].cell,
                                                True)
            # set the cell attributes to the appropriate liststore column
            self.treeview.columns[n].set_attributes(
                self.treeview.columns[n].cell, text=n)
            self.treeview.columns[n].set_clickable(True)
            self.treeview.columns[n].connect("clicked", self.column_clicked)

        # make treeview searchable
        self.treeview.set_search_column(3)

        # make ui layout
        self.vbox = gtk.VBox()
        self.scrolledwindow = gtk.ScrolledWindow()
        self.bbox = gtk.HButtonBox()
        self.vbox.pack_start(self.scrolledwindow)
        self.vbox.pack_start(self.bbox, False)
        # create toggle buttons to select filtering based on
        # bug state and set buttons active
        for state in self.states:
            b = gtk.ToggleButton(state)
            self.bbox.pack_start(b)
            b.set_active(True)
            b.connect('toggled', self.check_buttons)

        self.scrolledwindow.add(self.treeview)
        self.window.add(self.vbox)

        self.treeview.grab_focus()
        self.window.show_all()
        return

    def column_clicked(self, column):
        ix = self.treeview.columns.index(column)
        column_data = []
        self.liststore.foreach(self.collect_column_data, (ix, column_data))
        sorted_data = sorted(column_data)
        new_order = []
        for item in sorted_data:
            orig_index = column_data.index(item)
            while orig_index in new_order:
                orig_index = column_data.index(item, orig_index + 1)
            new_order.append(orig_index)
        self.liststore.reorder(new_order)

    def collect_column_data(self, model, path, iter, userdata):
        ix, column_data = userdata
        column_data.append(model.get_value(iter, ix))

    # visibility determined by state matching active toggle buttons
    def visible_cb(self, model, iter, data):
        return model.get_value(iter, 1) in data

    # build list of bug states to show and then refilter
    def check_buttons(self, tb):
        del self.show_states[:]
        for b in self.bbox.get_children():
            if b.get_active():
                self.show_states.append(b.get_label())
        self.modelfilter.refilter()
        return

def main():
    gtk.main()

if __name__ == "__main__":
    tmfexample = TreeModelFilterExample()
    main()
