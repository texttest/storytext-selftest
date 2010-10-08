import gtk,gobject

"""Returns a ListStore with one Row per Network Setting"""

store = gtk.ListStore(str, gobject.TYPE_BOOLEAN)
        
store.append(["Hello", False])
store.append(["Hello1", True])

# sorting
store.set_sort_column_id(0, gtk.SORT_ASCENDING)

view = gtk.TreeView(store)
view.set_border_width(5)

def boolean_func(column, cell, model, iter):
    if model.get_value(iter, 1):
	stock_id = 'gtk-yes'
    else:
	stock_id = 'gtk-no'
    cell.set_property('stock-id', stock_id)

launch_cell = gtk.CellRendererPixbuf()
launch_cell.set_fixed_size(100, 50)
view.insert_column_with_data_func(1, 'Launch', launch_cell, boolean_func)
 
#view.connect('row-activated', self._rowActivatedCallback)
view.set_search_column(0)
#tvcolumn.set_sort_column_id(0)

window = gtk.Window()
window.set_title("Basic TreeView Example")
window.add(view)
window.show_all()
window.connect("delete-event", gtk.main_quit)
gtk.main()
