# -*- encoding: latin-1 -*-

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
    makeButton("Button Två", gridbag, constraints, panel, 1, 0)
    return panel

if __name__ == "__main__":
    frame = swing.JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)

    layout = GridBagLayout()
    panel = swing.JPanel(layout)
    constraints = GridBagConstraints()
    constraints.fill = GridBagConstraints.BOTH
    constraints.gridx = 0
    constraints.gridy = 0

    subpanel1 = swing.JPanel(GridBagLayout())
    layout.setConstraints(subpanel1, constraints)
    panel.add(subpanel1)

    subpanel2 = swing.JPanel(GridBagLayout())
    subpanel2.add(makeGridBagPanel())
    constraints.gridx = 1
    layout.setConstraints(subpanel2, constraints)
    panel.add(subpanel2)

    subpanel3 = makeGridBagPanel()
    constraints.gridx = 2
    layout.setConstraints(subpanel3, constraints)
    panel.add(subpanel3)
            
    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

