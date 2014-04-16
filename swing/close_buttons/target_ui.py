from javax.swing import JFrame, JPanel, JButton
from java.awt import BorderLayout

class CloseButtonsApp:
    def make_ui(self):
        self.frame = JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = JButton("Why?", actionPerformed=self.printMessage)
        self.button2 = JButton("Exit",actionPerformed=self.close)
        self.button2.setEnabled(False)
        panel = JPanel()
        panel.add(button1)
        panel.add(self.button2)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)
    
    def close(self, event):
        self.frame.dispose()

    def printMessage(self, event):
        print "Because"
        self.button2.setEnabled(True)
    
    @staticmethod
    def main():
        app = CloseButtonsApp()
        app.make_ui()

CloseButtonsApp.main()
