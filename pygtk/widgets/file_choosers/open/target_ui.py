#!/usr/bin/env python


import gtk, os

def folderChanged(dialog, *args):
    folder = dialog.get_current_folder()
    files = os.listdir(folder)
    files.sort()
    dialog.select_filename(os.path.join(folder, files[-1]))

def dialogRespond(dialog, response, *args):
    if response == gtk.RESPONSE_OK:
        print dialog.get_filename(), 'selected'
    elif response == gtk.RESPONSE_CANCEL:
        print 'Closed, no files selected'
    dialog.destroy()
    gtk.main_quit()
    
dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
dialog.set_default_response(gtk.RESPONSE_OK)
dialog.add_shortcut_folder(os.path.abspath("sampledir/subdir2"))
dialog.set_current_folder(os.path.abspath("sampledir/subdir"))
dialog.connect("current-folder-changed", folderChanged)
dialog.connect("response", dialogRespond)
dialog.set_modal(True)
dialog.show()
gtk.main()

