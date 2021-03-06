#!/usr/bin/python
import gtk

class AboutDialog():
    
    BUG_BUTTON = 42 # something else...
    DONATE_BUTTON = gtk.RESPONSE_NONE
    CLOSE_BUTTON = gtk.RESPONSE_CLOSE
    
    def __init__(self, parent_window):
        self._parent_window = parent_window

    def show(self):
        dialog = gtk.Dialog('The Dialog Title', self._parent_window)
        text = "Some text"
        self.about_label = gtk.Label(text)
        dialog.vbox.add(self.about_label)
        
        dialog.add_button('File a bug', AboutDialog.BUG_BUTTON)
        dialog.add_button('Donate', AboutDialog.DONATE_BUTTON)
        dialog.add_button('Close', AboutDialog.CLOSE_BUTTON)
        dialog.set_has_separator(False)

        self._runDialog(dialog)
                
    def _runDialog(self, dialog):
        result = dialog.run()
        self.about_label.set_text("Latest result was " + repr(result))    
        if result == self.CLOSE_BUTTON:
            dialog.hide()
        else:
            self._runDialog(dialog)


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
