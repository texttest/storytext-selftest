#!/usr/bin/env python

# example treeviewcolumn.py

import pygtk
pygtk.require('2.0')
import gtk

class TreeViewColumnExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def make_popup_menu(self):
        menu = gtk.Menu()
        menuItem = gtk.MenuItem("Add New Row")
        menu.append(menuItem)
        menuItem.connect("activate", self.add_row)
        menuItem.show()
        return menu

    def add_row(self, *args):
        iters = []
        def addSelIter(model, path, iter):
            iters.append(iter)
            
        self.treeview.get_selection().selected_foreach(addSelIter)
        newIter = self.liststore.insert_after(iters[-1], [ "" ])
        path = self.liststore.get_path(newIter)
        column = self.treeview.get_column(0)
        self.treeview.set_cursor(path, column, start_editing=True)

    def show_popup_menu(self, treeview, event):
        if event.button == 3:
            pathInfo = treeview.get_path_at_pos(int(event.x), int(event.y))
            if pathInfo is not None:
                treeview.grab_focus()
                self.current_path = pathInfo[0]
                self.popup_menu.popup(None, None, None, event.button, event.time)
                treeview.stop_emission("button_press_event") # Disable default handler which auto-selects rows

    def editText(self, cell, path, newText):
        self.liststore[path][0] = newText
        
    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.current_path = None
        self.window.set_title("TreeViewColumn Example")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(str)

        # create the TreeView using liststore
        self.treeview = gtk.TreeView(self.liststore)
        self.treeview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        self.popup_menu = self.make_popup_menu()

        # create the TreeViewColumns to display the data
        self.tvcolumn = gtk.TreeViewColumn('Text')

        # add a row with text and a stock item - color strings for
        # the background
        self.liststore.append(['The Row'])

        # add columns to treeview
        self.treeview.append_column(self.tvcolumn)

        self.cell = gtk.CellRendererText()
        self.cell.set_property('editable', True)
        self.cell.connect('edited', self.editText)

        # add the cells to the columns - 2 in the first
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn.set_attributes(self.cell, text=0)

        # Allow drag and drop reordering of rows
        self.treeview.connect("button_press_event", self.show_popup_menu)

        self.window.add(self.treeview)

        self.treeview.grab_focus()
        self.window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tvcexample = TreeViewColumnExample()
    main()
