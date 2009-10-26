#!/usr/bin/env python


import gtk, os

def status(checkBox):
    if checkBox.get_active():
        return "readonly file"
    else:
        return "writeable file"

dialog = gtk.Dialog("Save..", buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                       gtk.STOCK_SAVE, gtk.RESPONSE_OK))
dialog.set_name("The Save Dialog")
fileChooser = gtk.FileChooserWidget(gtk.FILE_CHOOSER_ACTION_SAVE)
dialog.vbox.pack_start(fileChooser, expand=True, fill=True)
checkBox = gtk.CheckButton("Make the file readonly")
dialog.vbox.pack_start(checkBox, expand=False, fill=False)

dialog.set_default_response(gtk.RESPONSE_OK)
fileChooser.add_shortcut_folder(os.path.abspath("sampledir/subdir2"))
fileChooser.set_current_folder(os.path.abspath("sampledir/subdir"))
dialog.show_all()

response = dialog.run()
if response == gtk.RESPONSE_OK:
    print 'Saving', status(checkBox), 'to', fileChooser.get_filename()
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, nothing will be saved'
dialog.destroy()
