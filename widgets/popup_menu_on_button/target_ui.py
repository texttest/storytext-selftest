#!/usr/bin/env python

# example menu.py

import pygtk
pygtk.require('2.0')
import gtk

class MenuExample:
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("GTK Menu Test")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

        # This is the root menu, and will be the label
        # displayed on the menu bar.  There won't be a signal handler attached,
        # as it only pops up the rest of the menu when pressed.
        root_menu = gtk.MenuItem("Root Menu")

        root_menu.show()

        # Now we specify that we want our newly created "menu" to be the
        # menu for the "root menu"
        root_menu.set_submenu(self.create_menu())

        # A vbox to put a menu and a button in:
        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        # Create a menu-bar to hold the menus and add it to our main window
        menu_bar = gtk.MenuBar()
        vbox.pack_start(menu_bar, False, False, 2)
        menu_bar.show()

        # Create a button to which to attach menu as a popup
        button = gtk.Button("press me")
        popup_menu = self.create_menu()
        button.connect("button-press-event", self.button_press, popup_menu)
        vbox.pack_end(button, True, True, 2)
        button.show()

        # And finally we append the menu-item to the menu-bar -- this is the
        # "root" menu-item I have been raving about =)
        menu_bar.append (root_menu)

        # always display the window as the last step so it all splashes on
        # the screen at once.
        window.show()

    def create_menu(self):
        # Init the menu-widget, and remember -- never
        # show() the menu widget!! 
        # This is the menu that holds the menu items, the one that
        # will pop up when you click on the "Root Menu" in the app
        menu = gtk.Menu()

        # Next we make a little loop that makes three menu-entries for
        # "test-menu".  Notice the call to gtk_menu_append.  Here we are
        # adding a list of menu items to our menu.  Normally, we'd also
        # catch the "clicked" signal on each of the menu items and setup a
        # callback for it, but it's omitted here to save space.
        for i in range(3):
            # Copy the names to the buf.
            buf = "Test-undermenu - %d" % i

            # Create a new menu-item with a name...
            menu_items = gtk.MenuItem(buf)

            # ...and add it to the menu.
            menu.append(menu_items)

	    # Do something interesting when the menuitem is selected
	    menu_items.connect("activate", self.menuitem_response, buf)
            
            # Show the widget
            menu_items.show()
        return menu

    # Respond to a button-press by posting a menu passed in as widget.
    def button_press(self, button, event, menu):
        if event.button == 3:
            menu.popup(None, None, None, event.button, event.time)
            # Tell calling code that we have handled this event the buck
            # stops here.
            button.emit_stop_by_name("button-press-event")
    
    # Print a string when a menu item is selected
    def menuitem_response(self, widget, string):
        print "%s" % string

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    MenuExample()
    main()
