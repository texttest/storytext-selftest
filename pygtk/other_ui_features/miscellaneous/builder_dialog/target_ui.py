#!/usr/bin/env python
import gtk
builder = gtk.Builder()
builder.add_from_file('target_ui.ui')

dialog = builder.get_object('test_dialog')

def respond(dialog, response):
    if response == 0:
        print "Hello!"
    else:
        dialog.destroy()
        gtk.main_quit()

dialog.connect('response', respond)
dialog.show()
gtk.main()
