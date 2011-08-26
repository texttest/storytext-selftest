
from javax import swing
from java import awt
from java.lang import System

class MyInternalFrame(swing.JInternalFrame):
    openFrameCount = 0
    xOffset = 30
    yOffset = 30

    def __init__(self):
        MyInternalFrame.openFrameCount += 1
        swing.JInternalFrame.__init__(self,
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


class InternalFrameDemo(swing.JFrame, awt.event.ActionListener):
    def __init__(self):
        swing.JFrame.__init__(self, "Internal Frame Demo")
        self.desktop = swing.JDesktopPane()

        #Set up the GUI.
        desktop = swing.JDesktopPane() #a specialized layered pane
        self.createFrame() #create first "window"
        self.setContentPane(self.desktop)
        self.setJMenuBar(self.createMenuBar())

        #Make dragging a little faster but perhaps uglier.
        self.desktop.setDragMode(swing.JDesktopPane.OUTLINE_DRAG_MODE)
        self.setSize(500, 500)

    def createMenuBar(self): 
        menuBar = swing.JMenuBar()

        #Set up the lone menu.
        menu = swing.JMenu("Document")
        menuBar.add(menu)

        #Set up the first menu item.
        menuItem = swing.JMenuItem("New")
        menuItem.setAccelerator(swing.KeyStroke.getKeyStroke(awt.event.KeyEvent.VK_N, awt.event.ActionEvent.ALT_MASK))
        menuItem.setActionCommand("new")
        menuItem.addActionListener(self)
        menu.add(menuItem)

        #Set up the second menu item.
        menuItem = swing.JMenuItem("Quit")
        menuItem.setMnemonic(awt.event.KeyEvent.VK_Q)
        menuItem.setAccelerator(swing.KeyStroke.getKeyStroke(awt.event.KeyEvent.VK_Q, awt.event.ActionEvent.ALT_MASK))
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
        frame.setDefaultCloseOperation(swing.JFrame.EXIT_ON_CLOSE)

        #Display the window.
        frame.setVisible(True)
    

if __name__ == "__main__":
    InternalFrameDemo.createAndShowGUI()
    

