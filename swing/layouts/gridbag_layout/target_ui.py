from javax.swing import JButton, JPanel, JFrame, WindowConstants
from java.awt import GridBagLayout, GridBagConstraints

def makeButton(name, layout, constraints, panel):
    button = JButton(name)
    layout.setConstraints(button, constraints)
    panel.add(button)


if __name__ == "__main__":
    frame = JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = JPanel()
    
    gridbag = GridBagLayout()
    constraints = GridBagConstraints()

    panel.setLayout(gridbag)
        
    constraints.fill = GridBagConstraints.BOTH
    constraints.weightx = 1.0
    makeButton("Button One", gridbag, constraints, panel)
    makeButton("Button Two", gridbag, constraints, panel)
    makeButton("Button Three", gridbag, constraints, panel)
        
    constraints.weightx = 1.0
    constraints.gridwidth = GridBagConstraints.REMAINDER #end row
    makeButton("Button Four", gridbag, constraints, panel)
        
    constraints.weightx = 0.0                #reset to the default
    makeButton("Button Five With A Long Name", gridbag, constraints, panel) #another row
        
    constraints.gridwidth = GridBagConstraints.RELATIVE #next-to-last in row
    makeButton("Button Six", gridbag, constraints, panel)
    
    constraints.gridwidth = GridBagConstraints.REMAINDER #end row
    makeButton("Button Seven", gridbag, constraints, panel)

    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

