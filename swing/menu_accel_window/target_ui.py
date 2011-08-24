
from javax import swing
from java import awt
from java.lang import System

class KeyboardDemo(swing.JFrame, awt.event.ActionListener):
    def __init__(self):
        swing.JFrame.__init__(self, "Keyboard Demo")
        
        #Set up the GUI.
        self.setJMenuBar(self.createMenuBar())

        self.setSize(500, 500)

    def createMenuBar(self): 
        menuBar = swing.JMenuBar()

        #Set up the lone menu.
        menu = swing.JMenu("File")
        menuBar.add(menu)

        #Set up the first menu item.
        menuItem = swing.JMenuItem("New")
        menuItem.setAccelerator(swing.KeyStroke.getKeyStroke(awt.event.KeyEvent.VK_N, awt.event.ActionEvent.CTRL_MASK))
        menuItem.setActionCommand("new")
        menuItem.addActionListener(self)
        menu.add(menuItem)

        #Set up the second menu item.
        menuItem = swing.JMenuItem("Quit")
        menuItem.setAccelerator(swing.KeyStroke.getKeyStroke(awt.event.KeyEvent.VK_Q, awt.event.ActionEvent.CTRL_MASK))
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
    

