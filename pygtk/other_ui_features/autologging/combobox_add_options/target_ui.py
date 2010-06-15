#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ComboBoxExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        button = gtk.Button("Add More Pies!")
        combobox = gtk.combo_box_new_text()
        combobox.set_name("Pie List")
        combobox.append_text('Select a pie:')
        combobox.append_text('Apple')
        combobox.append_text('Cherry')
        combobox.connect('changed', self.changed_cb)
        combobox.set_active(0)
        button.connect("clicked", self.addPies, combobox)
        box = gtk.HBox()
        box.pack_start(button)
        box.pack_start(combobox)
        window.add(box)
        window.show_all()
        return

    def addPies(self, button, combobox):
        combobox.append_text('Blueberry')
        combobox.append_text('Grape')
        combobox.append_text('Peach')
        combobox.append_text('Raisin')

    def changed_cb(self, combobox):
        model = combobox.get_model()
        index = combobox.get_active()
        if index:
            print 'I like', model[index][0], 'pie'
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = ComboBoxExample()
    main()
