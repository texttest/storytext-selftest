
from javax.swing import JButton, JPanel, JFrame, WindowConstants
from java.awt.event import ActionListener

# Create and set up the window.
frame = JFrame("ButtonDemo")
frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)

class PrintListener(ActionListener):
    def actionPerformed(self, *args):
        print "Hello World!"

b1 = JButton("Hello!")
b1.addActionListener(PrintListener())

newContentPane = JPanel()
newContentPane.add(b1)
newContentPane.setOpaque(True) #content panes must be opaque
frame.setContentPane(newContentPane)

#Display the window.
frame.pack()
frame.setVisible(True)
