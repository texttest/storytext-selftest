
from javax.swing import JButton, JPanel, JFrame, WindowConstants, BoxLayout
from java.awt.event import ActionListener

# Create and set up the window.
frame = JFrame("ButtonDemo")
frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)

newContentPane = JPanel()
newContentPane.setLayout(BoxLayout(newContentPane, BoxLayout.Y_AXIS))
newContentPane.add(JButton("We"))
newContentPane.add(JButton("Go"))
horizPane = JPanel()
horizPane.setLayout(BoxLayout(horizPane, BoxLayout.X_AXIS))
horizPane.add(JButton("Down"))
horizPane.add(JButton("Then"))
horizPane.add(JButton("Across"))
newContentPane.add(horizPane)
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
