from javax.swing import JFrame, JPanel, JButton, Timer
from java.awt import BorderLayout, Frame
from java.awt.event import ActionListener


class ApplicationEventManager:
    APP_EVENT_STR = "ApplicationEvent"
    instance = None
    
    def __init__(self):
        self.button = JButton()
        self.button.setSize(0, 0)
        self.button.setVisible(False)

    def findContainer(self):
        return Frame.getFrames()[0]

    def sendApplicationEvent(self, message):
        self.button.setText(self.APP_EVENT_STR + " " + message)
        if self.button.getParent() is None:
            self.findContainer().add(self.button)
        self.button.doClick()


ApplicationEventManager.instance = ApplicationEventManager()

class ApplicationEventApp:
    def make_ui(self):
        self.stupidFrame = JFrame("Not Really")
        self.frame = JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = JButton("Why?", actionPerformed=self.handleButton)
        self.button2 = JButton("Exit", actionPerformed=self.close)
        self.button2.setEnabled(False)

        panel = JPanel()
        panel.add(button1)
        panel.add(self.button2)
        self.frame.add(panel)
        self.frame.pack()
        self.stupidFrame.setVisible(False)
        self.frame.setVisible(True)
    
    def close(self, event):
        self.stupidFrame.dispose()
        self.frame.dispose()
    
    def handleButton(self, event):
        class ButtonListener(ActionListener):
            def actionPerformed(lself, event):
                print "Because"
                self.button2.setEnabled(True)
                ApplicationEventManager.instance.sendApplicationEvent("Exit button to be enabled")
                
        timer = Timer(1000, ButtonListener())
        timer.setRepeats(False)
        timer.start()

    @staticmethod
    def main():
        app = ApplicationEventApp()
        app.make_ui()

ApplicationEventApp.main()

