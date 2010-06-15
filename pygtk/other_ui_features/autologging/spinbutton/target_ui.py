#$Id: spinbutton.py,v 1.3 2004/04/22 04:31:18 mandava Exp $

# This example illustrates spin button. 

# Importing pygtk module and initializing it.
import gtk


class spinbuttonexample:

	# Call back function to be implemented when the checkbutton snap_to_0.5
	# _ticks is checked 
    def toggle_snap(self, widget, spin):
        spin.set_snap_to_ticks(widget.get_active())
    
	# Call back function to be implemented whrn the checkbutton
        # numeric_only_inputmode is checked
    def toggle_numeric(self, widget, spin):
        spin.set_numeric(widget.get_active())

        # Call back function for spinbutton value_changed
    def change_digits(self, widget, spin, spin1):
        spin1.set_digits(spin.get_value_as_int())

    # Call back function to be implemented when value as int or value as
    # float buttons are clicked 
    def get_value(self, widget, data, spin, spin2, label):
        if data == 1:
            buf = "%d" % spin.get_value_as_int()
        else:
            buf = "%0.*f" % (spin2.get_value_as_int(),
                             spin.get_value())
        label.set_text(buf)

    def __init__(self):
    
        # Create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
       	# Set the handler for destroy that immediately quits gtk 
       	window.connect("destroy", gtk.mainquit)
       
       	# Set the ttle of the window to spin button
       	window.set_title("Spin Button")

        # Create a vertical box.
       	main_vbox = gtk.VBox(False, 5)
        
       	# Set the border width of the vertical box.
       	main_vbox.set_border_width(10)
        
       	# Add the vertical box into the window.
       	window.add(main_vbox)

        # Create a frame
       	frame = gtk.Frame("Not accelerated")
        
       	# Pack the frame into the vertical box.
       	main_vbox.pack_start(frame, True, True, 0)
  
        # Create a new vertical box
       	vbox = gtk.VBox(False, 0)
        
       	# Set the border width
       	vbox.set_border_width(5)
        
       	# Add the vertical box into the frame.
       	frame.add(vbox)

        # Day, month, year spinners
        # Packing with boxes.
       	hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, True, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

        # Setting the 'day' field and packing it 
       	label = gtk.Label("Day :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        # Using adjustment object to hold information about the range of
        # values that the spin button can take.
       	adj = gtk.Adjustment(1, 1, 31, 1, 5, 0)
        
       	# create a spin button and pack into the vertical box.
       	spinner = gtk.SpinButton(adj, 0, 0)
        spinner.set_wrap(True)
        spinner.set_name("Day")
        vbox2.pack_start(spinner, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        # Setting the 'month' field and packing it
       	label = gtk.Label("Month :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)

        # Using adjustment object to hold information about the range of 
       	# values that 'month' field can take 
       	adj = gtk.Adjustment(1, 1, 12, 1, 5, 0)
        
       	# Creating a spin button and packing it.
       	spinner = gtk.SpinButton(adj, 0, 0)
        spinner.set_name("Month")
        spinner.set_wrap(True)
        vbox2.pack_start(spinner, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        # Setting the 'year' field and packing it.
       	label = gtk.Label("Year :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        # Using adjustment object to hold information about the range of
        # values that 'year' field can take
       	adj = gtk.Adjustment(1998, 0, 2100, 1, 100, 0)
        
       	# Create a spin button
       	spinner = gtk.SpinButton(adj, 0, 0)
        spinner.set_wrap(False)
        spinner.set_name("Year")
        spinner.set_size_request(55, -1)
        vbox2.pack_start(spinner, False, True, 0)
  
        # Create an other frame 'accelerated' and pack it into the main
        # vertical box. 
       	frame = gtk.Frame("Accelerated")
        main_vbox.pack_start(frame, True, True, 0)
  
        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        frame.add(vbox)
  
        # create a horizontal box and pack it into the vertical box
       	hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        # Setting the 'value' field and packing it. 
       	label = gtk.Label("Value :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
       	# Using adjustment object to hold information about the range of
        # values that 'value' field can take
       	adj = gtk.Adjustment(0.0, -10000.0, 10000.0, 0.5, 100.0, 0.0)
        
       	# Create a spinbutton and pack it
       	spinner1 = gtk.SpinButton(adj, 1.0, 2)
        spinner1.set_wrap(True)
        spinner1.set_name("Value")
        spinner1.set_size_request(100, -1)
        vbox2.pack_start(spinner1, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
       	# Setting up the 'digits' field and pack it
        label = gtk.Label("Digits :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
       	# Using adjustment object to hold information about the range of
        # values that 'value' field can take
        adj = gtk.Adjustment(2, 1, 5, 1, 1, 0)

       	# Create a spin button and pack it 
        spinner2 = gtk.SpinButton(adj, 0.0, 0)
        spinner2.set_wrap(True)
     	adj.connect("value_changed", self.change_digits, spinner2,
		spinner1)
        vbox2.pack_start(spinner2, False, True, 0)
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)

        # Create a checkbutton for snap to 0.5 ticks
       	button = gtk.CheckButton("Snap to 0.5-ticks")
        button.connect("clicked", self.toggle_snap, spinner1)
        vbox.pack_start(button, True, True, 0)
        button.set_active(True)
  		
       	# Create a checkbutton for numeric only input mode
        button = gtk.CheckButton("Numeric only input mode")
        button.connect("clicked", self.toggle_numeric, spinner1)
        vbox.pack_start(button, True, True, 0)
        button.set_active(True)
  
        val_label = gtk.Label("")
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
        
       	# Create buttons for 'valus as int' and 'valus as float' fields and
       	# set handlers 
       	button = gtk.Button("Value as Int")
        button.connect("clicked", self.get_value, 1, spinner1, spinner2,
                       val_label)
        hbox.pack_start(button, True, True, 5)
  
        button = gtk.Button("Value as Float")
        button.connect("clicked", self.get_value, 2, spinner1, spinner2,
                       val_label)
        hbox.pack_start(button, True, True, 5)
  
        vbox.pack_start(val_label, True, True, 0)
        val_label.set_text("0")
  
        hbox = gtk.HBox(False, 0)
        main_vbox.pack_start(hbox, False, True, 0)
  		
       	# Create a button for close
        button = gtk.Button("Close")
        button.connect("clicked", gtk.main_quit)
        hbox.pack_start(button, True, True, 5)
        window.show_all()

    def main(self):
        gtk.main()
        return 0

if __name__ == "__main__":
    spin = spinbuttonexample()
    spin.main()

