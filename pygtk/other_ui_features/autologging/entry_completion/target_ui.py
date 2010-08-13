#!/usr/bin/env python

import time
import pygtk
pygtk.require('2.0')
import gtk

class EntryCompletionExample:
    def __init__(self):
        window = gtk.Window()
        window.set_title("Entry Completion")
        window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox()
        label = gtk.Label('Type a, b, c or d\nfor completion')
        vbox.pack_start(label)
        entry = gtk.Entry()
        vbox.pack_start(entry)
        button = gtk.Button("Hello")
        vbox.pack_start(button)
        window.add(vbox)
        completion = gtk.EntryCompletion()
        self.liststore = gtk.ListStore(str)
        for s in ['apple', 'banana', 'cap', 'comb', 'color',
                  'dog', 'doghouse']:
            self.liststore.append([s])
        completion.set_model(self.liststore)
        completion.set_text_column(0)
        entry.set_completion(completion)
        completion.set_match_func(self.contains)
        window.show_all()

    def contains(self, completion, key, iter):
        text = completion.get_model().get_value(iter, 0)
        return key and key in text

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ee = EntryCompletionExample()
    main()
