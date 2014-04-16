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
        confirmed = JOptionPane.showOptionDialog(self.frame, 
                                                 "Are you sure you want to exit?", 
                                                 "User Confirmation", 
                                                 JOptionPane.YES_NO_OPTION,
                                                 JOptionPane.QUESTION_MESSAGE, None,
                                                 [ "Ok", "close" ], "Ok")
        if confirmed == JOptionPane.YES_OPTION:
            self.frame.dispose()

    @staticmethod                    
    def main():
        app = ConfirmDialogApp()
        app.make_ui()

ConfirmDialogApp.main()
