#!/usr/bin/python
import gtk, gobject, time, sys

def idle_handler(*args):
    time.sleep(0.1)
    return True

class MyDialog():
        
    def __init__(self, parent_window):
        self._parent_window = parent_window

    def show(self):
        dialog = gtk.Dialog('The Dialog Title', self._parent_window)
        button = gtk.CheckButton("check button 1")
        dialog.vbox.add(button)
        
        dialog.add_button('Close', gtk.RESPONSE_CLOSE)
        dialog.connect('destroy', self.destroyed)
        result = dialog.run()
        dialog.destroy()

    def destroyed(self, dialog):
        print "The dialog was actually destroyed!"
        
if __name__ == "__main__":
    gobject.idle_add(idle_handler, priority=gobject.PRIORITY_DEFAULT_IDLE + 20)
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
