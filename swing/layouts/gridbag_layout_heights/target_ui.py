from javax import swing
from java.awt import *
from java.util import *


if __name__ == "__main__":
    frame = swing.JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(swing.WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = swing.JPanel()
    
    gridbag = GridBagLayout()
    constraints = GridBagConstraints()

    panel.setLayout(gridbag)
        
    constraints.fill = GridBagConstraints.HORIZONTAL
    label = swing.JLabel("Name")
    gridbag.setConstraints(label, constraints)
    panel.add(label)

    constraints.fill = GridBagConstraints.BOTH
    text = swing.JTextField()
    gridbag.setConstraints(text, constraints)
    panel.add(text)
    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

