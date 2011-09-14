
from javax import swing
from java import awt

def getBox(num):
    horizPane = swing.JPanel()
    horizPane.setLayout(awt.FlowLayout())
    horizPane.add(swing.JLabel("Box " + str(num)))
    horizPane.add(swing.JTextField())
    return horizPane

# Create and set up the window.
frame = swing.JFrame("ButtonDemo")
frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)

newContentPane = swing.JPanel()
newContentPane.setLayout(awt.FlowLayout())
newContentPane.add(getBox(1))
newContentPane.add(swing.JLabel("A Label"))
newContentPane.add(swing.JButton("A Button"))
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
