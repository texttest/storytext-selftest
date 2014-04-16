from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent
from javax.swing import JFrame, JMenu, JMenuBar, JMenuItem, JPanel, JLabel, JTextField, KeyStroke

class MenuApp:
        
    def make_ui(self):
        self.frame = JFrame("Menu demo")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        panel2 = JPanel(BorderLayout())
        textLabel = JLabel("Some Text: ")
        self.textField = JTextField()
        panel2.add(textLabel, BorderLayout.WEST)
        panel2.add(self.textField, BorderLayout.CENTER)
        panel2.setOpaque(True) #content panes must be opaque
        self.frame.setContentPane(panel2)
        self.frame.setJMenuBar(self.createMenuBar())
        self.frame.setPreferredSize(Dimension(150, 100))
        self.frame.pack()
        self.frame.setVisible(True)

    def createMenuBar(self):
        menuBar = JMenuBar()
        menu = JMenu("File")
        menu.setMnemonic(KeyEvent.VK_F)
        addItem = JMenuItem("Add Text", actionPerformed=self.addText)
        addItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_T, KeyEvent.CTRL_MASK))       
        menu.add(addItem)
        quitItem = JMenuItem("Quit", actionPerformed=self.quit)
        quitItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, KeyEvent.CTRL_MASK))       
        menu.add(quitItem)
        menuBar.add(menu)
        return menuBar

    def addText(self, event):
        self.textField.setText("Added" + self.textField.getText())

    def quit(self, event):
        self.frame.dispose()

    @staticmethod            
    def main():
        app = MenuApp()
        app.make_ui()

MenuApp.main()


