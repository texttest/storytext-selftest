from java.awt.event import KeyEvent, ActionEvent, ActionListener
from javax.swing import JFrame, JMenu, JMenuBar, JMenuItem, KeyStroke

class KeyboardDemo(JFrame, ActionListener):
    def __init__(self):
        JFrame.__init__(self, "Keyboard Demo")
        
        #Set up the GUI.
        self.setJMenuBar(self.createMenuBar())

        self.setSize(500, 500)

    def createMenuBar(self): 
        menuBar = JMenuBar()

        #Set up the lone menu.
        menu = JMenu("File")
        menuBar.add(menu)

        #Set up the first menu item.
        menuItem = JMenuItem("New")
        menuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, ActionEvent.CTRL_MASK))
        menuItem.setActionCommand("new")
        menuItem.addActionListener(self)
        menu.add(menuItem)

        #Set up the second menu item.
        menuItem = JMenuItem("Quit")
        menuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, ActionEvent.CTRL_MASK))
        menuItem.setActionCommand("quit")
        menuItem.addActionListener(self)
        menu.add(menuItem)

        return menuBar

    #React to menu selections.
    def actionPerformed(self, e):
        if e.getActionCommand() == "new":
            print "Here's a new file!"
        else:  #quit
            print "Quitting"
            self.dispose()
                
    @staticmethod
    def main():
        #Create and set up the window.
        frame = KeyboardDemo()
        
        #Display the window.
        frame.setVisible(True)
    

if __name__ == "__main__":
    KeyboardDemo.main()
    

