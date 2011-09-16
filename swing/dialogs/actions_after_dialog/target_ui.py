from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent, WindowAdapter
from java.lang import System, Runnable, Thread
from javax.swing import JOptionPane, SwingUtilities

class ConfirmDialogApp:                  
    def make_ui(self):                
        self.frame = swing.JFrame("Dialog Demo")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        panel = swing.JPanel()
        button = swing.JButton("Dialog", actionPerformed=self.showDialog)
        panel.add(button)
        button2 = swing.JButton("Message", actionPerformed=self.printMessage)
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
