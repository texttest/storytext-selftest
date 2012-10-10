import gtk

if __name__ == "__main__":
    counter = 0
    win = gtk.Window()
    def clicked(widget, frame):
        global counter
        counter += 1
        frame.set_label("Current count: " + str(counter))
    box = gtk.VBox()
    frame = gtk.Frame("Current count: 0 ")
    button = gtk.Button("Count up")
    button.connect("clicked", clicked, frame)
    frame.add(button)
    box.add(frame)

    win.set_deletable(True)
    win.connect("destroy", gtk.main_quit, None)

    win.add(box)

    win.show_all()
    gtk.main()
