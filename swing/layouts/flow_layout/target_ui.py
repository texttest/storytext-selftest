from javax.swing import JButton, JPanel, JFrame, JLabel, JTextField, WindowConstants
from java.awt import FlowLayout

def getBox(num):
    horizPane = JPanel()
    horizPane.setLayout(FlowLayout())
    horizPane.add(JLabel("Box " + str(num)))
    horizPane.add(JTextField())
    return horizPane

# Create and set up the window.
frame = JFrame("ButtonDemo")
frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)

newContentPane = JPanel()
newContentPane.setLayout(FlowLayout())
newContentPane.add(getBox(1))
newContentPane.add(JLabel("A Label"))
newContentPane.add(JButton("A Button"))
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
