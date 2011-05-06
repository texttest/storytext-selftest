from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent
from java.lang import System
class ToolBarApp:
        
    def make_ui(self):
        frame = swing.JFrame("Tool bar demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        panel = swing.JPanel()
        panel.setPreferredSize(Dimension(200, 150))
        panel.add(self.createToolBar())
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createToolBar(self):
        toolBar = swing.JToolBar()
        self.addButtons(toolBar)
        return toolBar
    
    def addButtons(self, toolBar):
        for i in range(1, 6):
            button = swing.JButton('Item' + str(i), actionPerformed=self.printButton)
            toolBar.add(button)
            
    def printButton(self, event):
        widget = event.getSource()
        print "Selected Tool bar's",widget.getText()
        
    def quit(self, event):
        self.printMenu(event)
        System.exit(0);

    @staticmethod        
    def main():
        app = ToolBarApp()
        app.make_ui()

ToolBarApp.main()
