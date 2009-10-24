#!/usr/bin/env python


import gtk, os

dialog = gtk.FileChooserDialog("Save..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_SAVE,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_SAVE, gtk.RESPONSE_OK))
dialog.set_default_response(gtk.RESPONSE_OK)
dialog.add_shortcut_folder(os.path.abspath("sampledir/subdir2"))
dialog.set_current_folder(os.path.abspath("sampledir/subdir"))

response = dialog.run()
if response == gtk.RESPONSE_OK:
    print 'Saving to', dialog.get_filename()
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, nothing will be saved'
dialog.destroy()
