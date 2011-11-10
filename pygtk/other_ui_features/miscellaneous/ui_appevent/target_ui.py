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
from storytext import applicationEvent

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("App event")
        applicationEvent("application to start")
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
       
PyApp()
gtk.main()
