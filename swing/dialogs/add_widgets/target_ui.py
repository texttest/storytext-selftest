from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent, WindowAdapter
from java.lang import System, Runnable, Thread
from javax.swing import JOptionPane, SwingUtilities

class ConfirmDialogApp:                  
    def make_ui(self):                
        self.frame = swing.JFrame("Confirm Dialog Demo")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        panel = swing.JPanel()
        button = swing.JButton("Dialog", actionPerformed=self.showDialog)
        panel.add(button)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)

    def showDialog(self, event):
        dialog = swing.JDialog(self.frame, "The Dialog", True)
        dialog.setDefaultCloseOperation(swing.JDialog.DISPOSE_ON_CLOSE)
        dialog.setLayout(BorderLayout())
        panel = swing.JPanel()
        panel.setPreferredSize(Dimension(500, 150))
        self.toolbar = self.createToolBar()
        panel.add(self.toolbar)        
        dialog.setContentPane(panel)
        dialog.pack()
        dialog.setLocationRelativeTo(self.frame)
        dialog.setVisible(True)
        
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
        app = ConfirmDialogApp()
        app.make_ui()

ConfirmDialogApp.main()
