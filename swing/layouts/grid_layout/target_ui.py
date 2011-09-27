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
    
    grid = GridLayout(3, 3)

    panel.setLayout(grid)

    panel.add(swing.JButton("Button One"))
    panel.add(swing.JButton("Button Two"))
    panel.add(swing.JButton("Button Three"))
        
    panel.add(swing.JButton("Button Four"))
        
    panel.add(swing.JButton("Button Five With A Long Name"))
        
    panel.add(swing.JButton("Button Six"))
    
    panel.add(swing.JButton("Button Seven"))

    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

