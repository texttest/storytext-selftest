#!/usr/bin/env python

# example paned.py

import pygtk
pygtk.require('2.0')
import gtk, gobject

class PanedExample:
    # Create the list of "messages"
    def create_list(self):
        # Create a new scrolled window, with scrollbars only if needed
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        model = gtk.ListStore(gobject.TYPE_STRING)
        tree_view = gtk.TreeView(model)
        scrolled_window.add_with_viewport (tree_view)
        tree_view.show()

        # Add some messages to the window
        for i in range(10):
            msg = "Message #%d" % i
            iter = model.append()
            model.set(iter, 0, msg)

        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Messages", cell, text=0)
        tree_view.append_column(column)
        tree_view.get_selection().connect("changed", self.selection_changed)

        return scrolled_window
   
    def selection_changed(self, selection, *args):
        selection.selected_foreach(self.set_text)

    def set_text(self, model, path, iter):
        messageText = "Now Showing:\n" + model.get_value(iter, 0) + "\n"
        self.buffer.set_text(messageText)
   
    # Create a scrolled text area that displays a "message"
    def create_text(self):
        view = gtk.TextView()
        self.buffer = view.get_buffer()
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolled_window.add(view)
        self.buffer.set_text("No message selected.\n")
        scrolled_window.show_all()
        return scrolled_window

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Paned Windows")
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_border_width(10)
        window.set_size_request(450, 400)

        # create a vpaned widget and add it to our toplevel window
        vpaned = gtk.VPaned()
        window.add(vpaned)
        vpaned.show()

        # Now create the contents of the two halves of the window
        list = self.create_list()
        vpaned.add1(list)
        list.show()

        text = self.create_text()
        vpaned.add2(text)
        text.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    PanedExample()
    main()
