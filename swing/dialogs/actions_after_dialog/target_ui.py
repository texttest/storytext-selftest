from javax.swing import JFrame, JPanel, JButton, JOptionPane
from java.awt import BorderLayout

class ConfirmDialogApp:                  
    def make_ui(self):                
        self.frame = JFrame("Dialog Demo")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        panel = JPanel()
        button = JButton("Dialog", actionPerformed=self.showDialog)
        panel.add(button)
        button2 = JButton("Message", actionPerformed=self.printMessage)
        panel.add(button2)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)

    def showDialog(self, event):
        confirmed = JOptionPane.showConfirmDialog(self.frame, 
                                                    "Is the Pope a Catholic?", 
                                                    "User Confirmation", 
                                                    JOptionPane.YES_NO_OPTION)
        print "Dialog answered", confirmed

    def printMessage(self, event):
        print "Hello World!"

    @staticmethod                    
    def main():
        app = ConfirmDialogApp()
        app.make_ui()

ConfirmDialogApp.main()
