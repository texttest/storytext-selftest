#!/usr/bin/env python
import gtk
class ConfirmDialog:
    def __init__(self, parent_window):
        self._parent_window = parent_window

    def askForConfirm(self):
        dialog = gtk.Dialog('Confirm', self._parent_window)
        text = "Are you sure you want to close the window?"
        dialog.vbox.add(gtk.Label(text))
        dialog.set_has_separator(False)
        dialog.add_button('Yes', gtk.RESPONSE_YES)
        dialog.add_button('No', gtk.RESPONSE_NO)
        dialog.show_all()
        result = dialog.run()
        ret = result == gtk.RESPONSE_YES
        dialog.hide()
        dialog.destroy()
        return ret
        

if __name__ == "__main__":
    win = gtk.Window()

    def close(*args):
        dialog = ConfirmDialog(win)
        if dialog.askForConfirm():
            gtk.main_quit()
        else:
            return not win.emit_stop_by_name("delete_event")

    win.set_deletable(True)

    win.connect("delete-event", close)

    win.show_all()
    gtk.main()
