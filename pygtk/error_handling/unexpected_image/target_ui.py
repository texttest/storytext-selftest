#!/usr/bin/env python
#-*- coding: utf-8 -*-

import gtk

class MyApp(object):

   def __init__(self):
       win = gtk.Window()

       vbox = gtk.HBox()
       win.add(vbox)

       button = gtk.Button()
       button.set_image(gtk.CellView()) # hildon.CheckButton works a bit like this
       vbox.pack_start(button)

       bt_quit = gtk.Button('Quit')
       bt_quit.connect('clicked', self.on_bt_quit_clicked)
       vbox.pack_start(bt_quit)

       win.set_focus(bt_quit)
       win.show_all()
       win.resize(100,100)

   def run(self):
       gtk.main()

   def on_bt_quit_clicked(self, *args):
       gtk.main_quit()

MyApp().run()
