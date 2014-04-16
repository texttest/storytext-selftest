from java.awt.event import ActionListener, KeyEvent, ActionEvent
from java.lang import System
from javax.swing import JFrame, JInternalFrame, JDesktopPane, JMenu, JMenuItem, JMenuBar,KeyStroke

class MyInternalFrame(JInternalFrame):
    openFrameCount = 0
    xOffset = 30
    yOffset = 30

    def __init__(self):
        MyInternalFrame.openFrameCount += 1
        JInternalFrame.__init__(self,
                                      "Document #" + str(MyInternalFrame.openFrameCount), 
                                      True, #resizable
                                      True, #closable
                                      True, #maximizable
                                      True) #iconifiable

        #...Create the GUI and put it in the window...

        #...Then set the window size or call pack...
        self.setSize(300,300)

        #Set the window's location.
        self.setLocation(self.xOffset*self.openFrameCount, self.yOffset*self.openFrameCount)


class InternalFrameDemo(JFrame, ActionListener):
    def __init__(self):
        JFrame.__init__(self, "Internal Frame Demo")
        self.desktop = JDesktopPane()

        #Set up the GUI.
        desktop = JDesktopPane() #a specialized layered pane
        self.createFrame() #create first "window"
        self.setContentPane(self.desktop)
        self.setJMenuBar(self.createMenuBar())

        #Make dragging a little faster but perhaps uglier.
        self.desktop.setDragMode(JDesktopPane.OUTLINE_DRAG_MODE)
        self.setSize(500, 500)

    def createMenuBar(self): 
        menuBar = JMenuBar()

        #Set up the lone menu.
        menu = JMenu("Document")
        menuBar.add(menu)

        #Set up the first menu item.
        menuItem = JMenuItem("New")
        menuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, ActionEvent.ALT_MASK))
        menuItem.setActionCommand("new")
        menuItem.addActionListener(self)
        menu.add(menuItem)

        #Set up the second menu item.
        menuItem = JMenuItem("Quit")
        menuItem.setMnemonic(KeyEvent.VK_Q)
        menuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, ActionEvent.ALT_MASK))
        menuItem.setActionCommand("quit")
        menuItem.addActionListener(self)
        menu.add(menuItem)

        return menuBar

    #React to menu selections.
    def actionPerformed(self, e):
        if e.getActionCommand() == "new":
            self.createFrame()
        else:  #quit
            self.quit()
        
    #Create a new internal frame.
    def createFrame(self):
        frame = MyInternalFrame()
        frame.setVisible(True) #necessary as of 1.3
        self.desktop.add(frame)
        frame.setSelected(True)
        
    #Quit the application.
    def quit(self): 
        System.exit(0)

    @staticmethod
    def createAndShowGUI():
        #Create and set up the window.
        frame = InternalFrameDemo()
        #Make sure we have nice window decorations.
        frame.setDefaultLookAndFeelDecorated(True)
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

        #Display the window.
        frame.setVisible(True)
    

if __name__ == "__main__":
    InternalFrameDemo.createAndShowGUI()
    

