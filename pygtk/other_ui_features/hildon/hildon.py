
import gtk

class CheckButton(gtk.ToggleButton):
    def get_name(self):
        return "HildonCheckButton"

class AppMenu(gtk.Dialog):
    def get_name(self):
        return "HildonAppMenu"
