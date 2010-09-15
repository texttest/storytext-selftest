#!/usr/bin/env python


import gtk, os

def startDialogWithWidget():
    dialog = gtk.Dialog("Save Dialog with Widget", buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                                            gtk.STOCK_SAVE, gtk.RESPONSE_OK))
    fileChooser = gtk.FileChooserWidget(gtk.FILE_CHOOSER_ACTION_SAVE)
    dialog.vbox.pack_start(fileChooser, expand=True, fill=True)
    checkBox = gtk.CheckButton("Make the file readonly")
    dialog.vbox.pack_start(checkBox, expand=False, fill=False)
    
    dialog.set_default_response(gtk.RESPONSE_OK)
    dialog.connect("response", dialogRespond, fileChooser)
    dialog.set_modal(True)
    dialog.show_all()


def dialogRespond(dialog, response, fileChooser):
    if response == gtk.RESPONSE_OK:
        print 'Saving to', fileChooser.get_filename()
        gtk.main_quit()
    elif response == gtk.RESPONSE_CANCEL:
        print 'Closed, nothing will be saved'
        startDialogWithWidget()
    dialog.destroy()


dialog = gtk.FileChooserDialog("Save Dialog",
                               None,
                               gtk.FILE_CHOOSER_ACTION_SAVE,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_SAVE, gtk.RESPONSE_OK))

dialog.set_default_response(gtk.RESPONSE_OK)
dialog.connect("response", dialogRespond, dialog)
dialog.set_modal(True)
dialog.show_all()
gtk.main()
