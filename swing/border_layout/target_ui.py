
from javax.swing import JButton, JPanel, JFrame, WindowConstants
from java.awt.event import ActionListener
from java.awt import BorderLayout

# Create and set up the window.
frame = JFrame("ButtonDemo")
frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)

newContentPane = JPanel()
newContentPane.setLayout(BorderLayout())
newContentPane.add(JButton("North"), BorderLayout.NORTH);
newContentPane.add(JButton("South"), BorderLayout.SOUTH);
newContentPane.add(JButton("East"), BorderLayout.EAST);
newContentPane.add(JButton("West"), BorderLayout.WEST);
newContentPane.add(JButton("Center"), BorderLayout.CENTER);
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
