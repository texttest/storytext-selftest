from javax.swing import JLabel, JPanel, JFrame, JTextField, BoxLayout, WindowConstants

def getBox(num):
    horizPane = JPanel()
    horizPane.setLayout(BoxLayout(horizPane, BoxLayout.X_AXIS))
    horizPane.add(JLabel("Box " + str(num) + " with a load of extra text to make it really wide"))
    horizPane.add(JTextField())
    return horizPane

# Create and set up the window.
frame = JFrame("ButtonDemo")
frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)

newContentPane = JPanel()
newContentPane.setLayout(BoxLayout(newContentPane, BoxLayout.X_AXIS))
newContentPane.add(getBox(1))
newContentPane.add(getBox(2))
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
