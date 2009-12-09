#!/usr/bin/env python
#-*- coding: utf-8 -*-

import gtk

class MyApp(object):

   def __init__(self):
       win = gtk.Window()

       vbox = gtk.HBox()
       win.add(vbox)

       treeview = gtk.TreeView()
       column = gtk.TreeViewColumn("Column 1")
       treeview.append_column(column)
       vbox.pack_start(treeview)

       bt_quit = gtk.Button('Quit')
       bt_quit.connect('clicked', self.on_bt_quit_clicked)
       vbox.pack_start(bt_quit)

       win.show_all()

   def run(self):
       gtk.main()

   def on_bt_quit_clicked(self, *args):
       gtk.main_quit()

MyApp().run()
