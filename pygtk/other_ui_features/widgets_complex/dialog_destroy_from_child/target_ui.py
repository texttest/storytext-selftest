#!/usr/bin/env python
import gtk

class LoginDialog(object):

    def __init__(self):
        self._dialog = gtk.Dialog()
        self._dialog.connect("destroy", self._destroyed)

        login_button = gtk.Button("Log in")
        login_button.connect("clicked", self.login_clicked)
        self._dialog.action_area.pack_end(login_button, expand=False)

        self._dialog.show_all()

    def login_clicked(self, widget, data=None):
        self._dialog.destroy()

    def _destroyed(self, widget, data=None):
        gtk.main_quit()

LoginDialog()
gtk.main()
