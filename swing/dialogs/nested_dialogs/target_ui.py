from javax.swing import JFrame, JPanel, JButton, JOptionPane
from java.awt import BorderLayout

class ConfirmDialogApp:                  
    def make_ui(self):                
        self.frame = JFrame("Confirm Dialog Demo")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        panel = JPanel()
        button = JButton("Exit", actionPerformed=self.quitDialog)
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
