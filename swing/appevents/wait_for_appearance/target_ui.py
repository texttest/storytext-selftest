from javax.swing import JFrame, JPanel, JButton, Timer
from java.awt import BorderLayout
from java.awt.event import ActionListener

class ApplicationEventApp:
    def make_ui(self):
        self.frame = JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = JButton("Get Exit!", actionPerformed=self.handleButton)

        self.panel = JPanel()
        self.panel.add(button1)
        self.frame.add(self.panel)
        self.frame.pack()
        self.frame.setVisible(True)
    
    def close(self, event):
        self.frame.dispose()
    
    def handleButton(self, event):
        class ButtonListener(ActionListener):
            def actionPerformed(lself, event):
                self.button2 = JButton("Exit", actionPerformed=self.close)
                self.panel.add(self.button2)
                self.frame.pack()
                
        timer = Timer(1000, ButtonListener())
        timer.setRepeats(False)
        timer.start()

    @staticmethod
    def main():
        app = ApplicationEventApp()
        app.make_ui()

ApplicationEventApp.main()

