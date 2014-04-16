from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JLabel, JTextField, JToolBar, JPanel, JButton

class ToolBarApp:
        
    def make_ui(self):
        self.frame = JFrame("Tool bar demo")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        panel = JPanel()
        panel.setLayout(BorderLayout())
        panel.setPreferredSize(Dimension(500, 150))
        self.toolbar = self.createToolBar()
        panel.add(self.toolbar, BorderLayout.NORTH)
        showButton = JButton('Show Toolbar', actionPerformed=self.showToolbar)
        panel.add(showButton, BorderLayout.CENTER)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)

    def createToolBar(self):
        toolBar = JToolBar()
        self.addButtons(toolBar)
        toolBar.setVisible(False)
        return toolBar
    
    def addButtons(self, toolBar):
        toolBar.add(JLabel("Value"))
        toolBar.add(JTextField(actionPerformed=self.activated))
            
    def showToolbar(self, event):
        self.toolbar.setVisible(True)
        self.frame.setTitle("New Title")

    def activated(self, event):
        print "Activated", event.getSource().getText()
        
    @staticmethod        
    def main():
        app = ToolBarApp()
        app.make_ui()

ToolBarApp.main()
