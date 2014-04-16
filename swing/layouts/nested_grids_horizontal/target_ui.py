from javax.swing import JButton, JPanel, JFrame, WindowConstants
from java.awt import GridBagLayout, GridBagConstraints, GridLayout

def makeButton(name, layout, constraints, panel, x, y):
    button = JButton(name)
    constraints.gridx = x
    constraints.gridy = y
    layout.setConstraints(button, constraints)
    panel.add(button)


def makeGridBagPanel():
    gridbag = GridBagLayout()
    panel = JPanel(gridbag)
    constraints = GridBagConstraints()
    constraints.fill = GridBagConstraints.BOTH
    makeButton("Button One", gridbag, constraints, panel, 0, 0)
    makeButton("Button Two", gridbag, constraints, panel, 1, 0)
    return panel

if __name__ == "__main__":
    frame = JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = JPanel(GridLayout())
    
    subpanel1 = JPanel(GridBagLayout())
    panel.add(subpanel1)

    panel.add(makeGridBagPanel())
    panel.add(makeGridBagPanel())
            
    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

