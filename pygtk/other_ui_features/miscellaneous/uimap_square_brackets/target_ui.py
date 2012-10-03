#!/usr/bin/python


import gtk

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("The title [with nasty brackets]")
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
       
PyApp()
gtk.main()
