#!/usr/bin/python
import gtk

class AboutDialog():
    
    BUG_BUTTON = 1
    DONATE_BUTTON = 2
    CLOSE_BUTTON = gtk.RESPONSE_NONE
    
    def __init__(self, parent_window):
        self._parent_window = parent_window

    def show(self):
        dialog = gtk.Dialog('The Dialog Title', self._parent_window)
        text = "Some text"
        about_label = gtk.Label(text)
        dialog.vbox.add(about_label)
        
        dialog.add_button('File a bug', AboutDialog.BUG_BUTTON)
        dialog.add_button('Donate', AboutDialog.DONATE_BUTTON)
        dialog.add_button('Close', AboutDialog.CLOSE_BUTTON)
        
        self._runDialog(dialog)
        
    def _responseCallback(self, dialog, result):
        dialog.hide()
        print "Result was", result    

    def _runDialog(self, dialog):
        dialog.connect("response", self._responseCallback)
        dialog.show_all()


if __name__ == "__main__":
    win = gtk.Window()
    dialog = AboutDialog(win)

    def clicked(*args):
        global dialog
        dialog.show()
    box = gtk.VBox()
    button = gtk.Button("hi - this button opens the about dialog")
    button.connect("clicked", clicked)
    box.add(button)

    win.set_deletable(True)

    win.connect("destroy", gtk.main_quit, None)

    win.add(box)

    win.show_all()
    gtk.main()
