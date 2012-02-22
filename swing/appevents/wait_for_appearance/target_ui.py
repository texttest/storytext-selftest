from javax import swing
from java.awt import BorderLayout, Toolkit, AWTEvent, Frame
from java.awt.event import ActionListener, ActionEvent, MouseEvent

class ApplicationEventApp:
    def make_ui(self):
        self.frame = swing.JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = swing.JButton("Get Exit!", actionPerformed=self.handleButton)

        self.panel = swing.JPanel()
        self.panel.add(button1)
        self.frame.add(self.panel)
        self.frame.pack()
        self.frame.setVisible(True)
    
    def close(self, event):
        self.frame.dispose()
    
    def handleButton(self, event):
        class ButtonListener(ActionListener):
            def actionPerformed(lself, event):
                self.button2 = swing.JButton("Exit", actionPerformed=self.close)
                self.panel.add(self.button2)
                self.frame.pack()
                
        timer = swing.Timer(1000, ButtonListener())
        timer.setRepeats(False)
        timer.start()

    @staticmethod
    def main():
        app = ApplicationEventApp()
        app.make_ui()

ApplicationEventApp.main()

