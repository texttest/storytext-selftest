from javax import swing
from java.awt import *
from java.util import *

def makeButton(name, layout, constraints, panel, x, y):
    button = swing.JButton(name)
    constraints.gridx = x
    constraints.gridy = y
    layout.setConstraints(button, constraints)
    panel.add(button)


def makeGridBagPanel():
    gridbag = GridBagLayout()
    panel = swing.JPanel(gridbag)
    constraints = GridBagConstraints()
    constraints.fill = GridBagConstraints.BOTH
    makeButton("Button One", gridbag, constraints, panel, 0, 0)
    makeButton("Button Two", gridbag, constraints, panel, 1, 0)
    return panel

if __name__ == "__main__":
    frame = swing.JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = swing.JPanel(GridLayout())
    
    subpanel1 = swing.JPanel(GridBagLayout())
    panel.add(subpanel1)

    panel.add(makeGridBagPanel())
    panel.add(makeGridBagPanel())
            
    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

