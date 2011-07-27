
from javax import swing
from java.awt.event import ActionListener

def getBox(num):
    horizPane = swing.JPanel()
    horizPane.setLayout(swing.BoxLayout(horizPane, swing.BoxLayout.X_AXIS))
    horizPane.add(swing.JLabel("Box " + str(num) + " with a load of extra text to make it really wide"))
    horizPane.add(swing.JTextField())
    return horizPane

# Create and set up the window.
frame = swing.JFrame("ButtonDemo")
frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)

newContentPane = swing.JPanel()
newContentPane.setLayout(swing.BoxLayout(newContentPane, swing.BoxLayout.X_AXIS))
newContentPane.add(getBox(1))
newContentPane.add(getBox(2))
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
