from javax.swing import JLabel, JPanel, JFrame, JTextField, WindowConstants
from java.awt import GridBagLayout, GridBagConstraints

if __name__ == "__main__":
    frame = JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = JPanel()
    
    gridbag = GridBagLayout()
    constraints = GridBagConstraints()

    panel.setLayout(gridbag)
        
    constraints.fill = GridBagConstraints.HORIZONTAL
    label = JLabel("Name")
    gridbag.setConstraints(label, constraints)
    panel.add(label)

    constraints.fill = GridBagConstraints.BOTH
    text = JTextField()
    gridbag.setConstraints(text, constraints)
    panel.add(text)
    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

