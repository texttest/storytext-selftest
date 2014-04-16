from javax.swing import JButton, JPanel, JFrame, WindowConstants
from java.awt import GridLayout


def makeButton(name, layout, constraints, panel):
    button = JButton(name)
    layout.setConstraints(button, constraints)
    panel.add(button)


if __name__ == "__main__":
    frame = JFrame("ButtonDemo")
    frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
    
    panel = JPanel()
    
    grid = GridLayout(3, 3)

    panel.setLayout(grid)

    panel.add(JButton("Button One"))
    panel.add(JButton("Button Two"))
    panel.add(JButton("Button Three"))
        
    panel.add(JButton("Button Four"))
        
    panel.add(JButton("Button Five With A Long Name"))
        
    panel.add(JButton("Button Six"))
    
    panel.add(JButton("Button Seven"))

    panel.setOpaque(True) #content panes must be opaque
    frame.setContentPane(panel)

    #Display the window.
    frame.pack()
    frame.setVisible(True)

