#!/usr/bin/python
import gtk

class MyDialog():
        
    def __init__(self, parent_window):
        self._parent_window = parent_window
        self.handler = None

    def show(self):
        dialog = gtk.Dialog('The Dialog Title', self._parent_window)
        
        dialog.add_button('Button', 42)
        dialog.add_button('Close', gtk.RESPONSE_CLOSE)
        self.handler = dialog.connect('response', self.respond)
        dialog.connect('response', self.closeRespond)
        dialog.show_all()

    def respond(self, dialog, response, *args):
        if response == 42:
            if dialog.handler_is_connected(self.handler):
                print "Disconnecting!"
                dialog.disconnect(self.handler)

    def closeRespond(self, dialog, response, *args):
        if response == gtk.RESPONSE_CLOSE:
            dialog.destroy()


if __name__ == "__main__":
    win = gtk.Window()
    dialog = MyDialog(win)

    def clicked(*args):
        global dialog
        dialog.show()
    box = gtk.VBox()
    button = gtk.Button("hi - this button opens the dialog")
    button.connect("clicked", clicked)
    box.add(button)

    win.set_deletable(True)

    win.connect("destroy", gtk.main_quit, None)

    win.add(box)

    win.show_all()
    gtk.main()
