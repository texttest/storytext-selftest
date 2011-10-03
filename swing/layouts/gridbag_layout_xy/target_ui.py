from javax import swing
from java.awt import *
from java.util import *

def makeButton(name, layout, constraints, panel, x, y):
    button = swing.JButton(name)
    constraints.gridx = x
    constraints.gridy = y
    layout.setConstraints(button, constraints)
    panel.add(button)


if __name__ == "__main__":
    frame = swing.JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = swing.JPanel()
    
    gridbag = GridBagLayout()
    constraints = GridBagConstraints()

    panel.setLayout(gridbag)
        
    constraints.fill = GridBagConstraints.BOTH
    makeButton("Button One", gridbag, constraints, panel, 0, 0)
    makeButton("Button Two", gridbag, constraints, panel, 1, 0)
    makeButton("Button Three", gridbag, constraints, panel, 2, 0)
    makeButton("Button Four", gridbag, constraints, panel, 3, 0)
                
    makeButton("Button Six", gridbag, constraints, panel, 2, 2)
    
    makeButton("Button Seven", gridbag, constraints, panel, 3, 2)

    makeButton("Button Five", gridbag, constraints, panel, 0, 1) #another row

    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

