#!/usr/bin/env python


import gtk, os

dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
dialog.set_default_response(gtk.RESPONSE_OK)
dialog.set_current_folder(os.path.abspath("sampledir"))

response = dialog.run()
if response == gtk.RESPONSE_OK:
    print dialog.get_filename(), 'selected'
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, no files selected'
dialog.destroy()
