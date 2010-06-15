import gtk

win = gtk.Window()
but = gtk.Button("Hellooo")

win.add(but)
win.show_all()

def quit_win(widget, e):
    widget.hide()
    gtk.main_quit()

win.connect("delete-event", quit_win)

gtk.main()
