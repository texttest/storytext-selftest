from javax import swing
from java.awt import BorderLayout, Toolkit, AWTEvent, Frame
from java.awt.event import ActionListener, ActionEvent

class ApplicationEventManager:
    APP_EVENT_STR = "ApplicationEvent"
    instance = None
    
    def __init__(self):
        self.button = swing.JButton()
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
        self.frame = swing.JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = swing.JButton("Why?", actionPerformed=self.handleButton)
        self.button2 = swing.JButton("Exit", actionPerformed=self.close)
        self.button2.setEnabled(False)

        panel = swing.JPanel()
        panel.add(button1)
        panel.add(self.button2)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)
    
    def close(self, event):
        self.frame.dispose()
    
        
    def handleButton(self, event):
        print "Because"
        self.button2.setEnabled(True)
        ApplicationEventManager.instance.sendApplicationEvent("Exit button to be enabled")
        
    @staticmethod
    def main():
        app = ApplicationEventApp()
        app.make_ui()

ApplicationEventApp.main()

