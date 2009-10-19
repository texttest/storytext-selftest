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

    def make_pb(self, tvcolumn, cell, model, iter):
        stock = model.get_value(iter, 1)
        pb = self.treeview.render_icon(stock, gtk.ICON_SIZE_MENU, None)
        cell.set_property('pixbuf', pb)
        return

    def make_popup_menu(self):
        menu = gtk.Menu()
        menuItem = gtk.MenuItem("Colour Last Column")
        menu.append(menuItem)
        menuItem.connect("activate", self.change_colours, True)
        menuItem.show()
        menuItem2 = gtk.MenuItem("Clear Last Column Colour")
        menu.append(menuItem2)
        menuItem2.connect("activate", self.change_colours, False)
        menuItem2.show()
        return menu

    def show_popup_menu(self, treeview, event):
        if event.button == 3:
            pathInfo = treeview.get_path_at_pos(int(event.x), int(event.y))
            if pathInfo is not None:
                treeview.grab_focus()
                self.current_path = pathInfo[0]
                self.popup_menu.popup(None, None, None, event.button, event.time)
                treeview.stop_emission("button_press_event") # Disable default handler which auto-selects rows
                # Check PyUseCase can handle this...

    def change_colours(self, menuItem, value):
        iter = self.liststore.get_iter(self.current_path)
        self.liststore.set_value(iter, 3, value)

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.current_path = None
        self.window.set_title("TreeViewColumn Example")

        #self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(str, str, str, 'gboolean')

        # create the TreeView using liststore
        self.treeview = gtk.TreeView(self.liststore)
        self.treeview.get_selection().set_mode(gtk.SELECTION_NONE)
        self.popup_menu = self.make_popup_menu()

        # create the TreeViewColumns to display the data
        self.tvcolumn = gtk.TreeViewColumn('Pixbuf and Text')
        self.tvcolumn1 = gtk.TreeViewColumn('Text Only')

        # add a row with text and a stock item - color strings for
        # the background
        self.liststore.append(['Open', gtk.STOCK_OPEN, 'Open a File', True])
        self.liststore.append(['New', gtk.STOCK_NEW, 'New File', True])
        self.liststore.append(['Print', gtk.STOCK_PRINT, 'Print File', False])

        # add columns to treeview
        self.treeview.append_column(self.tvcolumn)
        self.treeview.append_column(self.tvcolumn1)

        # create a CellRenderers to render the data
        self.cellpb = gtk.CellRendererPixbuf()
        self.cell = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()

        # set background color property
        self.cellpb.set_property('cell-background', 'yellow')
        self.cell.set_property('cell-background', 'cyan')
        self.cell1.set_property('cell-background', 'pink')


        # add the cells to the columns - 2 in the first
        self.tvcolumn.pack_start(self.cellpb, False)
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn1.pack_start(self.cell1, True)

        # set the cell attributes to the appropriate liststore column
        # GTK+ 2.0 doesn't support the "stock_id" property
        if gtk.gtk_version[1] < 2:
            self.tvcolumn.set_cell_data_func(self.cellpb, self.make_pb)
        else:
            self.tvcolumn.set_attributes(self.cellpb, stock_id=1)
        self.tvcolumn.set_attributes(self.cell, text=0)
        self.tvcolumn1.set_attributes(self.cell1, text=2,
                                      cell_background_set=3)

        # make treeview searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)
        self.treeview.connect("button_press_event", self.show_popup_menu)

        self.window.add(self.treeview)

        self.window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tvcexample = TreeViewColumnExample()
    main()
