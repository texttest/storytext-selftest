from javax import swing
from java.awt import *
from java.util import *

def makeButton(name, layout, constraints, panel):
    button = swing.JButton(name)
    layout.setConstraints(button, constraints)
    panel.add(button)


if __name__ == "__main__":
    frame = swing.JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = swing.JPanel()
    
    grid = GridLayout(2, 2)

    panel.setLayout(grid)

    panel.add(swing.JButton("Button One"))
    panel.add(swing.JButton("Button Two"))        
    panel.add(swing.JButton("Button Three With An Excessively Long Name"))
        
    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

