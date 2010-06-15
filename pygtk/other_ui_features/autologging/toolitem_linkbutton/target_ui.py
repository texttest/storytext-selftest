#!/usr/bin/python

# ZetCode PyGTK tutorial 
#
# This example shows a toolbar
# widget
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009


import gtk


class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Example")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        toolbar = gtk.Toolbar()
        toolbar.set_style(gtk.TOOLBAR_ICONS)

        quittb = gtk.ToolButton(gtk.STOCK_QUIT)
        sep = gtk.SeparatorToolItem()

        linkButton = gtk.LinkButton("My Home Page", "My Home Page")
        alignment = gtk.Alignment()
        alignment.set(1.0, 1.0, 1.0, 1.0)
        width=7
        alignment.set_padding(width, width, 1, width)
        alignment.add(linkButton)
        toolItem = gtk.ToolItem()
        toolItem.add(alignment)
        toolItem.set_expand(True)
        toolbar.insert(toolItem, -1)
        toolbar.insert(sep, -1)
        toolbar.insert(quittb, -1)

        quittb.connect("clicked", gtk.main_quit)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(toolbar, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
       
PyApp()
gtk.main()
