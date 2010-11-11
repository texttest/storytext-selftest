
import gtk

class CheckButton(gtk.ToggleButton):
    def get_name(self):
        return "HildonCheckButton"

class AppMenu(gtk.Dialog):
    def get_name(self):
        return "HildonAppMenu"

class GtkTreeView(gtk.TreeView):
    pass

class StackableWindow(gtk.Window):
    def set_edit_toolbar(self, toolbar):
        pass
    
