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
        button = swing.JButton("Exit", actionPerformed=self.quitDialog)
        panel.add(button)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)

    def quitDialog(self, event):
        confirmed = JOptionPane.showConfirmDialog(self.frame, 
                                                    "Are you sure you want to exit?", 
                                                    "User Confirmation", 
                                                    JOptionPane.YES_NO_OPTION)
        if confirmed == JOptionPane.YES_OPTION:
            JOptionPane.showMessageDialog(self.frame, "You are going to exit")
            self.frame.dispose()

    @staticmethod                    
    def main():
        app = ConfirmDialogApp()
        app.make_ui()

ConfirmDialogApp.main()
