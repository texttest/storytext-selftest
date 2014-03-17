#!/usr/bin/env python

import gtk, os

mydir = os.path.dirname(os.path.abspath(__file__))
builder = gtk.Builder()
builder.add_from_file(os.path.join(mydir, 'target_ui.ui'))

model = builder.get_object('tree_model')
def activate(col, path, column):
    row = model[path]
    print row[0], row[1]
builder.get_object('treeview').connect('row-activated', activate)

dialog = builder.get_object('test_dialog')

dialog.connect('response', gtk.main_quit)
dialog.show()
gtk.main()
