#!/usr/bin/python
import gtk

class MyDialog():
        
    def __init__(self, parent_window):
        self._parent_window = parent_window

    def show(self):
        dialog = gtk.Dialog('The Dialog Title', self._parent_window)
        label = gtk.Label("Enter some text in the dialog")
        dialog.vbox.add(label)
        dialog.set_has_separator(False)
        entry = gtk.Entry()
        entry.set_name("Dialog Text")
        dialog.vbox.add(entry)
        
        dialog.add_button('Close', gtk.RESPONSE_CLOSE)
        
        result = dialog.run()
        dialog.destroy()

if __name__ == "__main__":
    win = gtk.Window()
    dialog = MyDialog(win)

    def clicked(*args):
        global dialog
        dialog.show()
    box = gtk.VBox()
    label = gtk.Label("Enter some text in the main window")
    box.add(label)
    entry = gtk.Entry()
    entry.set_name("Main Text")
    box.add(entry)
    button = gtk.Button("hi - this button opens the dialog")
    button.connect("clicked", clicked)
    box.add(button)

    win.set_deletable(True)

    win.connect("destroy", gtk.main_quit, None)

    win.add(box)

    win.show_all()
    gtk.main()
