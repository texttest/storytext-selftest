#!/usr/bin/python
import gtk

class MyDialog():
        
    def __init__(self, parent_window):
        self._parent_window = parent_window

    def show(self):
        dialog = gtk.Dialog('The Dialog Title', self._parent_window)
        label = gtk.Label("Some message")
        dialog.vbox.add(label)        
        dialog.add_button('Close', gtk.RESPONSE_CLOSE)
        dialog.set_has_separator(False)
        
        result = dialog.run()
        dialog.destroy()

if __name__ == "__main__":
    win = gtk.Window()
    dialog = MyDialog(win)

    box = gtk.VBox()

    model = gtk.ListStore(str)
    model.append([ "A Row" ])
    list = gtk.TreeView(model)
    list.set_name("The List")
    cell_renderer = gtk.CellRendererText()
    list.append_column(gtk.TreeViewColumn("Name", cell_renderer, text=0))

    def can_select(*args):
        global dialog
        dialog.show()
        return False
    list.get_selection().set_mode(gtk.SELECTION_MULTIPLE)

    list.get_selection().set_select_function(can_select)
    box.add(list)

    win.set_deletable(True)

    win.connect("destroy", gtk.main_quit, None)

    win.add(box)

    win.show_all()
    gtk.main()
