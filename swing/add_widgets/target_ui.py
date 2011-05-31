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
        panel.setPreferredSize(Dimension(500, 150))
        self.toolbar = self.createToolBar()
        panel.add(self.toolbar)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createToolBar(self):
        toolBar = swing.JToolBar()
        self.addButtons(toolBar)
        return toolBar
    
    def addButtons(self, toolBar):
        for i in range(1, 6):
            button = swing.JButton('Item' + str(i), actionPerformed=self.addButton)
            toolBar.add(button)
            
    def addButton(self, event):
        widget = event.getSource()
        newButton = swing.JButton('Extra ' + widget.getText(), actionPerformed=self.addButton)
        self.toolbar.add(newButton)
        
    def quit(self, event):
        self.printMenu(event)
        System.exit(0);

    @staticmethod        
    def main():
        app = ToolBarApp()
        app.make_ui()

ToolBarApp.main()
