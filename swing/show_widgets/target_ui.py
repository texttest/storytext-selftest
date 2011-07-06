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
        panel.setLayout(BorderLayout())
        panel.setPreferredSize(Dimension(500, 150))
        self.toolbar = self.createToolBar()
        panel.add(self.toolbar, BorderLayout.NORTH)
        showButton = swing.JButton('Show Toolbar', actionPerformed=self.showToolbar)
        panel.add(showButton, BorderLayout.CENTER)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createToolBar(self):
        toolBar = swing.JToolBar()
        self.addButtons(toolBar)
        toolBar.setVisible(False)
        return toolBar
    
    def addButtons(self, toolBar):
        toolBar.add(swing.JLabel("Value"))
        toolBar.add(swing.JTextField(actionPerformed=self.activated))
            
    def showToolbar(self, event):
        self.toolbar.setVisible(True)

    def activated(self, event):
        print "Activated", event.getSource().getText()
        
    @staticmethod        
    def main():
        app = ToolBarApp()
        app.make_ui()

ToolBarApp.main()
