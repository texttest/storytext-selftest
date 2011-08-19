from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent
from java.lang import System
class MenuApp:
        
    def make_ui(self):
        frame = swing.JFrame("Menu demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        b1 = swing.JButton("Add Stuff", actionPerformed=self.addToMenus)
        
        newContentPane = swing.JPanel()
        newContentPane.add(b1)
        newContentPane.setOpaque(True) #content panes must be opaque
        frame.setContentPane(newContentPane)
        self.menuBar = self.createMenuBar()
        frame.setJMenuBar(self.menuBar)
        frame.setPreferredSize(Dimension(150, 100))
        frame.pack()
        frame.setVisible(True)

    def createMenuBar(self):
        menuBar = swing.JMenuBar()
        menu = swing.JMenu("File")
        menu.setMnemonic(KeyEvent.VK_F)
        
        quitItem = swing.JMenuItem("Quit", actionPerformed=self.quit)
        quitItem.setAccelerator(swing.KeyStroke.getKeyStroke(KeyEvent.VK_Q, KeyEvent.CTRL_MASK))       
        menu.add(quitItem)
        menuBar.add(menu)

        self.newmenu = swing.JMenu("New")
        self.newmenu.add(swing.JMenuItem("Select All", actionPerformed=self.printMenu))
        self.newmenu.setVisible(False)
        menuBar.add(self.newmenu)
        return menuBar

    def addToMenus(self, *args):
        self.newmenu.setVisible(True)
        
    def printMenu(self, event):
        widget = event.getSource()
        print "Selected the",widget.getText(), "menu"
        
    def quit(self, event):
        self.printMenu(event)
        System.exit(0);

    @staticmethod            
    def main():
        app = MenuApp()
        app.make_ui()

MenuApp.main()


