#!/usr/bin/env python
import gtk

class QuitDialog(object):

    def __init__(self):
        self._dialog = gtk.Dialog()
        self._dialog.connect("destroy", self._destroyed)

        self._dialog.add_button("Quit", gtk.RESPONSE_ACCEPT)
        self._dialog.connect("response", self.respond)

        self._dialog.show_all()

    def respond(self, widget, response):
        if response == gtk.RESPONSE_ACCEPT:
            self._dialog.destroy()

    def _destroyed(self, widget, data=None):
        gtk.main_quit()

QuitDialog()
gtk.main()
