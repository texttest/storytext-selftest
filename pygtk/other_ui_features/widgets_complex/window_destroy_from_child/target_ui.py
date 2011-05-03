#!/usr/bin/env python2
import gtk

def button_clicked(self, widget, data=None):
    window.destroy()

window = gtk.Window()
window.connect("destroy", gtk.main_quit)

button = gtk.Button("Quit")
button.connect("clicked", button_clicked, None)

window.add(button)
window.show_all()

gtk.main()
