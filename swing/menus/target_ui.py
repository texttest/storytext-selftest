from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent
from java.lang import System
from javax.swing import JFrame, JMenu, JMenuBar, JMenuItem, JPanel, JButton, KeyStroke

class MenuApp:
        
    def make_ui(self):
        frame = JFrame("Menu demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        b1 = JButton("Hello!")
        
        newContentPane = JPanel()
        newContentPane.add(b1)
        newContentPane.setOpaque(True) #content panes must be opaque
        frame.setContentPane(newContentPane)
        frame.setJMenuBar(self.createMenuBar())
        frame.setPreferredSize(Dimension(150, 100))
        frame.pack()
        frame.setVisible(True)

    def createMenuBar(self):
        menuBar = JMenuBar()
        menu = JMenu("File")
        menu.setMnemonic(KeyEvent.VK_F)
        menu.add(JMenuItem("Select All", actionPerformed=self.printMenu))
        
        menu.addSeparator();
        subMenu = JMenu("Sub menu")
        smItem = JMenuItem("Item", actionPerformed=self.printMenu) 
        
        menu.add(subMenu)
        menu.addSeparator()
        subMenu.add(smItem)
        invisibleItem = JMenuItem("Invisible Item", actionPerformed=self.printMenu)
        menu.add(invisibleItem)
        invisibleItem.setVisible(False)
        quitItem = JMenuItem("Quit", actionPerformed=self.quit)
        quitItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, KeyEvent.CTRL_MASK))       
        menu.add(quitItem)
        menuBar.add(menu)
        return menuBar

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


